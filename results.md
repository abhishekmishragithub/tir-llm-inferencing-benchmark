# TIR GenAI API Inference Benchmarking


## First Try, 10 runs (Sequential):

### e2e:
Prompt: "Explain inference benchmarking in 3 points"
  - TPS -  51.90, 47.36, 50.90, 52.47, 52.30, 50.41, 51.80, 52.89, 51.51, 49.33 (avg: 51.087)
  - Tokens - 244 (constant)
  - Latency: 5.15s, 4.79s, 4.65s, 4.67s, 4.84s, 4.70s, 4.71s, 4.61s, 4.74s, 4.95s, 4.66s (avg: 4.77s)

### nebius:
Prompt: "Explain inference benchmarking in 3 points"
  - TPS -  46.71, 62.32, 62.48,  62.67, 60.06, 58.47, 61.49, 60.29, 68.82, 65.90 (avg: 	56.921)
  - Tokens - 219 (constant)
  - Latency: 4.69s, 3.51s, 3.51s, 3.49s, 3.65s, 3.75s, 3.56s, 3.63s, 3.18s, 3.32s (avg: 3.62s)
---

## Second Try, 15 users concurrently:
### e2e:
Prompt: "Explain inference benchmarking in 3 points"
  - TPS - 32.04, 32.03, 32.03, 32.03, 31.43, 31.43, 31.42, 31.42, 31.42, 31.42, 31.42, 31.41, 31.41, 31.41, 31.41, 31.40, 31.40, 31.39, 31.39, 31.39, 31.22, 31.19, 31.19, 31.19, 31.17 (avg: 31.47)
  - Tokens - 248 (constant)
  - Latency: 7.74s, 7.74s, 7.74s, 7.74s, 7.89s, 7.89s, 7.89s, 7.89s, 7.89s, 7.89s, 7.89s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.94s, 7.95s, 7.95s, 7.95s, 7.96s (avg: 7.89s)
raw output:
```bash
[User 9] Latency: 7.74s | Tokens: 248 | TPS: 32.04
[User 5] Latency: 7.74s | Tokens: 248 | TPS: 32.03
[User 16] Latency: 7.74s | Tokens: 248 | TPS: 32.03
[User 11] Latency: 7.74s | Tokens: 248 | TPS: 32.03
[User 2] Latency: 7.89s | Tokens: 248 | TPS: 31.43
[User 22] Latency: 7.89s | Tokens: 248 | TPS: 31.43
[User 3] Latency: 7.89s | Tokens: 248 | TPS: 31.42
[User 0] Latency: 7.89s | Tokens: 248 | TPS: 31.42
[User 7] Latency: 7.89s | Tokens: 248 | TPS: 31.42
[User 18] Latency: 7.89s | Tokens: 248 | TPS: 31.42
[User 19] Latency: 7.89s | Tokens: 248 | TPS: 31.42
[User 4] Latency: 7.90s | Tokens: 248 | TPS: 31.41
[User 14] Latency: 7.90s | Tokens: 248 | TPS: 31.41
[User 15] Latency: 7.90s | Tokens: 248 | TPS: 31.41
[User 20] Latency: 7.90s | Tokens: 248 | TPS: 31.41
[User 12] Latency: 7.90s | Tokens: 248 | TPS: 31.40
[User 17] Latency: 7.90s | Tokens: 248 | TPS: 31.40
[User 8] Latency: 7.90s | Tokens: 248 | TPS: 31.39
[User 1] Latency: 7.90s | Tokens: 248 | TPS: 31.39
[User 23] Latency: 7.90s | Tokens: 248 | TPS: 31.39
[User 21] Latency: 7.94s | Tokens: 248 | TPS: 31.22
[User 13] Latency: 7.95s | Tokens: 248 | TPS: 31.19
[User 10] Latency: 7.95s | Tokens: 248 | TPS: 31.19
[User 24] Latency: 7.95s | Tokens: 248 | TPS: 31.19
[User 6] Latency: 7.96s | Tokens: 248 | TPS: 31.17
```

