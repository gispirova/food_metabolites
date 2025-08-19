# Food-Metabolite Correlation Analysis System

An AI-driven system for analyzing correlations between food exposure and metabolites in blood samples, designed for untargeted metabolomics studies in COPDGene and MGB BioBank projects.

## Overview

This system leverages current scientific literature knowledge to understand plausible dietary patterns through blood sample analysis, without requiring food-frequency questionnaires or patient interviews. It uses Llama (latest version) to generate prompts and find scientific references linking specific foods with blood metabolites.

## Features

- **Automated Prompt Generation**: Creates specialized prompts for each food item
- **Llama Integration**: Uses latest Llama models to find scientific correlations
- **Expert Review Interface**: Web-based interface for experts to verify correlations
- **Structured Data Export**: JSON format for further analysis
- **Comprehensive Coverage**: Handles 100+ food items from your CSV

## System Architecture

```
foods.csv → Food Analyzer → Llama Prompts → Llama Processing → Expert Interface → Verified Data
```

## Files Structure

- `foods.csv` - Input food list (comma-separated)
- `food_metabolite_analyzer.py` - Main analyzer script
- `llama_integration.py` - Llama processing integration
- `expert_interface.html` - Web interface for expert review
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## Installation

1. **Clone or download the project files**
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Llama** (choose one option):
   
   **Option A: llama.cpp (Command Line)**
   ```bash
   # Download and compile llama.cpp
   git clone https://github.com/ggerganov/llama.cpp
   cd llama.cpp
   make
   
   # Download a model (e.g., Llama 2 7B)
   # Place your .gguf model file in the project directory
   ```
   
   **Option B: Python Bindings**
   ```bash
   pip install llama-cpp-python
   ```
   
   **Option C: Ollama**
   ```bash
   # Install Ollama from https://ollama.ai/
   ollama pull llama2
   ```

## Usage

### Step 1: Generate Prompts

First, run the analyzer to process your foods and generate prompts:

```bash
python food_metabolite_analyzer.py
```

This will:
- Load foods from `foods.csv`
- Generate specialized prompts for each food
- Save prompts to `llama_prompts.json`
- Create initial interface data in `expert_interface_data.json`

### Step 2: Process with Llama

Run the Llama integration to find correlations:

```bash
python llama_integration.py
```

**Command line options**:
- `--prompts FILE`: Input prompts file (default: `llama_prompts.json`)
- `--output FILE`: Output correlations file (default: `llama_correlations.json`)
- `--max-foods N`: Process only first N foods (useful for testing)
- `--interface-output FILE`: Expert interface data file

**Example**:
```bash
python llama_integration.py --max-foods 5 --output test_correlations.json
```

### Step 3: Expert Review

Open `expert_interface.html` in a web browser to review and verify correlations.

## Llama Integration Setup

### Option 1: llama.cpp (Command Line)

Edit `llama_integration.py` and uncomment the command-line section:

```python
cmd = [
    "llama",  # or path to your llama executable
    "--model", "path/to/your/model.gguf",
    "--prompt", prompt,
    "--n-predict", "2048",
    "--temp", "0.7"
]
result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
return result.stdout
```

### Option 2: Python Bindings

Edit `llama_integration.py` and uncomment the Python bindings section:

```python
from llama_cpp import Llama
llm = Llama(model_path="path/to/your/model.gguf")
response = llm(prompt, max_tokens=2048, temperature=0.7)
return response['choices'][0]['text']
```

### Option 3: Ollama

Edit `llama_integration.py` and uncomment the Ollama section:

```python
import requests
response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama2",  # or your specific model name
    "prompt": prompt,
    "stream": False
})
return response.json()['response']
```

## Expert Interface Features

The web interface provides:

- **Food List**: Browse all processed foods with correlation counts
- **Search**: Find specific foods quickly
- **Correlation Table**: View all found correlations with:
  - Reference (paper citation)
  - Metabolite name
  - Correlation type (positive/negative)
  - Finding description
  - Relevant quote from the paper
- **Verification System**: Click buttons to mark correlations as True/False
- **Expert Notes**: Add detailed notes for each correlation
- **Export**: Download verified data or all data as JSON

## Data Format

### Input Format (`foods.csv`)
```
broccoli, cabbage, coleslaw, cauliflower, brussels sprouts, kale, ...
```

### Output Format (Correlations)
```json
{
  "food_name": {
    "prompt": "Generated prompt for Llama",
    "correlations": [
      {
        "reference": "Smith et al. (2023) - Journal of Nutrition",
        "metabolite": "Sulforaphane",
        "correlationType": "Positive",
        "finding": "Increased plasma levels after consumption",
        "relevantQuote": "Quote from the paper...",
        "verified": null,
        "expertNotes": ""
      }
    ],
    "processed_at": "2024-01-01T12:00:00",
    "total_correlations": 1
  }
}
```

## Customization

### Modifying Prompts

Edit the `generate_llama_prompt()` method in `food_metabolite_analyzer.py` to customize the prompt structure.

### Adding New Food Sources

Modify the `load_foods()` method to support different input formats (Excel, database, etc.).

### Enhancing Llama Integration

Customize the `call_llama()` method in `llama_integration.py` for your specific Llama setup.

## Troubleshooting

### Common Issues

1. **"No prompts loaded"**: Run `food_metabolite_analyzer.py` first
2. **Llama not responding**: Check your Llama installation and model path
3. **Interface not loading**: Ensure all JSON files are generated and accessible

### Performance Tips

- Use `--max-foods` to test with a subset first
- Adjust Llama parameters (temperature, max_tokens) for better results
- Consider batch processing for large numbers of foods

## Example Workflow

1. **Start with your foods.csv**:
   ```bash
   python food_metabolite_analyzer.py
   ```

2. **Process with Llama** (test with 5 foods first):
   ```bash
   python llama_integration.py --max-foods 5
   ```

3. **Review results** in the expert interface:
   - Open `expert_interface.html` in your browser
   - Click on foods to see correlations
   - Verify each correlation (True/False)
   - Add expert notes

4. **Export verified data** for further analysis

5. **Process remaining foods**:
   ```bash
   python llama_integration.py
   ```

## Contributing

To enhance the system:

1. Improve prompt engineering for better Llama responses
2. Add support for different Llama models and configurations
3. Enhance the expert interface with additional features
4. Add validation and quality control measures
5. Integrate with external databases (PubMed, etc.)

## License

This project is designed for research purposes. Please ensure compliance with your institution's policies and relevant regulations.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the code comments for implementation details
3. Ensure your Llama setup is working correctly
4. Verify all dependencies are installed

## Citation

If you use this system in your research, please cite:
- The underlying Llama model you use
- This system as a tool for food-metabolite correlation analysis
- Any relevant papers from the correlations you discover
