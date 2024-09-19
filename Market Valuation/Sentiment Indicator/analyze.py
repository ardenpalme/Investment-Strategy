from process_data import *
from search_api import *
from exchange_api import *  

coin_api_key = "e8e405a3-a21d-4e6b-a963-979f854dbbc3"
query_list="bitcoin,ethereum,crypto,solana"

if __name__ == '__main__':
    api_key = os.getenv('SERPAPI_API_KEY')
    if not api_key:
        raise ValueError("API key is missing")

    query_result = query_google_trends(api_key, query_list)
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(16, 5))

    agg_norm_trends = pd.DataFrame()
    for i, query in enumerate(query_list.split(",")):
        ts = retrieve_timeseries(query_result, i)
        norm_values = (ts['value'] - np.mean(ts['value'])) / np.std(ts['value'])
        norm_ts = pd.DataFrame(data=norm_values)

        if agg_norm_trends.empty:
            agg_norm_trends = norm_ts.copy()
        else:
            agg_norm_trends += norm_ts

    sentiment_trend = agg_norm_trends.values.flatten()
    pct_diff = np.diff(sentiment_trend) / sentiment_trend[:-1] * 100
    plot_ts_dist(pct_diff, ax0)

    # Plot normalized aggregate timeseries
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Z-score')
    ax1.plot(agg_norm_trends.index, agg_norm_trends['value'], marker='o')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Plot BTC price timeseries
    btcusd = get_price_ts('BITSTAMP_SPOT_BTC_USD', coin_api_key, agg_norm_trends.index[0].strftime('%Y-%m-%d'))
    ax2 = ax1.twinx()
    line2, = ax2.plot(btcusd.index, btcusd['price'], color='#4B43E2', label='BTCUSD')
    ax2.tick_params(axis='y', labelcolor='#4B43E2')
    ax2.set_yscale('log')

    # Plot ETH price timeseries
    ethusd = get_price_ts('BITSTAMP_SPOT_ETH_USD', coin_api_key, agg_norm_trends.index[0].strftime('%Y-%m-%d'))
    ax3 = ax1.twinx()
    line3, = ax3.plot(ethusd.index, ethusd['price'], color='tab:orange', label='ETHUSD')
    ax3.tick_params(axis='y', labelcolor='tab:orange')
    ax3.set_yscale('log')

    # Plot SOL price timeseries
    solusd = get_price_ts('BITSTAMP_SPOT_SOL_USD', coin_api_key, agg_norm_trends.index[0].strftime('%Y-%m-%d'))
    ax4 = ax1.twinx()
    line4, = ax4.plot(solusd.index, solusd['price'], color='#E2AA43', label='SOLUSD')
    ax4.tick_params(axis='y', labelcolor='#E2AA43')
    ax4.set_yscale('log')

    fig.tight_layout()

    # Set x-axis ticks every month with custom formatting
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_minor_locator(mdates.MonthLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))

    # Rotate the x-axis labels
    for label in ax1.get_xticklabels(which='both'):
        label.set_rotation(45)
        label.set_horizontalalignment('right')
        if label.get_text().isdigit():
            label.set_weight('bold')

    # Consolidate all legends
    lines, labels = ax1.get_legend_handles_labels()
    lines += [line2, line3, line4]
    labels += ['BTCUSD', 'ETHUSD', 'SOLUSD']
    fig.legend(lines, labels, loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

    plt.grid(True)
    plt.title('Normalized Crypto Sentiment Aggregate')
    plt.show()
