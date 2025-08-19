#!/usr/bin/env python3
"""
Script to fix the corrupted expert_interface_data.json and regenerate it with proper structure
"""

import json
import os
from typing import List, Dict, Any

def create_comprehensive_correlations(food_name: str) -> List[Dict[str, Any]]:
    """Create comprehensive correlations with honest data structure"""
    
    # Comprehensive list of metabolites and their effects
    metabolites_data = [
        # Positive correlations (beneficial effects)
        ("Vitamin C (Ascorbic Acid)", "Positive", f"Increased plasma vitamin C levels after {food_name} consumption", f"Consumption of {food_name} led to a significant increase in plasma vitamin C concentrations (p<0.001)"),
        ("Beta-carotene", "Positive", f"Elevated beta-carotene levels in serum following {food_name} intake", f"Serum beta-carotene levels were 2.8-fold higher in participants consuming {food_name} compared to controls"),
        ("Folate", "Positive", f"Improved folate status in blood after {food_name} supplementation", f"Blood folate concentrations increased by 33% following regular {food_name} consumption"),
        ("Vitamin E (Alpha-tocopherol)", "Positive", f"Higher vitamin E levels in plasma after {food_name} consumption", f"Plasma vitamin E levels were significantly elevated (p<0.01) after {food_name} intake"),
        ("Polyphenols", "Positive", f"Increased polyphenol metabolites in blood following {food_name} consumption", f"Blood polyphenol metabolite levels increased by 2.5-fold after {food_name} consumption"),
        ("Vitamin K1 (Phylloquinone)", "Positive", f"Elevated vitamin K1 levels in serum after {food_name} intake", f"Serum vitamin K1 concentrations were 2.2-fold higher in {food_name} consumers"),
        ("Minerals (Potassium, Magnesium)", "Positive", f"Improved mineral status in blood after {food_name} consumption", f"Blood potassium and magnesium levels increased by 25% following {food_name} supplementation"),
        ("Antioxidant capacity", "Positive", f"Higher antioxidant capacity in plasma after {food_name} intake", f"Plasma antioxidant capacity was significantly elevated (p<0.05) after {food_name} consumption"),
        ("Fiber metabolites", "Positive", f"Improved fiber metabolite status in blood after {food_name} consumption", f"Blood fiber metabolite levels increased by 27% following regular {food_name} intake"),
        ("Phytochemicals", "Positive", f"Elevated phytochemical levels in serum after {food_name} consumption", f"Serum phytochemical levels were 2.6-fold higher in {food_name} consumers compared to non-consumers"),
        ("Lutein", "Positive", f"Increased lutein levels in plasma after {food_name} consumption", f"Plasma lutein concentrations were 3.1-fold higher in {food_name} consumers"),
        ("Zeaxanthin", "Positive", f"Elevated zeaxanthin levels in serum following {food_name} intake", f"Serum zeaxanthin levels increased by 2.9-fold after {food_name} consumption"),
        ("Lycopene", "Positive", f"Higher lycopene levels in blood after {food_name} consumption", f"Blood lycopene levels were significantly elevated (p<0.001) after {food_name} intake"),
        ("Quercetin", "Positive", f"Increased quercetin metabolites in plasma after {food_name} consumption", f"Plasma quercetin levels increased by 2.7-fold following {food_name} intake"),
        ("Resveratrol", "Positive", f"Elevated resveratrol levels in serum after {food_name} consumption", f"Serum resveratrol concentrations were 2.4-fold higher in {food_name} consumers"),
        ("Anthocyanins", "Positive", f"Higher anthocyanin levels in blood after {food_name} consumption", f"Blood anthocyanin levels increased by 3.2-fold after {food_name} intake"),
        ("Flavonoids", "Positive", f"Increased flavonoid metabolites in plasma after {food_name} consumption", f"Plasma flavonoid levels were significantly elevated (p<0.01) after {food_name} intake"),
        ("Carotenoids", "Positive", f"Elevated carotenoid levels in serum after {food_name} consumption", f"Serum carotenoid levels increased by 2.8-fold following {food_name} consumption"),
        ("Tocopherols", "Positive", f"Higher tocopherol levels in blood after {food_name} consumption", f"Blood tocopherol levels were 2.5-fold higher in {food_name} consumers"),
        ("Selenium", "Positive", f"Increased selenium levels in plasma after {food_name} consumption", f"Plasma selenium concentrations increased by 31% after {food_name} intake"),
        
        # Negative correlations (reduced adverse markers)
        ("Oxidative stress markers", "Negative", f"Reduced oxidative stress markers in blood after {food_name} consumption", f"Blood malondialdehyde levels decreased by 18% following regular {food_name} intake"),
        ("Inflammatory cytokines", "Negative", f"Lower inflammatory cytokine levels in plasma after {food_name} intake", f"Plasma IL-6 and TNF-alpha levels were significantly reduced (p<0.05) after {food_name} consumption"),
        ("LDL cholesterol", "Negative", f"Decreased LDL cholesterol levels in serum after {food_name} consumption", f"Serum LDL cholesterol concentrations were 12% lower in {food_name} consumers"),
        ("Blood pressure markers", "Negative", f"Reduced blood pressure-related metabolites after {food_name} intake", f"Plasma angiotensin II levels decreased by 15% following {food_name} consumption"),
        ("Glucose metabolism markers", "Negative", f"Improved glucose metabolism markers after {food_name} consumption", f"Fasting glucose levels were 8% lower in {food_name} consumers"),
        ("Advanced glycation end products", "Negative", f"Reduced advanced glycation end products in blood after {food_name} intake", f"Blood AGE levels decreased by 22% following regular {food_name} consumption"),
        ("Homocysteine", "Negative", f"Lower homocysteine levels in plasma after {food_name} consumption", f"Plasma homocysteine concentrations were 16% reduced in {food_name} consumers"),
        ("C-reactive protein", "Negative", f"Decreased C-reactive protein levels after {food_name} intake", f"Serum CRP levels were significantly lower (p<0.01) in {food_name} consumers"),
        ("Uric acid", "Negative", f"Reduced uric acid levels in blood after {food_name} consumption", f"Blood uric acid concentrations decreased by 14% following {food_name} intake"),
        ("Triglycerides", "Negative", f"Lower triglyceride levels in plasma after {food_name} consumption", f"Plasma triglyceride levels were 11% reduced in {food_name} consumers"),
        ("Insulin resistance markers", "Negative", f"Improved insulin sensitivity markers after {food_name} consumption", f"Homeostatic model assessment (HOMA) scores decreased by 19% following {food_name} intake"),
        ("Endothelial dysfunction markers", "Negative", f"Reduced endothelial dysfunction markers after {food_name} consumption", f"Plasma endothelin-1 levels decreased by 13% following {food_name} intake"),
        ("Pro-inflammatory markers", "Negative", f"Lower pro-inflammatory markers after {food_name} consumption", f"Plasma prostaglandin E2 levels decreased by 17% following {food_name} intake"),
        ("Oxidative DNA damage", "Negative", f"Reduced oxidative DNA damage markers after {food_name} consumption", f"8-hydroxy-2'-deoxyguanosine levels decreased by 21% following {food_name} intake"),
        ("Lipid peroxidation", "Negative", f"Lower lipid peroxidation markers after {food_name} consumption", f"Plasma thiobarbituric acid reactive substances decreased by 16% following {food_name} intake"),
        ("Nitric oxide inhibitors", "Negative", f"Reduced nitric oxide inhibitors after {food_name} consumption", f"Plasma asymmetric dimethylarginine levels decreased by 14% following {food_name} intake"),
        ("Adipokine imbalance", "Negative", f"Improved adipokine balance after {food_name} consumption", f"Plasma leptin/adiponectin ratio decreased by 12% following {food_name} intake"),
        ("Cellular stress markers", "Negative", f"Reduced cellular stress markers after {food_name} consumption", f"Plasma heat shock protein 70 levels decreased by 15% following {food_name} intake"),
        ("Metabolic endotoxemia", "Negative", f"Lower metabolic endotoxemia markers after {food_name} consumption", f"Plasma lipopolysaccharide levels decreased by 18% following {food_name} intake"),
        ("Advanced oxidation protein products", "Negative", f"Reduced advanced oxidation protein products after {food_name} consumption", f"Plasma AOPP levels decreased by 20% following {food_name} intake")
    ]
    
    correlations = []
    
    # Generate correlations with honest data structure
    for i, (metabolite, corr_type, finding, quote) in enumerate(metabolites_data):
        correlation = {
            "reference": f"Example correlation {i+1} - {metabolite}",
            "reference_link": None,  # No fake links
            "doi": None,  # No fake DOIs
            "metabolite": metabolite,
            "correlationType": corr_type,
            "finding": finding,
            "relevantQuote": quote,
            "verified": None,
            "expertNotes": "",
            "data_source": "Generated example data for demonstration purposes"
        }
        correlations.append(correlation)
    
    return correlations

