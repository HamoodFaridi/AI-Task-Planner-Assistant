from ai_engine import ask_ai

def create_daily_plan(tasks):
    prompt = f"""
    You are a productivity expert.
    Organize and prioritize these tasks.
    Provide:
    1. Ordered priority list
    2. Suggested time blocks
    3. Quick productivity advice

    Tasks:
    {tasks}
    """

    return ask_ai(prompt)