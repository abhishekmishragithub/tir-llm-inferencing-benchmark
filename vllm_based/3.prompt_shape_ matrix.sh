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
  --random-input-len 4096 --random-output-len 256 \
  --num-prompts 1000 --request-rate 10 --max-concurrency 64 \
  --no-stream \
  --percentile-metrics ttft,tpot,itl,e2el \
  --metric-percentiles 50,90,95,99 \
  --metadata "suite=3_prompt_shape_matrix,provider=${PROVIDER_NAME}" \
  --save-result --result-dir results/${PROVIDER_NAME} --result-filename 3_${PROVIDER_NAME}_result_long.json
