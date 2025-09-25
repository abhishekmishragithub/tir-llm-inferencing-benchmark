from locust import HttpUser, task, between, events
import os
# import json
import time
import requests

API_KEY = os.getenv("GENAI_API_TOKEN", "")
API_BASE_URL = os.getenv("API_BASE_URL", "").rstrip("/")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "llama3_1_8b_instruct")
PROVIDER = os.getenv("PROVIDER_NAME", "provider")

HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


class LLMUser(HttpUser):
    host = API_BASE_URL
    wait_time = between(0.3, 1.2)

    def _path(self, p: str) -> str:
        return p if p.startswith("/") else f"/{p}"

    def _fire_tps(self, resp_json, elapsed_ms, label):
        usage = resp_json.get("usage", {})
        total_tokens = usage.get("total_tokens", 0)
        tps = total_tokens / (elapsed_ms / 1000) if total_tokens else 0
        events.request.fire(
            request_type="LLM",
            name=f"[{PROVIDER}] {label} TPS",
            response_time=elapsed_ms,
            response_length=total_tokens,
            context={"tps": tps},
        )

    # latency focus
    @task(4)
    def small_prompt(self):
        payload = {
            "model": DEFAULT_MODEL,
            "messages": [{"role": "user", "content": "Return a one-word answer: ok"}],
            "max_tokens": 16,
            "temperature": 0.2,
            "stream": False,
        }
        t0 = time.perf_counter()
        resp = self.client.post(self._path("chat/completions"), headers=HEADERS,
                                json=payload, name=f"[{PROVIDER}] /chat (small)")
        try:
            data = resp.json()
            elapsed = (time.perf_counter() - t0) * 1000
            self._fire_tps(data, elapsed, "small")
        except Exception:
            pass

    # Medium prompt
    @task(3)
    def medium_prompt(self):
        payload = {
            "model": DEFAULT_MODEL,
            "messages": [{"role": "user", "content": "Explain HTTP/2 in two sentences."}],
            "max_tokens": 64,
            "temperature": 0.2,
            "stream": False,
        }
        t0 = time.perf_counter()
        resp = self.client.post(self._path("chat/completions"), headers=HEADERS,
                                json=payload, name=f"[{PROVIDER}] /chat (medium)")
        try:
            data = resp.json()
            elapsed = (time.perf_counter() - t0) * 1000
            self._fire_tps(data, elapsed, "medium")
        except Exception:
            pass


    @task(2)
    def long_prompt(self):
        lipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 400
        prompt = lipsum + "\nSummarize the above in one sentence."
        payload = {
            "model": DEFAULT_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 64,
            "temperature": 0.2,
            "stream": False,
        }
        t0 = time.perf_counter()
        resp = self.client.post(self._path("chat/completions"), headers=HEADERS,
                                json=payload, name=f"[{PROVIDER}] /chat (long)")
        try:
            data = resp.json()
            elapsed = (time.perf_counter() - t0) * 1000
            self._fire_tps(data, elapsed, "long")
        except Exception:
            pass


    @task(3)
    def streaming_ttft_and_ttl(self):
        url = f"{API_BASE_URL}/chat/completions"
        payload = {
            "model": DEFAULT_MODEL,
            "messages": [{"role": "user", "content": "List prime numbers from 2 to 29, separated by commas."}],
            "max_tokens": 64,
            "temperature": 0.2,
            "stream": True,
        }
        t0 = time.perf_counter()
        ttft_ms = None
        inter_times = []
        last = None
        try:
            with requests.post(url, headers=HEADERS, json=payload, stream=True, timeout=60) as r:
                for line in r.iter_lines(decode_unicode=True):
                    if not line:
                        continue
                    if isinstance(line, bytes):
                        line = line.decode("utf-8", errors="ignore")
                    if not line.startswith("data:"):
                        continue
                    if line.strip() == "data: [DONE]":
                        break
                    now = time.perf_counter()
                    if ttft_ms is None:
                        ttft_ms = (now - t0) * 1000
                        events.request.fire(request_type="LLM", name=f"[{PROVIDER}] TTFT",
                                            response_time=ttft_ms, response_length=0)
                    if last:
                        inter_times.append((now - last) * 1000)
                    last = now

                ttl_ms = (time.perf_counter() - t0) * 1000
                events.request.fire(request_type="LLM", name=f"[{PROVIDER}] TTLT",
                                    response_time=ttl_ms, response_length=0)
                if inter_times:
                    avg_cadence = sum(inter_times) / len(inter_times)
                    events.request.fire(request_type="LLM", name=f"[{PROVIDER}] cadence",
                                        response_time=avg_cadence, response_length=0)
        except Exception as e:
            events.request.fire(request_type="LLM", name=f"[{PROVIDER}] stream error",
                                response_time=0, response_length=0, exception=e)

    # Invalid params (negative max_tokens)
    @task(1)
    def invalid_params(self):
        payload = {"model": DEFAULT_MODEL, "messages": [{"role": "user", "content": "hello"}],
                   "max_tokens": -1, "stream": False}
        self.client.post(self._path("chat/completions"), headers=HEADERS,
                         json=payload, name=f"[{PROVIDER}] /chat (invalid)")

    # controlled: long response (TPS focus)
    @task(2)
    def fixed_long(self):
        payload = {
            "model": DEFAULT_MODEL,
            "messages": [{"role": "user", "content": "Write a 300-word essay about AI benchmarking."}],
            "max_tokens": 500,
            "stream": False,
        }
        t0 = time.perf_counter()
        resp = self.client.post(self._path("chat/completions"), headers=HEADERS,
                                json=payload, name=f"[{PROVIDER}] fixed_long")
        try:
            data = resp.json()
            elapsed = (time.perf_counter() - t0) * 1000
            self._fire_tps(data, elapsed, "fixed_long")
        except Exception:
            pass

    # uncontrolled: no max_tokens (realistic)
    @task(1)
    def uncontrolled(self):
        payload = {
            "model": DEFAULT_MODEL,
            "messages": [{"role": "user", "content": "Explain inference benchmarking in detail"}],
            "stream": False,  # no max_tokens
        }
        t0 = time.perf_counter()
        resp = self.client.post(self._path("chat/completions"), headers=HEADERS,
                                json=payload, name=f"[{PROVIDER}] uncontrolled")
        try:
            data = resp.json()
            elapsed = (time.perf_counter() - t0) * 1000
            self._fire_tps(data, elapsed, "uncontrolled")
        except Exception:
            pass

# run - locust -f locust_test.py --headless -u 200 -r 20 -t 5m --csv results/e2e_test --html results/e2e_report.html
# -u  concurrent “users”
# -r spawn new users/sec (ramp up)

# locust -f locust/locustfile.py ---> Open http://localhost:8089
