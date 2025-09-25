##### smoke test ######

PROVIDER_NAME=${PROVIDER_NAME:-"default"}
echo "Benchmarking for provider ${PROVIDER_NAME}"

# test if the api is working for vLLM compatibility
curl -sS -i "$OPENAI_API_BASE/completions" \
    -H "Authorization: Bearer $OPENAI_API_KEY" -H "Content-Type: application/json" \
    -d "{\"model\":\"$DEFAULT_MODEL\",\"prompt\":\"ping\",\"max_tokens\":4,\"stream\":false}"

# vllm smoke test for compatibility
vllm bench serve \
  --backend openai-chat \
  --endpoint-type openai-chat \
  --base-url "$OPENAI_API_BASE" \
  --endpoint /chat/completions \
  --model "$DEFAULT_MODEL" \
  --served-model-name "$DEFAULT_MODEL" \
  --tokenizer "$TOKENIZER" \
  --num-prompts 60 \
  --random-input-len 128 --random-output-len 128 \
  --request-rate 2 --max-concurrency 4 \
  --no-stream \
  --ready-check-timeout-sec 15 \
  --save-result --save-detailed \
  --metadata "suite=0_smoke_test,provider=${PROVIDER_NAME}" \
  --result-dir results/${PROVIDER_NAME} --result-filename "0_${PROVIDER_NAME}_result.json"
