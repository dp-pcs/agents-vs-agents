import openai
import os

client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])  # or pass your key directly

response = client.chat.completions.create(
    model="gpt-4.1",  # or "gpt-4-turbo" if you have access
    messages=[{"role": "user", "content": "Hello, world!"}]
)
print(response.choices[0].message.content)