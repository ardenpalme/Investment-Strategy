# Medium-Term Investment Strategy

![License](https://img.shields.io/badge/License-MIT-blue.svg)

## Technical Analysis
Trend-following strategy built and backtested in TradingView.  
The trend is determined by aggregating open-source trend-following indicators.  
Spot positions are entered if the strategy signals long AND market valuation is supportive of positive price performance.  
If the strategy signals short, cash or stablecoins are held.  

<p align="center">
  <img src="images/strategy1.png" alt="TradingView Strategy" width="600"/>
</p>

## Market Valuation
Determines whether the market environment is supportive of price performance.  
This system aggregates several key on-chain metrics, fundamental indicators, and sentiment indicators that are considered to have a predictive value for Bitcoin's price movements.  
This aggregate score is mean-reverting and signals overbought and oversold conditions.  

The Sentiment indicator queries CoinAPI for market data and GoogleTrends for the amount of google searches for a set of cryptocurrency terms. The search frequency of cryptocurrency terms can be indicative of retail sentiment. Below is a screenshot of an early version of this indicator.

<p align="center">
  <img src="images/on_chain1.png" alt="Market Valuation Score" width="400"/>
  <img src="images/sentiment1.png" alt="Market Valuation Score" width="400"/>
</p>
