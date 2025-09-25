## Overall Winner: E2E-TIR

### Key Performance Metrics Comparison

| Metric | E2E-TIR | Nebius | Winner |
|--------|---------|---------|---------|
| **Request Throughput** | 5.46 req/s | 3.92 req/s | E2E-TIR (39% better) |
| **Output Token Throughput** | 1264.52 tok/s | 1021.91 tok/s | E2E-TIR (24% better) |
| **Mean TTFT** | 147.44 ms | 357.35 ms | E2E-TIR (2.4x faster) |
| **P50 End-to-End Latency** | 7867.71 ms | 6559.66 ms | Nebius (17% better) |
| **P99 End-to-End Latency** | 9315.35 ms | 34766.47 ms | E2E-TIR (3.7x better) |
| **Test Duration** | 18:19 | 25:30 | E2E-TIR (40% faster) |

## Detailed Analysis by Category

### 1. **Time to First Token (TTFT)** - E2E-TIR Wins
- E2E-TIR is consistently 2-4x faster across all percentiles
- P50: 137ms vs 320ms
- P99: 275ms vs 1235ms
- This means users get initial responses much quicker with E2E-TIR

### 2. **Throughput** - E2E-TIR Wins
- Handles 39% more requests per second
- Processes 24% more tokens per second
- Completed the same workload in 18 minutes vs 25 minutes

### 3. **Consistency** - E2E-TIR Wins
- Much tighter variance between P50 and P99 metrics
- Nebius shows extreme P99 latency (34.7 seconds vs 9.3 seconds)
- E2E-TIR provides more predictable performance

### 4. **Token Generation Speed** - Comparable
- Both systems have similar TPOT (Time Per Output Token)
- E2E-TIR: 31.13ms mean
- Nebius: 34.46ms mean
- Only 10% difference here

## Why E2E-TIR Performs Better - Possible Reasons

### 1. **Better Architecture Optimization**
- More efficient request routing and load balancing
- Superior batching algorithms that group requests more effectively
- Optimized memory management reducing overhead

### 2. **Hardware Advantages**
- Potentially using newer GPU generations (A100/H100 vs older models)
- Better GPU memory bandwidth
- More optimized CPU-GPU communication
- Higher quality network infrastructure (lower latency interconnects)

### 3. **Software Stack Optimization**
- Better-tuned inference engine (vLLM configuration)
- More aggressive kernel fusion and optimization
- Superior model quantization or optimization techniques
- Better caching strategies for KV-cache management

### 4. **Infrastructure Scalability**
- More efficient auto-scaling under load
- Better resource allocation algorithms
- Lower system overhead and containerization costs

### 5. **Queue Management**
- E2E-TIR handles concurrent requests better (notice Nebius had 1 failed request)
- More sophisticated priority queuing
- Better timeout and retry mechanisms

---

**Executive Summary:**
E2E-TIR outperforms Nebius by 39% in throughput while maintaining 2.4x faster initial response times. Under sustained load, E2E-TIR shows superior stability with P99 latencies 3.7x better than Nebius.

**Key Takeaway:**
For production workloads requiring consistent performance and quick response times, E2E-TIR is the clear choice. Nebius shows concerning performance degradation at the tail end (P99), which could severely impact user experience during peak loads.

**Recommendation:**
Need to continue testing with TIR for higher load scenarios (Test 2, 3, etc.) to verify scalability, but based on this steady-state test, E2E-TIR demonstrates superior engineering and infrastructure quality.