### nebius:
Prompt: "Explain inference benchmarking in 3 points"
  - TPS - 33.33, 34.45, 34.44, 34.32, 34.31, 34.29, 34.21, 34.21, 34.20, 34.19, 34.20, 34.16, 34.15, 34.15, 34.13, 34.14, 34.13, 34.13, 34.10, 33.92, 33.84, 31.88, 29.69, 29.68, 28.80 (avg: 33.44)
  - Tokens - 210, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223 (avg: 222.48)
  - Latency - 6.30s, 6.47s, 6.47s, 6.50s, 6.50s, 6.50s, 6.52s, 6.52s, 6.52s, 6.52s, 6.52s, 6.53s, 6.53s, 6.53s, 6.53s, 6.53s, 6.53s, 6.53s, 6.54s, 6.57s, 6.59s, 7.00s, 7.51s, 7.51s, 7.74s (avg: 6.69s)
raw output:
```bash
User 11] Latency: 6.30s | Tokens: 210 | TPS: 33.33
[User 22] Latency: 6.47s | Tokens: 223 | TPS: 34.45
[User 12] Latency: 6.47s | Tokens: 223 | TPS: 34.44
[User 16] Latency: 6.50s | Tokens: 223 | TPS: 34.32
[User 4] Latency: 6.50s | Tokens: 223 | TPS: 34.31
[User 7] Latency: 6.50s | Tokens: 223 | TPS: 34.29
[User 2] Latency: 6.52s | Tokens: 223 | TPS: 34.21
[User 14] Latency: 6.52s | Tokens: 223 | TPS: 34.21
[User 5] Latency: 6.52s | Tokens: 223 | TPS: 34.20
[User 3] Latency: 6.52s | Tokens: 223 | TPS: 34.19
[User 20] Latency: 6.52s | Tokens: 223 | TPS: 34.20
[User 17] Latency: 6.53s | Tokens: 223 | TPS: 34.16
[User 21] Latency: 6.53s | Tokens: 223 | TPS: 34.15
[User 18] Latency: 6.53s | Tokens: 223 | TPS: 34.15
[User 1] Latency: 6.53s | Tokens: 223 | TPS: 34.13
[User 23] Latency: 6.53s | Tokens: 223 | TPS: 34.14
[User 0] Latency: 6.53s | Tokens: 223 | TPS: 34.13
[User 10] Latency: 6.53s | Tokens: 223 | TPS: 34.13
[User 15] Latency: 6.54s | Tokens: 223 | TPS: 34.10
[User 8] Latency: 6.57s | Tokens: 223 | TPS: 33.92
[User 6] Latency: 6.59s | Tokens: 223 | TPS: 33.84
[User 9] Latency: 7.00s | Tokens: 223 | TPS: 31.88
[User 19] Latency: 7.51s | Tokens: 223 | TPS: 29.69
[User 13] Latency: 7.51s | Tokens: 223 | TPS: 29.68
[User 24] Latency: 7.74s | Tokens: 223 | TPS: 28.80
```
---

## Third Try, 15 users concurrently for 5 min straight (using locust):

### e2e:
Prompt: "Explain inference benchmarking in 3 points"
  - TPS - 32.04, 32.03, 32.03, 32.03, 31.43, 31.43, 31.42, 31.42, 31.42, 31.42, 31.42, 31.41, 31.41, 31.41, 31.41, 31.40, 31.40, 31.39, 31.39, 31.39, 31.22, 31.19, 31.19, 31.19, 31.17 (avg: 31.47)
  - Tokens - 248 (constant)
  - Latency: 7.74s, 7.74s, 7.74s, 7.74s, 7.89s, 7.89s, 7.89s, 7.89s, 7.89s, 7.89s, 7.89s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.90s, 7.94s, 7.95s, 7.95s, 7.95s, 7.96s (avg: 7.89s)
