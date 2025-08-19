#!/usr/bin/env python3
"""
Setup script for Llama integration
This script helps you install dependencies and download a model
"""

import os
import subprocess
import sys
import urllib.request
from pathlib import Path

def install_dependencies():
    """Install required Python packages"""
    print("Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def download_model(model_name="llama-2-7b-chat", model_url=None):
    """Download a Llama model"""
    if not model_url:
        # Default model URLs
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
    
    print(f"Downloading {model_name}...")
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

def test_llama_integration():
    """Test if the Llama integration is working"""
    print("\nTesting Llama integration...")
    try:
        # Try to import llama_cpp
        import llama_cpp
        print("✅ llama-cpp-python is available")
        
        # Check if model exists
        model_path = get_model_path()
        if os.path.exists(model_path):
            print(f"✅ Model found at: {model_path}")
            
            # Try to initialize Llama
            try:
                from llama_cpp import Llama
                llm = Llama(model_path=model_path, n_ctx=512, n_threads=1)
                print("✅ Llama initialized successfully!")
                return True
            except Exception as e:
                print(f"❌ Failed to initialize Llama: {e}")
                return False
        else:
            print(f"❌ Model not found at: {model_path}")
            return False
            
    except ImportError:
        print("❌ llama-cpp-python not available")
        return False

def get_model_path():
    """Get model path from config or default"""
    try:
        from llama_config import get_model_path as config_get_path
        return config_get_path()
    except ImportError:
        return "llama-2-7b-chat.gguf"

def main():
    """Main setup function"""
    print("=" * 60)
    print("LLAMA SETUP FOR FOOD-METABOLITE ANALYSIS")
    print("=" * 60)
    
    # Step 1: Install dependencies
    if not install_dependencies():
        print("❌ Setup failed at dependency installation")
        return False
    
    # Step 2: Download model
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
        print("❌ Setup failed at model download")
        return False
    
    # Step 3: Test integration
    print("\n" + "=" * 40)
    print("TESTING INTEGRATION")
    print("=" * 40)
    
    if test_llama_integration():
        print("\n🎉 SETUP COMPLETE!")
        print("\nNext steps:")
        print("1. Test with 5 foods: python llama_integration.py --max-foods 5")
        print("2. Process all foods: python llama_integration.py")
        print("3. Open expert_interface.html to review results")
        return True
    else:
        print("\n❌ SETUP FAILED")
        print("Please check the error messages above and try again.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
