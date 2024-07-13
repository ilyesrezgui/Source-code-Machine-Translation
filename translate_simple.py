import openai
import os

def translate_my_code(input_code, selected_source, selected_target):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model_engine = "text-davinci-003"
    max_tokens = 2048
    prompt = f"Translate from {selected_source} to {selected_target}: \n\n{input_code}"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    translated_code = response.choices[0].text.strip()
    return translated_code