raw output:
```bash
Starting load: 15 users for 300s on model 'llama3_1_8b_instruct'

========== Load Test Summary ==========
Duration:           305.90s
Users:              15
Total requests:     690
Total errors:       0
Requests/sec (RPS): 2.26
Total tokens:       171120
Tokens/sec (TPS):   559.40
Avg latency:        4.810s
P50 latency:        4.763s
P90 latency:        4.827s
P95 latency:        4.880s
P99 latency:        6.623s
=======================================
```

### nebius:
Prompt: "Explain inference benchmarking in 3 points"
  - TPS - 33.33, 34.45, 34.44, 34.32, 34.31, 34.29, 34.21, 34.21, 34.20, 34.19, 34.20, 34.16, 34.15, 34.15, 34.13, 34.14, 34.13, 34.13, 34.10, 33.92, 33.84, 31.88, 29.69, 29.68, 28.80 (avg: 33.44)
  - Tokens - 210, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223, 223 (avg: 222.48)
  - Latency - 6.30s, 6.47s, 6.47s, 6.50s, 6.50s, 6.50s, 6.52s, 6.52s, 6.52s, 6.52s, 6.52s, 6.53s, 6.53s, 6.53s, 6.53s, 6.53s, 6.53s, 6.53s, 6.54s, 6.57s, 6.59s, 7.00s, 7.51s, 7.51s, 7.74s (avg: 6.69s)
raw output:
```bash
User 11] Latency: 6.30s | Tokens: 210 | TPS: 33.33
[User 22] Latency: 6.47s | Tokens: 223 | TPS: 34.45
[User 12] Latency: 6.47s | Tokens: 223 | TPS: 34.44
[User 16] Latency: 6.50s | Tokens: 223 | TPS: 34.32
[User 4] Latency: 6.50s | Tokens: 223 | TPS: 34.31
[User 7] Latency: 6.50s | Tokens: 223 | TPS: 34.29
[User 2] Latency: 6.52s | Tokens: 223 | TPS: 34.21
[User 14] Latency: 6.52s | Tokens: 223 | TPS: 34.21
[User 5] Latency: 6.52s | Tokens: 223 | TPS: 34.20
[User 3] Latency: 6.52s | Tokens: 223 | TPS: 34.19
[User 20] Latency: 6.52s | Tokens: 223 | TPS: 34.20
[User 17] Latency: 6.53s | Tokens: 223 | TPS: 34.16
[User 21] Latency: 6.53s | Tokens: 223 | TPS: 34.15
[User 18] Latency: 6.53s | Tokens: 223 | TPS: 34.15
[User 1] Latency: 6.53s | Tokens: 223 | TPS: 34.13
[User 23] Latency: 6.53s | Tokens: 223 | TPS: 34.14
[User 0] Latency: 6.53s | Tokens: 223 | TPS: 34.13
[User 10] Latency: 6.53s | Tokens: 223 | TPS: 34.13
[User 15] Latency: 6.54s | Tokens: 223 | TPS: 34.10
[User 8] Latency: 6.57s | Tokens: 223 | TPS: 33.92
[User 6] Latency: 6.59s | Tokens: 223 | TPS: 33.84
[User 9] Latency: 7.00s | Tokens: 223 | TPS: 31.88
[User 19] Latency: 7.51s | Tokens: 223 | TPS: 29.69
[User 13] Latency: 7.51s | Tokens: 223 | TPS: 29.68
[User 24] Latency: 7.74s | Tokens: 223 | TPS: 28.80
```
---

**note: tokens/sec = (prompt_tokens + completion_tokens) ÷ total_elapsed_time**

----

## Using vLLM Benchamrking Kit

### Test 1 - 20 users for 5 minutes (to check steady RPS)

purpose: match your target user load and capture stable p50/p90/p95/p99.
20 rps × 300 s = 6000 prompts.

