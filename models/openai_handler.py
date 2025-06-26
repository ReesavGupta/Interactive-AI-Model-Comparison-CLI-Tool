import os
from typing import Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_openai(prompt: str, model: str = "gpt-3.5-turbo") -> Dict[str, Any]:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    msg = response.choices[0].message.content

    if msg is None:
        msg = ""
    else:
        msg = msg.strip()

    token_usage = response.usage.total_tokens if response.usage else 0

    return {
        "model" : model,
        "response" : msg,
        "token_usage" : token_usage
    }    

# REESAV@LAPTOP-C70HI7IG MINGW64 /c/Users/REESAV/Desktop/misogi-assignments/day - 4 []/Interactive-AI-Model-Comparison-CLI-Tool (master)
# $ python compare_models.py compare
# Comparing models...
# ─────────────────────────────────────  moodel comparision CLI ─────────────────────────────────────
# ? Enter your prompt:  what are dinosaurs?
# ? Select comparison mode: All models (cross-type comparison)
# All available models: ['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo', 'gpt2', 'llama', 'alpaca']
# ? Select models to compare (use SPACE to select, ENTER to confirm): [alpaca (fine tuned - hf)]     

# Running comparison...

# Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
# Both `max_new_tokens` (=100) and `max_length`(=54) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)
# ╭──────────────────────────────── HF ────────────────────────────────╮
# │ alpaca                                                             │
# │                                                                    │
# │ Do YOU think you need to go with us from a biological perspective? │
# │                                                                    │
# │ Tokens used: 23                                                    │
# ╰────────────────────────────────────────────────────────────────────╯
# (.venv) 
# REESAV@LAPTOP-C70HI7IG MINGW64 /c/Users/REESAV/Desktop/misogi-assignments/day - 4 []/Interactive-AI-Model-Comparison-CLI-Tool (master)
# $
# (.venv)
# REESAV@LAPTOP-C70HI7IG MINGW64 /c/Users/REESAV/Desktop/misogi-assignments/day - 4 []/Interactive-AI-Model-Comparison-CLI-Tool (master)
# $ python compare_models.py compare
# Comparing models...
# ─────────────────────────────────────  moodel comparision CLI ─────────────────────────────────────
# ? Enter your prompt:  what is dinosaur?
# ? Select comparison mode: All models (cross-type comparison)
# All available models: ['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo', 'gpt2', 'llama', 'distilgpt2']     
# ? Select models to compare (use SPACE to select, ENTER to confirm): [llama (instruct - hf)]        

# Running comparison...

# tokenizer_config.json: 100%|█████████████████████████████████████████| 1.62k/1.62k [00:00<?, ?B/s]
# C:\Users\REESAV\Desktop\misogi-assignments\day - 4 []\Interactive-AI-Model-Comparison-CLI-Tool\.venv\Lib\site-packages\huggingface_hub\file_download.py:143: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in C:\Users\REESAV\.cache\huggingface\hub\models--meta-llama--Llama-2-7b-chat-hf. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
# To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. In order to activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
#   warnings.warn(message)
# Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package[hf_xet]` or `pip install hf_xet`
# tokenizer.model: 100%|██████████████████████████████████████████| 500k/500k [00:00<00:00, 546kB/s]
# tokenizer.json: 100%|████████████████████████████████████████| 1.84M/1.84M [00:00<00:00, 2.85MB/s]
# special_tokens_map.json: 100%|███████████████████████████████████████████| 414/414 [00:00<?, ?B/s]
# config.json: 100%|███████████████████████████████████████████████████████| 614/614 [00:00<?, ?B/s]
# model.safetensors.index.json: 100%|██████████████████████████| 26.8k/26.8k [00:00<00:00, 1.61MB/s]
# Fetching 2 files:   0%|                                                     | 0/2 [00:00<?, ?it/s]Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package with: `pip install huggingface_hub[hf_xet]` or `pip install hf_xet`
# Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package with: `pip install huggingface_hub[hf_xet]` or `pip install hf_xet`
# model-00002-of-00002.safetensors: 100%|██████████████████████| 3.50G/3.50G [09:02<00:00, 6.46MB/s]
# model-00001-of-00002.safetensors: 100%|██████████████████████| 9.98G/9.98G [20:12<00:00, 8.23MB/s]
# Fetching 2 files: 100%|████████████████████████████████████████████| 2/2 [20:14<00:00, 607.17s/it]
# Loading checkpoint shards: 100%|████████████████████████████████████| 2/2 [01:16<00:00, 38.13s/it]
# generation_config.json: 100%|████████████████████████████████████████████| 188/188 [00:00<?, ?B/s]
# Both `max_new_tokens` (=100) and `max_length`(=57) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)
# ╭────────────────────────────────────────────────────────────────────────────── HF ───────────────────────────────────────────────────────────────────────────────╮
# │ llama                                                                                            
#                                                                │
# │ A dinosaur is a type of reptile that lived during the Mesozoic Era, which lasted from about 252 million to 66 million years ago. Dinosaurs were incredibly      │
# │ diverse, with over 1,800 known species ranging in size, shape, and behavior. Some dinosaurs were plant-eaters, while others were meat-eaters.                   │
# │                                                                                                                                                                 │
# │ Dinosaurs are known for their unique characteristics, such                                                                                                      │
# │                                                                                                                                                                 │
# │ Tokens used: 114                                                                                                                                                │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
# (.venv)

# REESAV@LAPTOP-C70HI7IG MINGW64 /c/Users/REESAV/Desktop/misogi-assignments/day - 4 []/Interactive-AI-Model-Comparison-CLI-Tool (master)
# $ python compare_models.py compare
# Comparing models...
# ─────────────────────────────────────  moodel comparision CLI ─────────────────────────────────────
# ? Enter your prompt:  what is quantum computing?
# ? select your model type: fine tuned
# Available fine tuned models: ['alpaca']
# Auto-selected the only available model: alpaca

# Running comparison...

# Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
# Both `max_new_tokens` (=100) and `max_length`(=55) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)
# ╭────────────────────────────────────────────── HF ───────────────────────────────────────────────╮
# │ alpaca                                                                                          │
# │                                                                                                 │
# │ I'm not sure any more than quantum computing is capable of making calculations. But what? This  │
# │ might be my main question. Well, I've been looking at quantum statistics and the quantum        │
# │ methods that we used for the first time. This is a fascinating question, a question I've been   │
# │ asked many times. Now, when I talk about quantum theory, a lot of them come from the academic   │
# │ side. At this point, I want to be more specific. I have no particular interest in quantum       │
# │ theory,                                                                                         │
# │                                                                                                 │
# │ Tokens used: 110                                                                                │
# ╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
# (.venv) 