def load_foods_list() -> List[str]:
    """Load the list of foods from foods.csv"""
    try:
        with open('foods.csv', 'r') as f:
            content = f.read().strip()
            # Parse the comma-separated food list
            foods = [food.strip() for food in content.split(',') if food.strip()]
            return foods
    except FileNotFoundError:
        # Fallback food list if CSV is not available
        return [
            "broccoli", "cabbage", "coleslaw", "cauliflower", "brussels sprouts",
            "kale", "mustard greens", "chard", "spinach", "romaine",
            "leaf lettuce", "tomatoes", "carrots", "orange winter squash", "celery",
            "peppers", "onions", "eggplant", "zucchini", "summer squash",
            "mixed vegetables", "iceberg", "head lettuce", "string beans", "corn",
            "yams", "sweet potatoes", "peas", "lima beans", "potatoes", "beans",
            "lentils", "soy foods", "tofu", "soybeans", "soy milk", "oranges",
            "grapefruits", "blueberries", "strawberries", "apples", "pears",
            "prunes", "peaches/plums", "apricots", "grapes", "raisins",
            "bananas", "cantaloupe", "avocado", "bran", "dark bread",
            "whole grain bread", "rye", "pumpernickel bread", "brown rice",
            "cold breakfast cereal", "other cooked cereal", "oatmeal", "popcorn",
            "white bread", "white rice", "crackers", "other refined grains",
            "pasta", "tortillas", "pretzels", "pancakes", "waffles",
            "English muffins", "bagels", "rolls", "muffins", "biscuits",
            "peanuts", "peanut butter", "walnuts", "other nuts", "beef",
            "pork hotdogs", "bacon", "salami", "bologna", "processed meats",
            "lean hamburgers", "extra lean hamburgers", "regular hamburgers",
            "beef, pork, lamb sandwich", "beef as a main dish", "lamb as a main dish",
            "pork as a main dish", "chicken hotdogs", "turkey hotdogs",
            "chicken sandwich", "turkey sandwich", "frozen dinner",
            "chicken with skin", "turkey with skin", "chicken without skin",
            "turkey without skin", "dark meat fish", "canned tuna",
            "breaded fish pieces", "other fish", "shrimp", "lobster",
            "scallops", "whole eggs", "omega-3 fortified eggs", "candy",
            "dark chocolate", "milk chocolate", "jam", "jelly",
            "non-dairy dessert", "cookies", "brownies", "sweetroll",
            "pie", "doughnuts", "cakes", "olive oil", "other vegetable oils",
            "tea", "herbal tea", "coffee", "decaffeinated coffee",
            "red wine", "white wine", "beer", "light beer", "liquor",
            "low-calorie beverages with caffeine", "low-calorie beverages without caffeine",
            "carbonated beverages with sugar", "other sugared beverages",
            "punch", "fruit juice", "breakfast bars", "energy bars",
            "low-carb bars", "chicken liver", "turkey liver"
        ]

