#!/usr/bin/env python3
"""
Test script for the Food-Metabolite Correlation Analysis System
"""

import json
import os
import sys
from food_metabolite_analyzer import FoodMetaboliteAnalyzer
from llama_integration import LlamaIntegration

def test_food_analyzer():
    """Test the food analyzer component"""
    print("Testing Food Analyzer...")
    
    try:
        analyzer = FoodMetaboliteAnalyzer()
        
        # Check if foods were loaded
        if not analyzer.foods:
            print("❌ ERROR: No foods loaded from foods.csv")
            return False
        
        print(f"✅ Loaded {len(analyzer.foods)} foods")
        
        # Test prompt generation
        sample_food = analyzer.foods[0]
        prompt = analyzer.generate_llama_prompt(sample_food)
        
        if not prompt or len(prompt) < 100:
            print("❌ ERROR: Generated prompt is too short or empty")
            return False
        
        print(f"✅ Generated prompt for '{sample_food}' ({len(prompt)} characters)")
        
        # Test saving prompts
        prompts_file = analyzer.save_prompts_to_file()
        if not os.path.exists(prompts_file):
            print(f"❌ ERROR: Prompts file {prompts_file} was not created")
            return False
        
        print(f"✅ Saved prompts to {prompts_file}")
        
        # Test interface data creation
        interface_file = analyzer.save_interface_data()
        if not os.path.exists(interface_file):
            print(f"❌ ERROR: Interface file {interface_file} was not created")
            return False
        
        print(f"✅ Saved interface data to {interface_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR in food analyzer: {e}")
        return False

def test_llama_integration():
    """Test the Llama integration component"""
    print("\nTesting Llama Integration...")
    
    try:
        # Check if prompts file exists
        if not os.path.exists("llama_prompts.json"):
            print("❌ ERROR: Prompts file not found. Run food analyzer first.")
            return False
        
        integration = LlamaIntegration()
        
        # Check if prompts were loaded
        if not integration.prompts:
            print("❌ ERROR: No prompts loaded")
            return False
        
        print(f"✅ Loaded {len(integration.prompts)} prompts")
        
        # Test processing a single food (mock mode)
        sample_food = list(integration.prompts.keys())[0]
        sample_prompt = integration.prompts[sample_food]
        
        correlations = integration.process_food(sample_food, sample_prompt)
        
        if not isinstance(correlations, list):
            print("❌ ERROR: process_food did not return a list")
            return False
        
        print(f"✅ Processed sample food '{sample_food}' and found {len(correlations)} correlations")
        
        # Test data structure creation
        test_correlations = {sample_food: {
            'prompt': sample_prompt,
            'correlations': correlations,
            'processed_at': '2024-01-01T00:00:00',
            'total_correlations': len(correlations)
        }}
        
        interface_data = integration.create_expert_interface_data(test_correlations)
        
        if 'foods' not in interface_data:
            print("❌ ERROR: Interface data structure is invalid")
            return False
        
        print(f"✅ Created interface data structure with {len(interface_data['foods'])} foods")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR in Llama integration: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\nTesting File Structure...")
    
    required_files = [
        "foods.csv",
        "food_metabolite_analyzer.py",
        "llama_integration.py",
        "expert_interface.html",
        "requirements.txt",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ ERROR: Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files present")
    return True

def test_json_files():
    """Test that generated JSON files are valid"""
    print("\nTesting Generated JSON Files...")
    
    json_files = [
        "llama_prompts.json",
        "expert_interface_data.json"
    ]
    
    for file in json_files:
        if os.path.exists(file):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                print(f"✅ {file} is valid JSON")
            except json.JSONDecodeError as e:
                print(f"❌ ERROR: {file} contains invalid JSON: {e}")
                return False
        else:
            print(f"⚠️  {file} not found (run food analyzer first)")
    
    return True

def main():
    """Run all tests"""
    print("Food-Metabolite Correlation Analysis System - Test Suite")
    print("=" * 60)
    
    tests = [
        test_file_structure,
        test_food_analyzer,
        test_llama_integration,
        test_json_files
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ ERROR: Test {test.__name__} failed with exception: {e}")
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! System is ready to use.")
        print("\nNext steps:")
        print("1. Set up Llama (see README.md for options)")
        print("2. Run: python llama_integration.py --max-foods 5")
        print("3. Open expert_interface.html in your browser")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
