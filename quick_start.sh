#!/bin/bash

echo "🚀 Food-Metabolite Correlation Analysis System - Quick Start"
echo "============================================================"
echo ""

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed or not in PATH"
    echo "Please install Python 3.7+ and try again"
    exit 1
fi

echo "✅ Python found: $(python --version)"
echo ""

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "⚠️  Some dependencies may not have installed. Continuing anyway..."
fi

echo ""

# Step 1: Generate prompts
echo "🔍 Step 1: Generating prompts for all foods..."
python food_metabolite_analyzer.py

if [ $? -ne 0 ]; then
    echo "❌ Failed to generate prompts. Please check the error above."
    exit 1
fi

echo ""

# Step 2: Test with a few foods
echo "🤖 Step 2: Testing Llama integration with 3 foods..."
python llama_integration.py --max-foods 3

if [ $? -ne 0 ]; then
    echo "❌ Failed to process foods with Llama. Please check the error above."
    exit 1
fi

echo ""

# Step 3: Run tests
echo "🧪 Step 3: Running system tests..."
python test_system.py

if [ $? -ne 0 ]; then
    echo "❌ Some tests failed. Please check the errors above."
    exit 1
fi

echo ""
echo "🎉 Quick start completed successfully!"
echo ""
echo "📁 Generated files:"
echo "   - llama_prompts.json (prompts for all 153 foods)"
echo "   - llama_correlations.json (sample correlations for 3 foods)"
echo "   - expert_interface_data.json (data for the web interface)"
echo ""
echo "🌐 Next steps:"
echo "   1. Open expert_interface.html in your web browser"
echo "   2. Set up Llama (see README.md for options)"
echo "   3. Run: python llama_integration.py (to process all foods)"
echo "   4. Have experts verify correlations in the web interface"
echo ""
echo "📚 For detailed instructions, see README.md"
echo "🔧 For Llama setup help, see the Llama Integration Setup section in README.md"
