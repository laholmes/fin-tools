# fin-tools  
<a href="https://badge.fury.io/py/fin-tools"><img src="https://badge.fury.io/py/fin-tools.svg" alt="PyPI version" height="18"></a>
[![Twitter](https://img.shields.io/twitter/url/https/pypi.python.org/pypi/fin-tools.svg?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fpypi.python.org%2Fpypi%2Ffin-tools)



Overview
--------
common tools used in finance - risk, pricing, etc

pypi registry - https://pypi.python.org/pypi/fin-tools


Installation
--------

```
pip install fin-tools
```

## Dependencies

fin-tools requires:

numpy==1.12.1 or later   
pandas==0.19.2 or later


## API

### Pricing

#### cds(n, d, p, R, N) -> float
n - number of periods
d - constant discount factor
p - prob default
R - recovery rate
N - notional

returns price of CDS using probability tree model

### Risk 

#### vol(returns) -> float
standard deviation of returns

#### beta(returns, market) -> float
beta of returns

#### var(returns, alpha) -> float
historical var of returns (takes t historical returns, orders them, and takes the loss at the point in the list which corresponds to alpha)

#### cvar(returns, alpha) -> float
conditional var of returns

#### lower_partial_moment(returns, threshold, order) -> float
measures of risk-adjusted return based on vol treat all deviations from the mean as risk, whereas measures of risk-adjusted return based on lower partial moments consider only deviations below some predefined minimum return threshold, t as risk

#### higher_partial_moment(returns, threshold, order) -> float

#### drawdown(returns, tau) -> float
maximum decrease in the value of the portfolio over a specific period of time

#### max_drawdown(returns) -> float

#### average_drawdown(returns, periods) -> float

#### average_drawdown_squared(returns, periods) -> float

#### treynor_ratio(er, returns, market, rf) -> float
excess returns generated by a portfolio, discounted by portfolio beta

#### sharpe_ratio(er, returns, rf) -> float
discounts expected excess returns by vol

#### information_ratio(returns, benchmark) -> float
extension of Sharpe ratio - replaces risk-free rate of return with the scalar expected return of a benchmark portfolio E(rb)

#### modigliani_ratio(er, returns, benchmark, rf) -> float
combination of the Sharpe and information ratios: adjusts the expected excess returns of the portfolio above the risk free rate by the expected excess returns of a benchmark portfolio, above the risk free rate

#### excess_var(er, returns, rf, alpha) -> float
excess return on value at risk discounts the excess return of the portfolio above the risk-free rate by the value at risk of the portfolio

#### conditional_sharpe_ratio(er, returns, rf, alpha) -> float
discounts the excess return of the portfolio above the risk-free rate by the conditional VaR of the portfolio

#### omega_ratio(er, returns, rf, target=0) -> float
discounts the excess returns of a portfolio above the target threshold
(usually risk-free rate), by the first-order lower partial moment of the returns. first-order lower partial moment corresponds to the average expeceted loss aka downside risk

#### sortino_ratio(er, returns, rf, target=0) -> float
modification of sharpe - only uses downside vol (delta)

#### kappa_three_ratio(er, returns, rf, target=0) -> float
generalization of omega and sortino ratios
if j = 1, kappa is omega, j = 2, kappa is sortino

#### gain_loss_ratio(returns, target=0) -> float
discounts first order higher partial moment of a portfolio's returns, upside potential, by the first-order lower partial moment of a portfolio's returns, downside risk

#### upside_potential_ratio(returns, target=0) -> float
discounts first order higher partial moment of a portfolio's returns, upside potential, by the second-order lower partial moment of a portfolio's returns, downside variation

#### calmar_ratio(er, returns, rf) -> float
discounts expected excess return of a portfolio by the worst expected maximum draw down for that portfolio

#### sterling_ratio(er, returns, rf, periods) -> float
discounts the expected excess return of a portfolio by the average of the N worst expected maximum drawdowns for that portfolio

#### burke_ratio(er, returns, rf, periods) -> float
similar to sterling, but less sensitive to outliers discounts the expected excess return of a portfolio by the square root of the average of the N worst expected maximum drawdowns for that portfolio
