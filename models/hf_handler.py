from typing import Dict, Any
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

HF_MODELS = {
    "gpt2": "gpt2",
    "llama": "microsoft/DialoGPT-small",   # Smaller alternative to LLaMA for demo
    "distilgpt2": "distilgpt2"  # DistilGPT2 fine-tuned model
}
cache = {}

def query_local_models(prompt: str, model_name: str = "gpt2") -> Dict[str, Any]:
    if model_name not in cache :
        try:
            # Use low memory loading for efficiency
            tokenizer = AutoTokenizer.from_pretrained(
                HF_MODELS[model_name],
                cache_dir="./cache/tokenizers"
            )
            model = AutoModelForCausalLM.from_pretrained(
                HF_MODELS[model_name],
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                low_cpu_mem_usage=True,
                cache_dir="./cache/models"
            )
            model.eval()
            cache[model_name] = (tokenizer, model)
        except Exception as e:
            return {
                "model": model_name,
                "response": f"Error loading model: {str(e)}",
                "token_usage": 0
            }

    tokenizer, model = cache[model_name] 

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=inputs['input_ids'].shape[1] + 50, max_new_tokens=100 ,do_sample=True)

    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Remove the original prompt from the response
    response_text = response_text[len(prompt):].strip()
    
    total_tokens = len(inputs.input_ids[0]) + len(outputs[0])
    
    return {
        "model": model_name,
        "response": response_text,
        "token_usage": total_tokens
    }
