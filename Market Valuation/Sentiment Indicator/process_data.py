import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy.stats import norm
import seaborn as sns

def retrieve_timeseries(data, idx):
    results = []
    for entry in data['interest_over_time']['timeline_data']:
        timestamp = entry['timestamp']
        extracted_value = entry['values'][idx]['extracted_value']
        results.append({'timestamp': timestamp, 'value': extracted_value})

    df = pd.DataFrame(results)
    df['timestamp'] = pd.to_numeric(df['timestamp'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='s')
    df.set_index('date', inplace=True)
    df = df.drop('timestamp', axis=1)
    return df

def plot_ts_dist(percent_increases, ax):
    sns.histplot(percent_increases, bins=30, kde=False, color='blue', stat='density', ax=ax)
    
    mu, std = norm.fit(percent_increases)
    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    title = f"Normal Model Fit results: µ = {mu:.2f}, σ = {std:.2f}"
    ax.set_title(title)
    ax.set_xlabel('Percent Increase')
    ax.set_ylabel('Density')

    return mu, std
