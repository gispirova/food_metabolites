#!/usr/bin/env python3
"""
Test script for Llama integration
Run this to verify your setup is working
"""

import json
import os
from llama_integration import LlamaIntegration

def test_llama_setup():
    """Test the Llama integration setup"""
    print("=" * 50)
    print("TESTING LLAMA INTEGRATION SETUP")
    print("=" * 50)
    
    # Check if prompts exist
    if not os.path.exists("llama_prompts.json"):
        print("❌ llama_prompts.json not found")
        print("Please run: python food_metabolite_analyzer.py first")
        return False
    
    # Check if model exists
    try:
        from llama_config import get_model_path
        model_path = get_model_path()
        if not os.path.exists(model_path):
            print(f"❌ Model not found at: {model_path}")
            print("Please run: python setup_llama.py to download a model")
            return False
        print(f"✅ Model found: {model_path}")
    except ImportError:
        print("⚠️  llama_config.py not found, using default settings")
    
    # Test with a single food
    print("\nTesting with a single food...")
    integration = LlamaIntegration()
    
    if not integration.prompts:
        print("❌ No prompts loaded")
        return False
    
    # Get first food
    first_food = list(integration.prompts.keys())[0]
    first_prompt = integration.prompts[first_food]
    
    print(f"Testing with: {first_food}")
    print(f"Prompt length: {len(first_prompt)} characters")
    
    # Test Llama call
    print(f"\nCalling Llama for {first_food}...")
    response = integration.call_llama(first_prompt, first_food)
    
    if response:
        print("✅ Llama responded successfully!")
        print(f"Response length: {len(response)} characters")
        print("\nFirst 200 characters of response:")
        print(response[:200] + "..." if len(response) > 200 else response)
        
        # Test parsing
        correlations = integration.parse_llama_response(response, first_food)
        print(f"\n✅ Parsed {len(correlations)} correlations")
        
        return True
    else:
        print("❌ Llama call failed")
        return False

def main():
    """Main test function"""
    if test_llama_setup():
        print("\n🎉 LLAMA SETUP IS WORKING!")
        print("\nYou can now:")
        print("1. Test with 5 foods: python llama_integration.py --max-foods 5")
        print("2. Process all foods: python llama_integration.py")
        print("3. Open expert_interface.html to review results")
    else:
        print("\n❌ LLAMA SETUP HAS ISSUES")
        print("Please check the error messages above and fix them.")

if __name__ == "__main__":
    main()
