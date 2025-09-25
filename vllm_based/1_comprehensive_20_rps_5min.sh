
PROVIDER_NAME=${PROVIDER_NAME:-"default"}
echo "Benchmarking for provider ${PROVIDER_NAME}"

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
  --ready-check-timeout-sec 15 \
  --metadata "suite=1_rps_20_5m,provider=${PROVIDER_NAME}" \
  --save-result --result-dir results/${PROVIDER_NAME} --result-filename 1_${PROVIDER_NAME}_result_rps20_5m.json
