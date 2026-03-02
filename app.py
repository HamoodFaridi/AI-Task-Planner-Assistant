# This is the UI layer 
import streamlit as st
from planner import create_daily_plan
import time

st.set_page_config(page_title = "AI Local Task Planner", layout = "centered")

# ------------------------
# Dark Mode Toggle
# ------------------------

dark_mode = st.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown(
        """
        <style>
        body { background-color: #0e1117; color: white; }
        </style>
        """,
        unsafe_allow_html = True
    )

st.title("🧠 Local AI Daily Planner")

# ------------------------
# Session State Setup
# ------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "stop_generation" not in st.session_state:
    st.session_state.stop_generation = False

# ------------------------
# Model Selector
# ------------------------
model_name = st.selectbox(
    "Choose Model",
    ["phi3:mini", "llama3", "mistral:7b-instruct"]
)

# ------------------------
# Tabs: Planner + Chat History
# ------------------------

tab1, tab2 = st.tabs(["📋 Planner", "💬 History"])

# ========================
# TAB 1 – STRUCTURED PLANNER
# ========================

with tab1:
    tasks = st.text_area(
        "Enter your tasks for today:",
        height = 150,
        placeholder = "Example: Gym 1h, Study 2h, Coding 3h..."
    ) 

    col1, col2 = st.columns(2)

    generate_clicked = col1.button("Generate Plan")
    stop_clicked = col2.button("Stop")

    if stop_clicked:
        st.session_state.stop_generation = True

    # ------------------------
    # Generate Button
    # ------------------------


    if generate_clicked and tasks:
        
        st.session_state.stop_generation = False

        with st.spinner("Generating Plan..."):
            start = time.time()
            response_stream = create_daily_plan(tasks, model_name)
            output_placeholder = st.empty()
            full_response = ""

            # ------------------------
            # Streaming Effect
            # ------------------------
            for chunk in response_stream:
                if st.session_state.stop_generation:
                    break
                
                full_response += chunk
                output_placeholder.markdown(
                    f"""
                    ### 🗂 Structured Plan

                    {full_response}
                    """
                    )
            end = time.time()
        # st.write(result)
        st.caption(f"Generated in {round(end - start, 2)} seconds")

        # Save to session history
        st.session_state.history.append(
            {
                "tasks": tasks,
                "response": full_response,
                "model": model_name,
                "time": round(end - start, 2),
            }
        )

# ========================
# TAB 2 – HISTORY
# ========================
        
with tab2:
    st.subheader("Session History")
    if not st.session_state.history:
        st.info("No plans generated yet.")
    
    for idx, entry in enumerate(reversed(st.session_state.history), 1):
        with st.expander(f"Plan #{idx} | Model: {entry['model']} | {entry['time']}s"):
            st.markdown("**Tasks:")
            st.write(entry["tasks"])

            st.markdown("**Generated Plan**:")
            st.write(entry["response"])