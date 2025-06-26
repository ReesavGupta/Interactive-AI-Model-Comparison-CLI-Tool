# Interactive AI Model Comparison CLI Tool

A powerful command-line tool for comparing different types of AI models (Base, Instruct, and Fine-tuned) across multiple providers including OpenAI and Hugging Face. This tool helps developers and researchers understand the characteristics and performance differences between various AI model architectures.

## 🚀 Features

- **Multi-Model Support**: Compare models from OpenAI and Hugging Face
- **Cross-Type Comparison**: Compare Base, Instruct, and Fine-tuned models side-by-side
- **Interactive CLI**: User-friendly interface with questionary-based selection
- **Token Usage Analysis**: Track and display token consumption for each model
- **Error Handling**: Robust error handling with graceful degradation
- **Flexible Comparison Modes**: Choose between type-specific or cross-type comparisons

## 📋 Supported Models

### OpenAI Models (Instruct)
- GPT-3.5-turbo
- GPT-4
- GPT-4-turbo

### Hugging Face Models
- **Base**: GPT-2 (~500MB)
- **Instruct**: DialoGPT-Small (~350MB)
- **Fine-tuned**: DistilGPT2 (~350MB)

> **Note**: Models are downloaded automatically on first use and cached locally.

## 🛠 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Interactive-AI-Model-Comparison-CLI-Tool
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🎯 Usage

### Basic Usage
```bash
python compare_models.py compare
```

### Interactive Flow
1. **Enter your prompt**: Type the question or text you want to test
2. **Select comparison mode**:
   - "By type" - Compare models within the same category
   - "All models" - Compare across different model types
3. **Choose models**: Use SPACE to select, ENTER to confirm
4. **View results**: See responses with token usage analysis

### Example Session
```
$ python compare_models.py compare
Comparing models...
? Enter your prompt: What is quantum computing?
? Select comparison mode: All models (cross-type comparison)
? Select models to compare: [gpt-3.5-turbo, gpt2, distilgpt2]

Running comparison...
[Results displayed with formatted panels]
```

## 📊 Understanding the Output

Each model response includes:
- **Model name and type**
- **Generated response**
- **Token usage statistics**
- **Source provider** (OpenAI/HF)
- **Error handling** (if model fails)

## 🔧 Configuration

### Adding New Models
Edit `models/registry.py` to add new models:
```python
"model-name": {
    "source": "openai|hf",
    "type": "base|instruct|fine tuned",
    "description": "Model description"
}
```

### Model Handlers
- `models/openai_handler.py` - OpenAI API integration
- `models/hf_handler.py` - Hugging Face models
- `models/registry.py` - Model configuration

## 📁 Project Structure
```
Interactive-AI-Model-Comparison-CLI-Tool/
├── compare_models.py          # Main CLI application
├── models/
│   ├── __init__.py
│   ├── registry.py           # Model registry and metadata
│   ├── openai_handler.py     # OpenAI API integration
│   └── hf_handler.py         # Hugging Face model handling
├── utils/
│   └── token_utils.py        # Token counting utilities
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── README.md               # This file
└── comparisons.md          # Detailed model comparison analysis
```

## 🔑 API Keys Setup

### OpenAI API Key
1. Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new API key
3. Add to your `.env` file as `OPENAI_API_KEY=your_key_here`

### Hugging Face (Optional)
- Most models work without authentication
- For private models, get a token from [Hugging Face](https://huggingface.co/settings/tokens)

## 🎨 Customization

### Adding Custom Prompts
You can create preset prompts by modifying the questionary input in `compare_models.py`.

### Styling
The tool uses Rich library for formatting. Customize colors and styles in the Panel configurations.

### Token Analysis
Extend `utils/token_utils.py` to add more detailed token analysis features.

## 🐛 Troubleshooting

### Common Issues

**"No models selected" error**
- Use SPACE bar to select models in the checkbox interface
- Make sure to press ENTER after selecting

**OpenAI API errors**
- Check your API key in `.env`
- Verify you have sufficient credits
- Ensure the model name is correct

**Hugging Face model loading issues**
- First run downloads models (can be large)
- Ensure sufficient disk space
- Check internet connection for downloads

**Memory issues with large models**
- Models are optimized for smaller sizes (~350-500MB each)
- Consider using smaller models for testing
- Close other applications to free memory

## 📈 Performance & Size Optimization

- **Repository size**: ~50KB (minimal, models downloaded on demand)
- **First run**: Hugging Face models download automatically (~1GB total)
- **Subsequent runs**: Models are cached locally for faster loading
- **Memory usage**: Optimized for smaller models (GPT-2: ~500MB, DialoGPT: ~350MB)
- **Token limits**: Respect API rate limits and quotas

### 🧹 Repository Cleanup
To minimize repository size before committing:
```bash
python cleanup.py
```
This removes all cached models, temporary files, and virtual environments.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Further Reading

- [Model Comparison Analysis](comparisons.md) - Detailed comparison results
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)

---

**Happy comparing!** 🎉

For questions or issues, please open a GitHub issue or contact the maintainers.