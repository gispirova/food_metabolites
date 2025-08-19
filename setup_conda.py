#!/usr/bin/env python3
"""
Conda environment setup for Food-Metabolite Analysis
This script creates a dedicated conda environment and installs dependencies
"""

import os
import subprocess
import sys
import urllib.request
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    print(f"Running: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Success!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False

def check_conda():
    """Check if conda is available"""
    try:
        result = subprocess.run(["conda", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Conda found: {result.stdout.strip()}")
            return True
        else:
            print("❌ Conda not working properly")
            return False
    except FileNotFoundError:
        print("❌ Conda not found. Please install Anaconda or Miniconda first.")
        return False

def create_conda_environment():
    """Create the conda environment"""
    env_name = "food-metabolites"
    
    # Check if environment already exists
    try:
        result = subprocess.run(["conda", "env", "list"], capture_output=True, text=True)
        if env_name in result.stdout:
            print(f"✅ Environment '{env_name}' already exists")
            return True
    except:
        pass
    
    # Create environment from yml file
    if os.path.exists("environment.yml"):
        print("Creating conda environment from environment.yml...")
        return run_command(["conda", "env", "create", "-f", "environment.yml"], 
                         f"Creating conda environment '{env_name}'")
    else:
        # Fallback: create environment manually
        print("Creating conda environment manually...")
        return run_command(["conda", "create", "-n", env_name, "python=3.9", "-y"], 
                         f"Creating conda environment '{env_name}'")

def install_dependencies():
    """Install dependencies in the conda environment"""
    env_name = "food-metabolites"
    
    # Activate environment and install dependencies
    print(f"\nInstalling dependencies in '{env_name}' environment...")
    
    # Install core packages via conda
    conda_packages = ["requests", "typing-extensions", "pytest", "black", "flake8"]
    for package in conda_packages:
        if not run_command(["conda", "install", "-n", env_name, package, "-y"], 
                          f"Installing {package} via conda"):
            return False
    
    # Install llama-cpp-python via pip in the environment
    print("\nInstalling llama-cpp-python via pip...")
    pip_cmd = ["conda", "run", "-n", env_name, "pip", "install", "llama-cpp-python"]
    
    # Try different installation approaches
    approaches = [
        pip_cmd + ["--prefer-binary", "--no-cache-dir"],
        pip_cmd + ["--prefer-binary"],
        pip_cmd + ["--no-cache-dir"],
        pip_cmd
    ]
    
    for i, approach in enumerate(approaches):
        print(f"\nTrying approach {i+1}: {' '.join(approach)}")
        if run_command(approach, f"Installing llama-cpp-python (approach {i+1})"):
            break
        else:
            print(f"Approach {i+1} failed, trying next...")
    else:
        print("❌ All pip installation approaches failed")
        print("We'll try alternative methods...")
    
    return True

def download_model(model_name="llama-2-7b-chat"):
    """Download a Llama model"""
    model_urls = {
        "llama-2-7b-chat": "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf",
        "llama-2-13b-chat": "https://huggingface.co/TheBloke/Llama-2-13B-Chat-GGUF/resolve/main/llama-2-13b-chat.Q4_K_M.gguf",
        "llama-3-8b-instruct": "https://huggingface.co/TheBloke/Llama-3-8B-Instruct-GGUF/resolve/main/llama-3-8b-instruct.Q4_K_M.gguf"
    }
    
    model_url = model_urls.get(model_name)
    if not model_url:
        print(f"❌ Unknown model: {model_name}")
        return False
    
    filename = f"{model_name}.gguf"
    
    if os.path.exists(filename):
        print(f"✅ Model {filename} already exists!")
        return True
    
    print(f"\nDownloading {model_name}...")
    print(f"URL: {model_url}")
    print("This may take a while depending on your internet connection...")
    
    try:
        urllib.request.urlretrieve(model_url, filename)
        print(f"✅ Model downloaded successfully: {filename}")
        
        # Update the config file
        update_config_model_path(filename)
        
        return True
    except Exception as e:
        print(f"❌ Failed to download model: {e}")
        return False

def update_config_model_path(model_path):
    """Update the model path in the config file"""
    config_file = "llama_config.py"
    if not os.path.exists(config_file):
        print("⚠️  Config file not found, skipping update")
        return
    
    try:
        with open(config_file, 'r') as f:
            content = f.read()
        
        # Update the model path
        old_path = "llama-2-7b-chat.gguf"
        content = content.replace(old_path, model_path)
        
        with open(config_file, 'w') as f:
            f.write(content)
        
        print(f"✅ Updated config file with model path: {model_path}")
    except Exception as e:
        print(f"⚠️  Failed to update config file: {e}")

def test_environment():
    """Test the conda environment"""
    env_name = "food-metabolites"
    
    print(f"\nTesting '{env_name}' environment...")
    
    # Test Python import
    test_cmd = ["conda", "run", "-n", env_name, "python", "-c", 
                "import requests, typing_extensions; print('✅ Core packages imported successfully')"]
    
    if not run_command(test_cmd, "Testing core package imports"):
        return False
    
    # Test llama-cpp-python import
    test_llama_cmd = ["conda", "run", "-n", env_name, "python", "-c", 
                      "import llama_cpp; print('✅ llama-cpp-python imported successfully')"]
    
    if not run_command(test_llama_cmd, "Testing llama-cpp-python import"):
        print("⚠️  llama-cpp-python not available, but environment is working")
        print("We can use alternative methods (Ollama, command line)")
    
    return True

def print_activation_instructions():
    """Print instructions for activating the environment"""
    print("\n" + "=" * 60)
    print("ENVIRONMENT SETUP COMPLETE!")
    print("=" * 60)
    
    print(f"\nTo activate the environment, run:")
    print(f"conda activate food-metabolites")
    
    print(f"\nTo run the project in this environment:")
    print(f"conda activate food-metabolites")
    print(f"python llama_integration.py --max-foods 5")
    
    print(f"\nOr use conda run to run commands directly:")
    print(f"conda run -n food-metabolites python llama_integration.py --max-foods 5")
    
    print(f"\nTo deactivate the environment:")
    print(f"conda deactivate")

def main():
    """Main setup function"""
    print("=" * 60)
    print("CONDA ENVIRONMENT SETUP FOR FOOD-METABOLITE ANALYSIS")
    print("=" * 60)
    
    # Check conda
    if not check_conda():
        return False
    
    # Create environment
    if not create_conda_environment():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Download model
    print("\n" + "=" * 40)
    print("MODEL DOWNLOAD")
    print("=" * 40)
    
    print("Available models:")
    print("1. llama-2-7b-chat (smaller, faster)")
    print("2. llama-2-13b-chat (larger, better quality)")
    print("3. llama-3-8b-instruct (newer, good balance)")
    
    choice = input("\nChoose model (1-3) or press Enter for default (llama-2-7b-chat): ").strip()
    
    model_choice = {
        "1": "llama-2-7b-chat",
        "2": "llama-2-13b-chat", 
        "3": "llama-3-8b-instruct"
    }.get(choice, "llama-2-7b-chat")
    
    if not download_model(model_choice):
        print("❌ Model download failed")
        return False
    
    # Test environment
    if not test_environment():
        print("❌ Environment test failed")
        return False
    
    # Print instructions
    print_activation_instructions()
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Setup failed. Please check the error messages above.")
        sys.exit(1)
