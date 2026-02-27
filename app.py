# This is the UI layer 
import streamlit as st
from planner import create_daily_plan
import time

st.set_page_config(page_title = "AI Local Task Planner", layout = "centered")

st.title("🧠 Local AI Daily Planner")

# tasks = st.text_area("Enter your tasks (one per line)")

# ------------------------
# Model Selector (NEW)
# ------------------------
model_name = st.selectbox(
    "Choose Model",
    ["phi3:mini", "llama3", "mistral"]
)

# ------------------------
# Task Input
# ------------------------

tasks = st.text_area(
    "Enter your tasks for today:",
    height = 150,
    placeholder = "Example: Gym 1h, Study 2h, Coding 3h..."
)

# ------------------------
# Generate Button
# ------------------------


if st.button("Generate Plan") and tasks:
        with st.spinner("Generating Plan..."):
            start = time.time()
            response_stream = create_daily_plan(tasks, model_name)
            output_placeholder = st.empty()
            full_response = ""

            # ------------------------
            # Streaming Effect (NEW)
            # ------------------------
            for chunk in response_stream:
                full_response += chunk
                output_placeholder.markdown(full_response)
            end = time.time()
        # st.write(result)
        st.caption(f"Generated in {round(end - start, 2)} seconds")