```bash
vllm bench serve \
  --backend openai-chat \
  --endpoint-type openai-chat \
  --base-url "$OPENAI_API_BASE" \
  --endpoint /chat/completions \
  --model "$DEFAULT_MODEL" \
  --served-model-name "$DEFAULT_MODEL" \
  --tokenizer "$TOKENIZER" \
  --dataset-name random \
  --random-input-len 256 --random-output-len 256 \
  --num-prompts 6000 --request-rate 20 --max-concurrency 40 \
  --no-stream \
  --percentile-metrics ttft,tpot,itl,e2el \
  --metric-percentiles 50,90,95,99 \
  --save-result --result-dir results/e2e --result-filename A_rps20_5m.json
```
#### E2E - TIR:

```bash
Maximum request concurrency: 40
100%|██████████████████████████████████████████| 6000/6000 [18:19<00:00,  5.46it/s]
============ Serving Benchmark Result ============
Successful requests:                     6000
Maximum request concurrency:             40
Request rate configured (RPS):           20.00
Benchmark duration (s):                  1099.79
Total input tokens:                      1527921
Total generated tokens:                  1390709
Request throughput (req/s):              5.46
Output token throughput (tok/s):         1264.52
Total Token throughput (tok/s):          2653.79
---------------Time to First Token----------------
Mean TTFT (ms):                          147.44
Median TTFT (ms):                        137.30
P50 TTFT (ms):                           137.30
P90 TTFT (ms):                           194.50
P95 TTFT (ms):                           224.16
P99 TTFT (ms):                           275.00
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          31.13
Median TPOT (ms):                        30.44
P50 TPOT (ms):                           30.44
P90 TPOT (ms):                           32.86
P95 TPOT (ms):                           33.39
P99 TPOT (ms):                           38.18
---------------Inter-token Latency----------------
Mean ITL (ms):                           31.04
Median ITL (ms):                         28.57
P50 ITL (ms):                            28.57
P90 ITL (ms):                            52.49
P95 ITL (ms):                            80.16
P99 ITL (ms):                            132.99
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7303.29
Median E2EL (ms):                        7867.71
P50 E2EL (ms):                           7867.71
P90 E2EL (ms):                           8461.22
P95 E2EL (ms):                           8594.66
P99 E2EL (ms):                           9315.35
==================================================
```

#### Nebius:

```bash
Traffic request rate: 20.0
Burstiness factor: 1.0 (Poisson process)
Maximum request concurrency: 40
100%|██████████████████████████████████████████| 6000/6000 [25:30<00:00,  3.92it/s]
============ Serving Benchmark Result ============
Successful requests:                     5999
Maximum request concurrency:             40
Request rate configured (RPS):           20.00
Benchmark duration (s):                  1530.33
Total input tokens:                      1527666
Total generated tokens:                  1563852
Request throughput (req/s):              3.92
Output token throughput (tok/s):         1021.91
Total Token throughput (tok/s):          2020.17
---------------Time to First Token----------------
Mean TTFT (ms):                          357.35
Median TTFT (ms):                        319.50
P50 TTFT (ms):                           319.50
P90 TTFT (ms):                           403.58
P95 TTFT (ms):                           511.12
P99 TTFT (ms):                           1234.84
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          34.46
Median TPOT (ms):                        32.76
P50 TPOT (ms):                           32.76
P90 TPOT (ms):                           42.89
P95 TPOT (ms):                           46.86
P99 TPOT (ms):                           60.66
---------------Inter-token Latency----------------
Mean ITL (ms):                           34.06
Median ITL (ms):                         28.89
P50 ITL (ms):                            28.89
P90 ITL (ms):                            45.88
P95 ITL (ms):                            64.77
P99 ITL (ms):                            163.74
----------------End-to-end Latency----------------
Mean E2EL (ms):                          9242.26
Median E2EL (ms):                        6559.66
P50 E2EL (ms):                           6559.66
P90 E2EL (ms):                           13296.82
P95 E2EL (ms):                           15884.70
P99 E2EL (ms):                           34766.47
==================================================
```

### Test 2 - concurrency (find saturation point)

