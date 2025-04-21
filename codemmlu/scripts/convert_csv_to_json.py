import csv
import json
import os

def convert_csv_to_json(csv_path, json_path):
    # Dictionary to store the results
    results = {}
    
    # Read CSV file
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            model_name = row['model'].strip()
            
            # Create model entry
            model_entry = {
                "link": model_name,
                "open-data": "None",
                "pass@1": {
                    "instruct": None,
                    "complete": float(row['codemmlu'])
                },
                "realtask_accuracy": float(row['fundamental']),
                "syntactic_accuracy": float(row['syntatic']),
                "semantic_accuracy": float(row['semantic']),
                "prompted": True,  # Instruction models
                "size": float(row['size']) if row['size'] else None,
                "direct_complete": False,
                "lazy": False,
                "elo_mle": 874
            }
            
            results[model_name] = model_entry
    
    # Write JSON file
    with open(json_path, 'w') as json_file:
        json.dump(results, json_file, indent=4)

def main():
    # Get the absolute path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct paths relative to the script directory
    csv_path = os.path.join(script_dir, '..', 'static', 'data', 'CodeMMLU_update_res.csv')
    json_path = os.path.join(script_dir, '..', 'static', 'data', 'updated_results.json')
    
    # Convert CSV to JSON
    convert_csv_to_json(csv_path, json_path)
    print(f"Conversion complete. JSON file saved to: {json_path}")

if __name__ == "__main__":
    main() 