PROVIDER_NAME=${PROVIDER_NAME:-"default"}
echo "Benchmarking for provider ${PROVIDER_NAME}"

# streaming
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
  --temperature 0 --top_p 1 \
  --no-stream \
  --percentile-metrics ttft,tpot,itl,e2el \
  --metric-percentiles 50,90,95,99 \
  --save-result --save-detailed \
  --metadata "suite=4_nonstream,provider=${PROVIDER_NAME},shape=256x256,rps=20,conc=40" \
  --result-dir results/${PROVIDER_NAME} --result-filename 4_${PROVIDER_NAME}_nostream_256x256_rps20_c40.json


#non-streaming
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
  --temperature 0 --top_p 1 \
  --percentile-metrics ttft,tpot,itl,e2el \
  --metric-percentiles 50,90,95,99 \
  --save-result --save-detailed \
  --metadata "suite=4_stream,provider=${PROVIDER_NAME},shape=256x256,rps=20,conc=40" \
  --result-dir results/${PROVIDER_NAME} --result-filename 4_${PROVIDER_NAME}_stream_256x256_rps20_c40.json




#print result
# jq -r '[.label?, .request_throughput, .output_token_throughput, .ttft_ms.p50, .ttft_ms.p95, .e2e_latency_ms.p50, .e2e_latency_ms.p95, .total_input_tokens, .total_output_tokens] | @csv' results/e2e/*.json
