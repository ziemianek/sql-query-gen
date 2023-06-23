from . import credentials
from . import measure_time
import openai

openai.api_key = credentials.API_KEY


@measure_time.measure_time
def generate_sql_query(prompt: str, model: str = "gpt-3.5-turbo", role: str = "user") -> str:
    """Function uses OpenAI's api to generate sql queries from the provided prompt"""
    try:
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[
                {
                    "role": role, 
                    "content": f"Generate a SQL query from the following prompt: {prompt}. Only respond with code as plain text without code block syntax around it. "
                }
            ]
        )
        response = completion.choices[0].message.content.strip()
    except Exception as e:
        response = f"Something went wrong: {e}"
    return response
