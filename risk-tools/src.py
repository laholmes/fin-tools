import numpy as np
import numpy.random as nrand


def vol(returns) -> float:
    return np.std(returns)


def beta(returns, market) -> float:
    m = np.matrix([returns, market])
    return np.cov(m)[0][1] / np.std(market)


def var(returns, alpha):
    sorted_returns = np.sort(returns)
    index = int(alpha * len(sorted_returns))
    return abs(sorted_returns[index])

def cvar(returns, alpha):
    sorted_returns = np.sort(returns)
    index = int(alpha * len(sorted_returns))
    sum_var = sorted_returns[0]
    for i in range(1, index):
        sum_var += sorted_returns[i]

    return abs(sum_var / index)


def lower_partial_moment(returns, threshold, order):
    threshold_array = numpy.empty(len(returns))
    threshold_array.fill(threshold)

    diff = threshold_array - returns
    diff = diff.clip(min=0)

    return np.sum(diff ** order) / len(returns)


def higher_partial_moment(returns, threshold, order):
    threshold_array = np.empty(len(returns))
    threshold_array.fill(threshold)
    diff = returns - threshold_array
    diff = diff.clip(min=0)
    return np.sum(diff ** order) / len(returns)


def drawdown(returns, tau):
    values = prices(returns, 100)
    pos = len(values) - 1
    pre = pos - tau
    drawdown = float('+inf')

    while pre >= 0:
        dd_i = (values[pos] / values[pre]) - 1
        if dd_i < drawdown:
            drawdown = dd_i

        pos, pre = pos - 1, pre - 1

    return abs(drawdown)

def max_drawdown(returns):
    max_drawdown = float('-inf')
    for i in range(0, len(returns)):
        drawdown_i = dd(returns, i)
        if drawdown_i > max_drawdown:
            max_drawdown = drawdown_i

    return abs(max_drawdown)


def average_drawdown(returns, periods):
    for i in range(0, len(returns)):
        drawdown_i = dd(returns, i)
        drawdowns.append(drawdown_i)
    drawdowns = sorted(drawdowns)
    total_dd = abs(drawdowns[0])
    
    for i in range(1, periods):
        total_dd += abs(drawdowns[i])
    
    return total_dd / periods


def average_drawdown_squared(returns, periods):
    drawdowns = []
    for i in range(0, len(returns)):
        drawdown_i = math.pow(dd(returns, i), 2.0)
        drawdowns.append(drawdown_i)
    drawdowns = sorted(drawdowns)
    total_dd = abs(drawdowns[0])

    for i in range(1, periods):
        total_dd += abs(drawdowns[i])
    return total_dd / periods


def treynor_ratio(er, returns, market, rf):
    return (er - ef) / beta(returns, market)


def sharpe_ratio(er, returns, rf):
    return (er - ef) / vol(returns)


def information_ratio(returns, benchmark):
    diff = returns - benchmark
    return np.mean(diff) / vol(diff)


def modigliani_ratio(er, returns, benchmark, rf):
    np_rf = np.empty(len(returns))
    np_rf.fill(rf)
    rdiff = returns - np_rf
    bdiff = benchmark - np_rf
    return (er - rf) * (vol(rdiff) / vol(bdiff)) + rf


def excess_var(er, returns, rf, alpha):
    return (er - rf) / var(returns, alpha)


def conditional_sharpe_ratio(er, returns, rf, alpha):
    return (er - rf) / cvar(returns, alpha)


def omega_ratio(er, returns, rf, target=0):
    return (er - rf) / lower_partial_moment(returns, target, 1)


def sortino_ratio(er, returns, rf, target=0):
    return (er -rf) / math.sqrt(lower_partial_moment(returns, target, 2))


def kappa_three_ratio(er, returns, rf, target=0):
    return (er - rf) / math.pow(lower_partial_moment(returns, target, 3), float(1/3))


def gain_loss_ratio(returns, target=0):
    return higher_partial_moment(returns, target, 1) / lpm(returns, target, 1)


def upside_potential_ratio(returns, target=0):
    return higher_partial_moment(returns, target, 1) / math.sqrt(lpm(returns, target, 2))


def calmar_ratio(er, returns, rf):
    return (er-rf) / max_drwadown(returns)


def sterling_ratio(er, returns, rf, periods):
    return (er - ef) / average_drawdown(returns, periods)


def burke_ratio(er, returns, rf, periods)
    return (er - ef) / math.sqrt(average_drawdown_squared(returns, periods))