# Import necessary libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define your training data
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

# Linear regression model parameters
w = 200
b = 100

# Compute model output
def compute_model_output(x, w, b):
    return w * x + b

# Create a basic Matplotlib chart
fig, ax = plt.subplots()
ax.scatter(x_train, y_train, marker='x', c='r')
ax.plot(x_train, compute_model_output(x_train, w, b), c='b', label='Our Prediction')
ax.set_title("Housing Prices")
ax.set_ylabel('Price (in 1000s of dollars)')
ax.set_xlabel('Size (1000 sqft)')

# Display the plot using Streamlit
st.pyplot(fig)

# Calculate and display predicted price for 1200 sqft
x_i = 1.2
cost_1200sqft = compute_model_output(x_i, w, b)
st.write(f"Predicted price for 1200 sqft: ${cost_1200sqft:.0f} thousand dollars")
