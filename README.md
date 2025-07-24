# 📈 Call Option Heatmap Visualizer

A simple and interactive web application built with [Streamlit](https://streamlit.io/) that visualizes the value of European call options over a range of spot prices and volatilities using a heatmap. The app also displays the calculated call option value for a fixed set of parameters with a clear interface.

---

## 🚀 Features

- 🎛 Adjustable inputs for:
  - Strike Price (K)
  - Risk-Free Rate (r)
  - Time to Maturity (t)
  - Spot Price range (S<sub>min</sub> to S<sub>max</sub>)
  - Volatility range (σ<sub>min</sub> to σ<sub>max</sub>)
- ✅ Highlighted call option value for a **fixed** spot price and volatility
- 💡 Simple UI with live updates as parameters change

---

## 📷 Screenshot

![heatmap-demo](screenshot.png)  
> Example heatmap showing option values over spot price and volatility

---

## 🧠 How it Works

The application uses the **Black-Scholes** model to calculate the price of a European call option:

\[
C = S \cdot N(d_1) - K \cdot e^{-rt} \cdot N(d_2)
\]

where:

- \( d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)t}{\sigma \sqrt{t}} \)
- \( d_2 = d_1 - \sigma \sqrt{t} \)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** for the interactive web UI
- **Matplotlib** for plotting the heatmap
- **SciPy** for the normal distribution (`scipy.stats.norm`)

---

