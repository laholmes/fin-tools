from typing import List
import numpy as np

class cds():
    def __init__(self, num_periods: int, 
        discount_factors: float, 
        default_probabilities: float, 
        recovery_rate: float, 
        notional: float, 
        coupon_frequency: float, 
        issue_premium: float):
        self.num_periods = num_periods
        self.discount_factors = discount_factors
        self.default_probabilities = default_probabilities
        self.recovery_rate = recovery_rate
        self.notional = notional
        self.coupon_frequency = coupon_frequency
        self.issue_premium = issue_premium

    def get_price(self):
        def get_dynamic_price() -> float:
            no_default = np.prod([1 - prob for prob in self.default_probabilities]) * np.sum(self.discount_factors) * \
                (self.issue_premium * self.notional)/ self.coupon_frequency

            return np.sum([
                np.power(1-self.default_probabilities[period], period) * 
                self.default_probabilities[period] * 
                (self.notional * (1 - self.recovery_rate) * self.discount_factors[period] - (self.notional * self.issue_premium * np.sum(self.discount_factors[0:period]))/self.coupon_frequency)
                for period in range(self.num_periods)
            ]) - no_default

        def get_fixed_price() -> float:
            no_default = np.power(1-self.default_probabilities[0], self.num_periods) * \
                self.num_periods * self.discount_factors[0] * (self.notional * self.issue_premium)/self.coupon_frequency

            return np.sum([
                np.power(1-self.default_probabilities[0], period) * 
                self.default_probabilities[0] * 
                (self.notional * (1 - self.recovery_rate) * self.discount_factors [0]- (self.notional * self.issue_premium * period)/self.coupon_frequency)
                for period in range(self.num_periods)
            ]) - no_default

        
        if len(self.discount_factors) == 1:
            return get_fixed_price()
        else: 
            return get_dynamic_price()