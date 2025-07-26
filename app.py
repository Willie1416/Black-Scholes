# app.py
import streamlit as st
from utils import create_heatmap, calculate_call_option, calculate_put_option

st.set_page_config(page_title="Call & Put Option Heatmap", layout="wide")

st.title("Call & Put Option Heatmap Visualizer")

st.sidebar.header("Variabels")
# Strike, Rate, and Time remain single values
s = st.sidebar.number_input("Spot Price (S)", value=100.0, step=1.0)
k = st.sidebar.number_input("Strike Price (K)", value=105.0, step=1.0)
sigma = st.sidebar.number_input("Volatility (σ)", value=0.33, step=0.01)
r = st.sidebar.number_input("Risk-Free Rate (r)", value=0.05, step=0.001, format="%.3f")
t = st.sidebar.number_input("Time to Maturity (t)", value=1.0, step=0.1)

st.sidebar.divider()
# Spot Price range
st.sidebar.subheader("Spot Price (S) Range")
s_min = st.sidebar.number_input("Min Spot Price", value=80.0, step=1.0, key="s_min")
s_max = st.sidebar.number_input("Max Spot Price", value=120.0, step=1.0, key="s_max")

# Volatility range
st.sidebar.subheader("Volatility (σ) Range")
sigma_min = st.sidebar.number_input("Min Volatility", value=0.1, step=0.01, key="sigma_min")
sigma_max = st.sidebar.number_input("Max Volatility", value=0.5, step=0.01, key="sigma_max")

call_value = calculate_call_option(s, sigma, k, r, t)
put_value = calculate_put_option(s, sigma, k, r, t)


# Create two side-by-side columns
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div style="background-color: #28a745; padding: 10px; border-radius: 5px; text-align: center; color: white; font-size: 20px;">
            📈 Call Option Value: <strong>{call_value:.2f}</strong>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="background-color: #dc3545; padding: 10px; border-radius: 5px; text-align: center; color: white; font-size: 20px;">
            📉 Put Option Value: <strong>{put_value:.2f}</strong>
        </div>
        """, 
        unsafe_allow_html=True
    )

# Display plot
call_fig, put_fig = create_heatmap(s_min, s_max, sigma_min, sigma_max, k, r, t)

# Display them side by side using columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Call Option Heatmap")
    st.pyplot(call_fig, use_container_width=True)

with col2:
    st.subheader("📉 Put Option Heatmap")
    st.pyplot(put_fig, use_container_width=True)