def regenerate_expert_interface_data():
    """Regenerate the expert_interface_data.json with proper structure"""
    
    print("Loading foods list...")
    foods = load_foods_list()
    print(f"Found {len(foods)} foods")
    
    # Create the proper data structure
    data = {
        "foods": [],
        "metadata": {
            "created_at": "2025-08-19T12:00:00Z",
            "total_foods": len(foods),
            "total_correlations": len(foods) * 40,  # 40 correlations per food (20 positive + 20 negative)
            "correlation_types": ["Positive", "Negative"],
            "data_source": "Example correlations for demonstration purposes - NOT real scientific data",
            "reference_count": 40,
            "metabolite_count": 40,
            "disclaimer": "This data is generated for demonstration purposes. Real scientific references should be added by researchers."
        }
    }
    
    print("Generating comprehensive correlations for each food...")
    for i, food_name in enumerate(foods):
        food_data = {
            "id": i,
            "name": food_name,
            "prompt": f"Find correlations between {food_name} consumption and blood metabolites",
            "correlations": create_comprehensive_correlations(food_name),
            "verified": False,
            "expertNotes": ""
        }
        data["foods"].append(food_data)
        
        if (i + 1) % 10 == 0:
            print(f"Processed {i + 1}/{len(foods)} foods...")
    
    # Save the regenerated data
    output_file = "expert_interface_data.json"
    print(f"Saving regenerated data to {output_file}...")
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Successfully regenerated {output_file}")
    print(f"📊 Total foods: {len(data['foods'])}")
    print(f"🔬 Total correlations: {data['metadata']['total_correlations']}")
    print(f"📈 Correlation types: {', '.join(data['metadata']['correlation_types'])}")
    print(f"📚 Correlations per food: {data['metadata']['reference_count']}")
    print(f"🧬 Metabolites per food: {data['metadata']['metabolite_count']}")
    print(f"⚠️  IMPORTANT: This is example data for demonstration purposes")
    print(f"📝 Real scientific references should be added by researchers")
    
    return data

if __name__ == "__main__":
    print("🔄 Regenerating expert_interface_data.json with honest data structure...")
    print("=" * 70)
    
    try:
        data = regenerate_expert_interface_data()
        print("\n🎉 Data regeneration completed successfully!")
        print("\nNext steps:")
        print("1. Commit the updated file: git add expert_interface_data.json")
        print("2. Push to GitHub: git push origin master")
        print("3. The HTML will now show honest data without fake links")
        print("4. GitHub Pages will automatically update")
        
    except Exception as e:
        print(f"❌ Error during regeneration: {e}")
        import traceback
        traceback.print_exc()
