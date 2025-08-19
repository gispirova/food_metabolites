#!/usr/bin/env python3
"""
Configuration file for Llama integration
Update these settings based on your Llama setup
"""

# Llama Configuration
LLAMA_CONFIG = {
    # Option 1: Python bindings (llama-cpp-python)
    "python_bindings": {
        "enabled": True,
        "model_path": "llama-2-13b-chat.gguf",  # Update this to your model path
        "n_ctx": 4096,  # Context window size
        "n_threads": 4,  # Number of CPU threads
        "n_gpu_layers": 0,  # Set to >0 if you have GPU
        "max_tokens": 2048,
        "temperature": 0.7
    },
    
    # Option 2: Ollama
    "ollama": {
        "enabled": False,  # Set to True if using Ollama
        "base_url": "http://localhost:11434",
        "model": "llama2",  # Your Ollama model name
        "max_tokens": 2048,
        "temperature": 0.7
    },
    
    # Option 3: Command line llama.cpp
    "command_line": {
        "enabled": False,  # Set to True if using command line
        "executable": "llama",  # Path to llama executable
        "model_path": "llama-2-13b-chat.gguf",  # Path to your model
        "max_tokens": 2048,
        "temperature": 0.7,
        "context_size": 4096
    }
}

# Processing Configuration
PROCESSING_CONFIG = {
    "max_foods": 5,  # Number of foods to process for testing
    "timeout": 300,  # Timeout for Llama calls in seconds
    "retry_attempts": 3,  # Number of retry attempts if Llama fails
    "delay_between_calls": 2  # Delay between food processing in seconds
}

# Model Download URLs (for reference)
MODEL_URLS = {
    "llama-2-7b-chat": "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf",
    "llama-2-13b-chat": "https://huggingface.co/TheBloke/Llama-2-13B-Chat-GGUF/resolve/main/llama-2-13b-chat.Q4_K_M.gguf",
    "llama-3-8b-instruct": "https://huggingface.co/TheBloke/Llama-3-8B-Instruct-GGUF/resolve/main/llama-3-8b-instruct.Q4_K_M.gguf"
}

def get_model_path():
    """Get the configured model path"""
    return LLAMA_CONFIG["python_bindings"]["model_path"]

def is_python_bindings_enabled():
    """Check if Python bindings are enabled"""
    return LLAMA_CONFIG["python_bindings"]["enabled"]

def is_ollama_enabled():
    """Check if Ollama is enabled"""
    return LLAMA_CONFIG["ollama"]["enabled"]

def is_command_line_enabled():
    """Check if command line is enabled"""
    return LLAMA_CONFIG["command_line"]["enabled"]

def get_processing_config():
    """Get processing configuration"""
    return PROCESSING_CONFIG.copy()

def print_setup_instructions():
    """Print setup instructions for the user"""
    print("=" * 60)
    print("LLAMA SETUP INSTRUCTIONS")
    print("=" * 60)
    
    print("\n1. INSTALL DEPENDENCIES:")
    print("   pip install -r requirements.txt")
    
    print("\n2. DOWNLOAD A MODEL:")
    print("   Choose one of these options:")
    for name, url in MODEL_URLS.items():
        print(f"   - {name}: {url}")
    
    print("\n3. UPDATE CONFIGURATION:")
    print("   Edit llama_config.py and update the model_path")
    print("   Example: 'model_path': 'path/to/your/model.gguf'")
    
    print("\n4. TEST THE INTEGRATION:")
    print("   python llama_integration.py --max-foods 5")
    
    print("\n5. PROCESS ALL FOODS:")
    print("   python llama_integration.py")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    print_setup_instructions()
