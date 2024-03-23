import json
import os

def convert_to_intent_format(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    questions = data["questions"]

    qa_dict = {}

    for qa in questions:
        question = qa["question"]
        answer = qa["answer"]
        
        if question not in qa_dict:
            qa_dict[question] = [answer]
        else:
            qa_dict[question].append(answer)

    intents = []
    for counter, (question, answers) in enumerate(qa_dict.items(), 1):
        tag = counter
        patterns = [question]
        responses = answers
        intent = {
            "tag": tag,
            "patterns": patterns,
            "responses": responses
        }
        intents.append(intent)

    return intents

# Directory containing the JSON files
directory = "datasets"

# List to store all intents from all JSON files
all_intents = []

# Iterate over each JSON file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        filepath = os.path.join(directory, filename)
        intents = convert_to_intent_format(filepath)
        all_intents.extend(intents)

# Create a dictionary with all intents
intent_data = {"intents": all_intents}

# Save the combined intents to a single JSON file
output_filename = "combined_intents.json"
with open(output_filename, "w") as outfile:
    json.dump(intent_data, outfile, indent=4)

print(f"Combined intents saved to '{output_filename}'")