purpose: match target user load and capture stable p50/p90/p95/p99.
20 rps × 300 s = 6000 prompts.

```bash
for C in 8 16 32 48 64 96; do
  vllm bench serve \
    --backend openai-chat \
    --endpoint-type openai-chat \
    --base-url "$OPENAI_API_BASE" \
    --endpoint /chat/completions \
    --model "$DEFAULT_MODEL" \
    --served-model-name "$DEFAULT_MODEL" \
    --tokenizer "$TOKENIZER" \
    --dataset-name random \
    --random-input-len 256 --random-output-len 256 \
    --num-prompts 1500 \
    --request-rate inf \
    --max-concurrency $C \
    --no-stream \
    --percentile-metrics ttft,tpot,itl,e2el \
    --metric-percentiles 50,90,95,99 \
    --ready-check-timeout-sec 15 \
    --save-result --result-dir results/e2e --result-filename B_conc${C}.json
done
```
#### E2E TIR:

```bash

```

#### Nebius:

```bash
```

note: the idea is throughput should climb with ```C``` until p95/p99 TTFT spikes—mark the last “good” C as sustainable. this pattern is widely used in vLLM perf threads.

### Test 3: prompt shape matrix (short / mid / long)
purpose: latency & throughput change with context length.

|Case	|` --random-input-len` |	`--random-output-len` |
|---| --- | --- |
|S	| 64	 | 128 |
|M	| 512	 | 256 |
|L	| 4096 | 256 |

```bash
vllm bench serve \
  --base-url "$OPENAI_API_BASE" --endpoint /completions \
  --model "$MODEL" --tokenizer "$TOKENIZER" \
  --dataset-name random \
  --random-input-len 4096 --random-output-len 256 \
  --num-prompts 1000 --request-rate 10 --max-concurrency 64 \
  --no-stream \
  --percentile-metrics ttft,tpot,itl,e2el \
  --metric-percentiles 50,90,95,99 \
  --save-result --result-dir results/e2e --result-filename C_long.json

```

### Test 4: streaming vs non-streaming
purpose: measure TTFT benefits & server behavior with SSE.

```bash
# non-stream (baseline)
vllm bench serve ... --no-stream \
  --save-result --result-dir results/e2e --result-filename D_nostream.json

# stream (remove --no-stream)
vllm bench serve ... \
  --save-result --result-dir results/e2e --result-filename D_stream.json
```

 <!--
```bash
jq -r '[.label?, .request_throughput, .output_token_throughput, .ttft_ms.p50, .ttft_ms.p95, .e2e_latency_ms.p50, .e2e_latency_ms.p95, .total_input_tokens, .total_output_tokens] | @csv' results/e2e/*.json
```
-->

---

RPS (Requests per Second): how many requests the system completed per second.
`RPS = successful_requests / benchmark_duration_sec`

TPS (Tokens per Second): ambiguous term—be explicit in your report:

  - Output Token Throughput (tok/s) = total_output_tokens / duration

  - Total Token Throughput (tok/s) = (input_tokens + output_tokens) / duration

  - Per-request TPS (your sequential runs) = tokens_returned / request_latency

TTFT (Time To First Token): time from request send → first token received. Proxy for perceived snappiness. Lower is better.

TPOT (Time Per Output Token) (excl. first token): cadence after streaming begins.
`TPOT ≈ 1 / (tokens_per_second_per_stream)`

ITL (Inter-Token Latency): measured gap between consecutive tokens when streaming. Similar to TPOT; sometimes includes small transport overheads.

E2E (End-to-End latency): request send → last token received. Depends heavily on output length.

Concurrency (in-flight): how many requests are simultaneously being processed.

Burstiness factor: if arrivals are Poisson (default), a factor of 1.0 = classic Poisson; >1 makes bursts spikier.

rule of thumb: TTFT = “how fast does it start talking?”, ITL/TPOT = “how fast does it keep talking?”, E2E = “when does it finish?”, tok/s = “how much work per second can it do?”
