from typing import Dict, Any

# Model registry containing metadata for all available models
registry: Dict[str, Dict[str, Any]] = {
    # OpenAI models
    "gpt-3.5-turbo": {
        "source": "openai",
        "type": "instruct",
        "description": "OpenAI GPT-3.5 Turbo model"
    },
    "gpt-4": {
        "source": "openai",
        "type": "instruct",
        "description": "OpenAI GPT-4 model"
    },
    "gpt-4-turbo": {
        "source": "openai",
        "type": "instruct",
        "description": "OpenAI GPT-4 Turbo model"
    },



    # Hugging Face models
    "gpt2": {
        "source": "hf",
        "type": "base",
        "description": "GPT-2 base model from Hugging Face"
    },
    "llama": {
        "source": "hf",
        "type": "instruct",
        "description": "DialoGPT Small Chat model (lightweight demo)"
    },
    "distilgpt2": {
        "source": "hf",
        "type": "fine tuned",
        "description": "DistilGPT2 fine-tuned model"
    }
}