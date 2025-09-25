import time
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("GENAI_API_TOKEN")
openai.base_url = os.getenv("API_BASE_URL")
model = os.getenv("DEFAULT_MODEL") or "llama3_1_8b_instruct"

for times in range(10):
    start = time.time()
    resp = openai.chat.completions.create(
        model=model,
        messages=[{"role":"user","content":"Explain inference benchmarking in 3 points"}],
        max_tokens=200
    )
    end = time.time()

    output = resp.choices[0].message.content
    tokens = resp.usage.total_tokens
    print(f"Latency: {end-start:.2f}s, Tokens: {tokens}, TPS: {tokens/(end-start):.2f}")
    time.sleep(3)

# print("Output:", output)
# import ipdb
#
# ipdb.set_trace()
