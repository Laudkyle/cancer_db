import json

with open('combined_intents.json') as f:
    data = json.load(f)


intents = data['intents']

all_intents = []
temp_tags=[]

for int_ in intents:
    tag = int_["tag"]
    temp_tags.append(tag)

temp_tag = set(temp_tags)

for int_ in intents:
    tag = int_["tag"]
    pattern = int_["patterns"]
    responses = int_["responses"]

    if tag in temp_tag:
        all_intents.append(int_)
        temp_tag.remove(tag)
    else:
        continue

# Create a dictionary with all intents
intent_data = {"intents": all_intents}

# Save the combined intents to a single JSON file
output_filename = "combined_intents_filtered.json"
with open(output_filename, "w") as outfile:
    json.dump(intent_data, outfile, indent=4)

print(f"Combined intents saved to '{output_filename}'")

