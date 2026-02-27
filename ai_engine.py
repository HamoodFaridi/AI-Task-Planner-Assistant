import ollama

def generate_plan(prompt: str, model_name: str):
    """
    Streams response from Ollama model.
    Yields chunks of text progressively.
    """
    # response = ollama.chat(
    stream = ollama.chat(
        model = model_name, #"phi3:mini",  "llama3"
        messages = [{"role": "user", "content": prompt}],
        stream = True,
        options = {
            "temperature": 0.2,
            "num_predict": 400
            }
    )
    # return response["message"]["content"]
    for chunk in stream:
        yield chunk["message"]["content"]