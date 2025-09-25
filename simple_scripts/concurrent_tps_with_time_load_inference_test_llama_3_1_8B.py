import os
import time
import random
import statistics
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
import openai


NUM_USERS = 15
DURATION_SEC = 300          # run for 5 min
THINK_TIME_RANGE = (1.0, 2.5)  # per user delay between requests (in seconds)
PROMPT = "Explain inference benchmarking in 3 points"
MAX_TOKENS = 200


load_dotenv()
openai.api_key = os.getenv("GENAI_API_TOKEN")
openai.base_url = os.getenv("API_BASE_URL")
MODEL = os.getenv("DEFAULT_MODEL") or "llama3_1_8b_instruct"

def percentile(values, p):
    if not values:
        return None
    values = sorted(values)
    k = (len(values)-1) * (p/100.0)
    f = int(k)
    c = min(f+1, len(values)-1)
    if f == c:
        return values[f]
    return values[f] + (values[c] - values[f]) * (k - f)

def user_loop(user_id: int, end_time: float):
    """Continuously send requests until end_time; return per-user stats."""
    req_count = 0
    err_count = 0
    total_tokens = 0
    latencies = []

    while time.time() < end_time:
        try:
            start = time.time()
            resp = openai.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": f"[User {user_id}] {PROMPT}"}],
                max_tokens=MAX_TOKENS,
            )
            dur = time.time() - start
            latencies.append(dur)
            # usage can vary across providers; guard with getattr
            usage = getattr(resp, "usage", None)
            if usage and getattr(usage, "total_tokens", None) is not None:
                total_tokens += usage.total_tokens
            req_count += 1
        except Exception as e:
            # optional: print or log per-user errors
            # print(f"[User {user_id}] error: {e}")
            err_count += 1

        # small random think time to avoid thundering herd
        time.sleep(random.uniform(*THINK_TIME_RANGE))

    return {
        "user_id": user_id,
        "requests": req_count,
        "errors": err_count,
        "tokens": total_tokens,
        "latencies": latencies,
    }

def main():
    print(f"Starting load: {NUM_USERS} users for {DURATION_SEC}s on model '{MODEL}'")
    test_start = time.time()
    end_time = test_start + DURATION_SEC

    all_stats = []
    with ThreadPoolExecutor(max_workers=NUM_USERS) as ex:
        futures = [ex.submit(user_loop, i, end_time) for i in range(NUM_USERS)]
        for f in as_completed(futures):
            all_stats.append(f.result())

    # aggregate
    test_end = time.time()
    duration = max(0.001, test_end - test_start)
    total_requests = sum(s["requests"] for s in all_stats)
    total_errors = sum(s["errors"] for s in all_stats)
    total_tokens = sum(s["tokens"] for s in all_stats)
    latencies = [l for s in all_stats for l in s["latencies"]]

    avg_latency = statistics.mean(latencies) if latencies else None
    p50 = percentile(latencies, 50) or 0
    p90 = percentile(latencies, 90) or 0
    p95 = percentile(latencies, 95) or 0
    p99 = percentile(latencies, 99) or 0

    rps = total_requests / duration
    tps = total_tokens / duration if duration > 0 else 0.0

    # Per-user (optional): uncomment to see distribution
    # for s in all_stats:
    #     print(f"User {s['user_id']:>2} -> reqs={s['requests']}, errs={s['errors']}")

    print("\n========== Load Test Summary ==========")
    print(f"Duration:           {duration:.2f}s")
    print(f"Users:              {NUM_USERS}")
    print(f"Total requests:     {total_requests}")
    print(f"Total errors:       {total_errors}")
    print(f"Requests/sec (RPS): {rps:.2f}")
    print(f"Total tokens:       {total_tokens}")
    print(f"Tokens/sec (TPS):   {tps:.2f}")
    if latencies:
        print(f"Avg latency:        {avg_latency:.3f}s")
        print(f"P50 latency:        {p50:.3f}s")
        print(f"P90 latency:        {p90:.3f}s")
        print(f"P95 latency:        {p95:.3f}s")
        print(f"P99 latency:        {p99:.3f}s")
    print("=======================================")

if __name__ == "__main__":
    main()
