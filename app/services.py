from openai import OpenAI
from config import Config

class OpenAIService:
    def __init__(self):
        self.api_key = Config.OPENAI_API_KEY
        self.client = OpenAI(
        api_key = self.api_key
    )

    def get_answer_from_openai(self, question):
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="gpt-3.5-turbo",
            max_tokens=50,
        )
        return response.choices[0].message.content