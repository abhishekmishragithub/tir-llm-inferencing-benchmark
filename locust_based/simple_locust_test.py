from locust import HttpUser, task, between
import os
import json
import random

API_KEY = os.getenv("GENAI_API_TOKEN", "")
API_BASE_URL = os.getenv("API_BASE_URL")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")

class LLMUser(HttpUser):
    host = API_BASE_URL
    wait_time = between(0.5, 2.0)  # user think time between requests

    @task
    def infer(self):
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": DEFAULT_MODEL,
            "messages": [
                {"role": "user", "content": f"Generate a short poem about number {random.randint(1,100)}"}
            ],
            "max_tokens": 64,
            "temperature": 0.7,
            "stream": False,
        }
        self.client.post(
            f"{API_BASE_URL}/chat/completions",
            headers=headers,
            data=json.dumps(payload),
            name="/chat/completions"
        )
