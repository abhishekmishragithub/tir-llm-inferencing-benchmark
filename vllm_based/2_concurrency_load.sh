PROVIDER_NAME=${PROVIDER_NAME:-"default"}
echo "Benchmarking for provider ${PROVIDER_NAME}"

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
    --metadata "suite=2_concurrency_load,provider=${PROVIDER_NAME}" \
    --save-result --result-dir results/${PROVIDER_NAME} --result-filename 2_${PROVIDER_NAME}_conc${C}_result.json
done
