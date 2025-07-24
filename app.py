# app.py
import streamlit as st
from utils import create_heatmap

st.set_page_config(page_title="Call Option Heatmap", layout="centered")

st.title("📈 Call Option Heatmap Visualizer")

# Sidebar sliders
s = st.sidebar.number_input("Spot Price (S)", value=100.0, step=1.0)
sigma = st.sidebar.number_input("Volatility (σ)", value=0.33, step=0.01)
k = st.sidebar.number_input("Strike Price (K)", value=105.0, step=1.0)
r = st.sidebar.number_input("Risk-Free Rate (r)", value=0.05, step=0.001, format="%.3f")
t = st.sidebar.number_input("Time to Maturity (t)", value=1.0, step=0.1)

# Display plot
fig = create_heatmap(s, sigma, k, r, t)
st.pyplot(fig)
