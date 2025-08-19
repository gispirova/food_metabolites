#!/usr/bin/env python3
"""
Food-Metabolite Correlation Analyzer
AI-driven system to find scientific literature linking foods with metabolites in blood samples
"""

import csv
import json
import os
from typing import List, Dict, Any
import requests
from datetime import datetime

class FoodMetaboliteAnalyzer:
    def __init__(self, foods_file: str = "foods.csv"):
        self.foods_file = foods_file
        self.foods = []
        self.correlations = {}
        self.load_foods()
    
    def load_foods(self):
        """Load foods from CSV file"""
        try:
            with open(self.foods_file, 'r') as file:
                content = file.read().strip()
                # Split by comma and clean up whitespace
                self.foods = [food.strip() for food in content.split(',') if food.strip()]
            print(f"Loaded {len(self.foods)} foods from {self.foods_file}")
        except Exception as e:
            print(f"Error loading foods: {e}")
            self.foods = []
    
    def generate_llama_prompt(self, food: str) -> str:
        """Generate a prompt for Llama to find food-metabolite correlations"""
        prompt = f"""You are a scientific literature researcher specializing in metabolomics and nutritional science. 

Your task is to find ALL scientific papers, research articles, and references that mention the food item "{food}" in correlation with metabolites found in blood (plasma or serum).

Please search for:
1. Positive correlations (increased levels of metabolites when consuming {food})
2. Negative correlations (decreased levels of metabolites when consuming {food})
3. Any significant associations between {food} consumption and blood metabolite levels

For each reference found, provide:
- Full citation (authors, title, journal, year, DOI if available)
- Specific metabolite(s) mentioned
- Type of correlation (positive/negative/association)
- Brief description of the finding
- Relevant quote or sentence from the paper mentioning the correlation

Focus ONLY on blood-based studies (plasma, serum, whole blood) and exclude urine, tissue, or other biospecimens.

Format your response as a structured table with columns:
Reference | Metabolite | Correlation Type | Finding Description | Relevant Quote

Be comprehensive and thorough in your search. If you find multiple metabolites for the same food, list each correlation separately."""
        
        return prompt
    
    def generate_all_prompts(self) -> Dict[str, str]:
        """Generate prompts for all foods"""
        prompts = {}
        for food in self.foods:
            prompts[food] = self.generate_llama_prompt(food)
        return prompts
    
    def save_prompts_to_file(self, output_file: str = "llama_prompts.json"):
        """Save all prompts to a JSON file"""
        prompts = self.generate_all_prompts()
        data = {
            "generated_at": datetime.now().isoformat(),
            "total_foods": len(self.foods),
            "prompts": prompts
        }
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Saved {len(prompts)} prompts to {output_file}")
        return output_file
    
    def create_expert_interface_data(self) -> Dict[str, Any]:
        """Create data structure for the expert interface"""
        interface_data = {
            "foods": [],
            "correlations": {},
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "total_foods": len(self.foods)
            }
        }
        
        for food in self.foods:
            food_entry = {
                "id": len(interface_data["foods"]),
                "name": food,
                "prompt": self.generate_llama_prompt(food),
                "correlations": [],
                "verified": False,
                "expert_notes": ""
            }
            interface_data["foods"].append(food_entry)
        
        return interface_data
    
    def save_interface_data(self, output_file: str = "expert_interface_data.json"):
        """Save interface data for the web application"""
        data = self.create_expert_interface_data()
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Saved interface data to {output_file}")
        return output_file

def main():
    """Main function to run the analyzer"""
    print("Food-Metabolite Correlation Analyzer")
    print("=" * 50)
    
    analyzer = FoodMetaboliteAnalyzer()
    
    if not analyzer.foods:
        print("No foods loaded. Please check your foods.csv file.")
        return
    
    # Generate and save prompts
    prompts_file = analyzer.save_prompts_to_file()
    print(f"Prompts saved to: {prompts_file}")
    
    # Generate interface data
    interface_file = analyzer.save_interface_data()
    print(f"Interface data saved to: {interface_file}")
    
    # Display sample prompt
    if analyzer.foods:
        sample_food = analyzer.foods[0]
        print(f"\nSample prompt for '{sample_food}':")
        print("-" * 50)
        print(analyzer.generate_llama_prompt(sample_food)[:200] + "...")
        print("-" * 50)
    
    print(f"\nTotal foods processed: {len(analyzer.foods)}")
    print("Next steps:")
    print("1. Use the prompts with Llama to generate correlations")
    print("2. Load the results into the expert interface")
    print("3. Have experts verify the correlations")

if __name__ == "__main__":
    main()
