from ai_engine import generate_plan

def create_daily_plan(tasks: str, model_name: str):
    """
    Builds structured prompt and streams AI output.
    """
    prompt = f"""
    You are a productivity expert.
    Organize and prioritize these tasks.
    Provide:
    1. Ordered priority list
    2. Suggested time blocks
    3. Quick productivity advice

    Rules:
    - Total hours must equal the sum of time blocks.
    - Double-check calculations.
    - Do not contradict yourself.
    - Show total hours clearly.

    Tasks:
    {tasks}
    """

    return generate_plan(prompt, model_name)