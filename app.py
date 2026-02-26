# This is the UI layer 
import streamlit as st
from planner import create_daily_plan

st.title("🧠 Local AI Daily Planner")

tasks = st.text_area("Enter your tasks (one per line)")

if st.button("Generate Plan"):
    if tasks.strip() == "":
        st.warning("Please enter some tasks.")
    else:
        with st.spinner("Generating Plan..."):
            result = create_daily_plan(tasks)
            st.write(result)