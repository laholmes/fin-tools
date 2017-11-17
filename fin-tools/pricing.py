from typing import List
import numpy as np

def cds(num_periods: int, 
        discount_factor: float, 
        default_probability: float, 
        recovery_rate: float, 
        notional: float, 
        coupon_frequency: float, 
        issue_premium: float) -> float:
    
    no_default = np.power(default_probability, num_periods) * discount_factor * notional
    
    return np.sum([
        np.power(1-default_probability, period) * 
        default_probability * 
        (notional * (1 - recovery_rate) * discount_factor - (notional*issue_premium*period)/coupon_frequency)
        for period in range(num_periods)
    ]) - no_default


def cds_variable(num_periods: int, 
        discount_factors: list, 
        default_probabilities: list, 
        recovery_rate: float, 
        notional: float, 
        coupon_frequency: float, 
        issue_premium: float) -> float:

    no_default = np.prod(default_probabilities) * np.sum(discount_factors) *  (issue_premium * notional)/ coupon_frequency
    return np.sum([
        np.power(1-default_probabilities[period], period) * 
        default_probabilities[period] * 
        (notional * (1 - recovery_rate) * discount_factors[period] - (notional*issue_premium * np.sum(discount_factors[0:period]))/coupon_frequency)
        for period in range(num_periods)
    ]) - no_default

fixed = cds(4, 1/1.1, 0.1, 0.75, 1000, 4, 10)
variable = cds_variable(4, [1/1.1, 1/1.11, 1/1.12, 1/1.13], [0.1, 0.05, 0.025, 0.0125], 0.75, 1000, 4, 10)
print(f'fixed: {fixed}')
print(f'variable: {variable}')
