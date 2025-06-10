import streamlit as st
from datetime import datetime
import pytz

# Page config
st.set_page_config(page_title="BenchAmigo 🧪", page_icon="🧪")

# Title and welcome message
st.title("👋 Welcome to BenchAmigo!")
st.markdown("Your personal lab assistant for quick chemistry calculations.")

# Time-based greeting
name = st.text_input("What's your name?")
role = st.text_input("What's your role in the lab?")
timezone = st.selectbox("🌐 Select your timezone", pytz.all_timezones, index=pytz.all_timezones.index('Asia/Kolkata'))

if name:
    now = datetime.now(pytz.timezone(timezone))
    hour = now.hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    st.success(f"{greeting}, {name}! Welcome to BenchAmigo.")

# Tool selector
st.header("🔧 Choose a Calculator")
tool = st.selectbox("Pick a tool", ["Select", "Density Calculator", "Dilution Calculator"])

# Density Calculator
if tool == "Density Calculator":
    st.subheader("🧪 Density Calculator (g/mL)")
    mass = st.number_input("Enter mass (g)", min_value=0.0, step=0.1)
    volume = st.number_input("Enter volume (mL)", min_value=0.0, step=0.1)
    
    if st.button("Calculate Density"):
        if volume == 0:
            st.error("Volume cannot be zero!")
        else:
            density = mass / volume
            st.success(f"Density: {density:.3f} g/mL")

# Dilution Calculator
elif tool == "Dilution Calculator":
    st.subheader("💧 Dilution Calculator (C1V1 = C2V2)")
    C1 = st.number_input("Stock concentration (C1)", min_value=0.0, step=0.1)
    C2 = st.number_input("Desired concentration (C2)", min_value=0.0, step=0.1)
    V2 = st.number_input("Final volume needed (V2 in mL)", min_value=0.0, step=0.1)

    if st.button("Calculate Volume of Stock (V1)"):
        if C1 == 0:
            st.error("Stock concentration (C1) cannot be zero.")
        else:
            V1 = (C2 * V2) / C1
            st.success(f"Required volume of stock (V1): {V1:.3f} mL")
