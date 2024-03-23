import json
import os

# Directory containing the JSON files
directory = "datasets"

# List to store all questions
all_questions = []

# Iterate over each JSON file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        questions = [qa["question"] for qa in data["questions"]]
        all_questions.extend(questions)

# Save the combined questions to a text file
output_filename = "extracted_questions.txt"
with open(output_filename, "w") as outfile:
    for question in all_questions:
        outfile.write(f"{question}\n")

print(f"Extracted questions saved to '{output_filename}'")
