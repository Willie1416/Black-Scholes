# utils.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
import math as Math

def calcd1_d2(s, k, t, r, sigma):
    d1 = (Math.log(s/k) + (r + 0.5 * sigma**2) * t) / (sigma * Math.sqrt(t))
    d2 = d1 - sigma * Math.sqrt(t)
    return d1, d2

def calculate_call_price(s, k, d1, d2, r, t):
    return s * norm.cdf(d1) - k * Math.exp(-r*t) * norm.cdf(d2)


def calculate_call_option(S, sigma, K, r, t):
    """Calculate call option price using Black-Scholes formula."""
    d1, d2 = calcd1_d2(S, K, t, r, sigma)

    call_price = S * norm.cdf(d1) - K * np.exp(-r * t) * norm.cdf(d2)
    return call_price


def create_heatmap(s_min, s_max, sigma_min, sigma_max, k, r, t):
    # Use numpy to generate a grid of S and σ values
    # Calculate option prices on the grid
    ...
    data = np.full((10, 10), np.nan)
    spot_prices = np.linspace(s_min, s_max, 10)
    sigmas = np.linspace(sigma_min, sigma_max, 10)

    for i, sig in enumerate(sigmas):
        for j, spot in enumerate(spot_prices):
            d1, d2 = calcd1_d2(spot, k, t, r, sig)
            call_price = calculate_call_price(spot, k, d1, d2, r, t)
            data[i][j] = call_price

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(data, annot=True, fmt=".2f",cmap='viridis',
                xticklabels=np.round(spot_prices, 2),
                yticklabels=np.round(sigmas, 2), ax=ax)
    ax.set_xlabel("Spot Price (S)")
    ax.set_ylabel("Volatility (σ)")
    ax.set_title("Call Option Prices by Spot and Volatility")
    return fig
