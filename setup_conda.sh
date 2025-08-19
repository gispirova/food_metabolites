#!/bin/bash

# Conda Environment Setup for Food-Metabolite Analysis
# This script creates and manages the conda environment

set -e  # Exit on any error

echo "============================================================"
echo "CONDA ENVIRONMENT SETUP FOR FOOD-METABOLITE ANALYSIS"
echo "============================================================"

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "❌ Conda not found. Please install Anaconda or Miniconda first."
    echo "Download from: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

echo "✅ Conda found: $(conda --version)"

# Environment name
ENV_NAME="food-metabolites"

# Check if environment already exists
if conda env list | grep -q "^$ENV_NAME "; then
    echo "✅ Environment '$ENV_NAME' already exists"
    echo "Activating existing environment..."
    conda activate $ENV_NAME
else
    echo "Creating new conda environment '$ENV_NAME'..."
    
    # Create environment from yml file if it exists
    if [ -f "environment.yml" ]; then
        echo "Creating environment from environment.yml..."
        conda env create -f environment.yml
    else
        echo "Creating environment manually..."
        conda create -n $ENV_NAME python=3.9 -y
    fi
    
    # Activate the environment
    conda activate $ENV_NAME
fi

echo "✅ Environment '$ENV_NAME' is now active"

# Install dependencies
echo "Installing dependencies..."

# Install core packages via conda
conda install -n $ENV_NAME requests typing-extensions pytest black flake8 -y

# Try to install llama-cpp-python via pip
echo "Installing llama-cpp-python..."
pip install llama-cpp-python --prefer-binary --no-cache-dir || {
    echo "⚠️  llama-cpp-python installation failed, trying alternative..."
    pip install llama-cpp-python --prefer-binary || {
        echo "⚠️  Still failed, but environment is ready for alternative methods"
    }
}

# Test the environment
echo "Testing environment..."
python -c "import requests, typing_extensions; print('✅ Core packages imported successfully')"

# Try to import llama_cpp
python -c "import llama_cpp; print('✅ llama-cpp-python imported successfully')" || {
    echo "⚠️  llama-cpp-python not available, but environment is working"
    echo "We can use alternative methods (Ollama, command line)"
}

echo ""
echo "============================================================"
echo "ENVIRONMENT SETUP COMPLETE!"
echo "============================================================"
echo ""
echo "To activate this environment in the future:"
echo "conda activate $ENV_NAME"
echo ""
echo "To run the project:"
echo "conda activate $ENV_NAME"
echo "python llama_integration.py --max-foods 5"
echo ""
echo "To deactivate:"
echo "conda deactivate"
echo ""
echo "Next steps:"
echo "1. Download a Llama model (run: python setup_conda.py)"
echo "2. Test the integration (run: python test_llama_setup.py)"
echo "3. Process foods with Llama (run: python llama_integration.py --max-foods 5)"
echo ""
