import numpy as np
from scipy.stats import norm

class BlackScholes:
    @staticmethod
    def calculate_price(S, K, T, r, sigma):
        '''
        Gave five inputs this method calculates the option price with the Black-Scholes model.
        :param S: Stock price
        :param K: Strike price
        :param T: Time to maturity
        :param r: interest rate
        :param sigma: volatility
        :return: Call price and Put price
        '''
        d1 = ((np.log(S / K) + (r + 0.5 * sigma ** 2) * T)
              / (sigma / np.sqrt(T)))
        d2 = d1 - sigma * np.sqrt(T)

        call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

        return call_price, put_price
