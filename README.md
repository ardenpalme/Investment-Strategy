# Medium-Term Investment Strategy

![License](https://img.shields.io/badge/License-MIT-blue.svg)

## Technical Analysis
Built and back-tested for BTC/USD in TradingView - Highest Sharpe ratio: 1.6. 
The trend is determined by aggregating open-source trend-following indicators.  
Spot positions are entered if the strategy signals long AND market valuation is supportive of positive price performance.
If the strategy signals short, cash or stablecoins are held.

<img src="images/strategy1.png" alt="TradingView Strategy" width="400"/>

## Market Valuation
Determines whether the market environment is supportive of price performance.  
This system aggregates several key on-chain metrics and fundamental indicators that are considered to have a predictive value for Bitcoin's price movements.  
This aggregate score is mean-reverting and signals overbought and oversold conditions.

<img src="images/on_chain1.png" alt="Market Valuation Score" width="400"/>
