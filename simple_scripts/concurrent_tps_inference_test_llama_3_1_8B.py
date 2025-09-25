import os
import time
import openai
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor, as_completed

load_dotenv()
openai.api_key = os.getenv("GENAI_API_TOKEN")
openai.base_url = os.getenv("API_BASE_URL")
model = os.getenv("DEFAULT_MODEL")


def run_inference(user_id: int):
    """Single simulated user request"""
    start = time.time()
    resp = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"[User {user_id}] Explain inference benchmarking in 3 points"}],
        max_tokens=200
    )
    end = time.time()

    output = resp.choices[0].message.content
    tokens = resp.usage.total_tokens
    latency = end - start
    tps = tokens / latency if latency > 0 else 0
    return user_id, latency, tokens, tps


if __name__ == "__main__":
    num_users = 25

    with ThreadPoolExecutor(max_workers=num_users) as executor:
        futures = [executor.submit(run_inference, i) for i in range(num_users)]

        for f in as_completed(futures):
            user_id, latency, tokens, tps = f.result()
            print(f"[User {user_id}] Latency: {latency:.2f}s | Tokens: {tokens} | TPS: {tps:.2f}")
