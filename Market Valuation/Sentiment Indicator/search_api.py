import os
from serpapi import GoogleSearch
from datetime import datetime, timedelta
import pandas as pd

api_key = os.getenv('SERPAPI_API_KEY')
if not api_key:
    raise ValueError("API key is missing")

def query_google_trends(api_key, search_term):
    params = {
        "engine": "google_trends",
        "q": search_term,
        "data_type": "TIMESERIES",
        "resolution": "DAY",
        "start_time": (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d'),
        "end_time": datetime.now().strftime('%Y-%m-%d'),
        "api_key": api_key
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        return results

    except Exception as e:
        print(f"Google Trends Query Error: {e}")

