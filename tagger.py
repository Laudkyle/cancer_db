import json
import os

data = {
    "questions": [
 {
      "question": "What are the treatment options for breast cancer?",
      "answer": "Treatment options for breast cancer include surgery, radiation therapy, chemotherapy, hormone therapy, targeted therapy, and immunotherapy. The choice of treatment depends on several factors, including the stage and type of breast cancer, as well as the patient's overall health and preferences."
    },   {
      "question": "What are the primary treatments for breast cancer?",
      "answer": "The primary treatments for breast cancer include surgery, radiation therapy, chemotherapy, hormone therapy, and targeted therapy. Treatment plans are individualized based on the type and stage of breast cancer, as well as the patient's overall health and preferences."
    },    {
      "question": "Are there alternative treatments for breast cancer?",
      "answer": "While conventional treatments like surgery, radiation therapy, and chemotherapy are standard for breast cancer, some patients explore alternative or complementary therapies such as acupuncture, herbal supplements, or dietary changes. It's essential to discuss these options with healthcare providers."
    }, {
      "question": "How is breast cancer treated?",
      "answer": "Breast cancer treatment varies based on the stage and type of cancer. Common treatments include surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy. Treatment plans are often tailored to individual patients to achieve the best possible outcomes."
    },
    {
      "question": "What are the treatment options for breast cancer?",
      "answer": "Treatment options for breast cancer include surgery to remove the tumor, chemotherapy to kill cancer cells, radiation therapy to destroy cancer cells, hormone therapy to block the effects of hormones that fuel cancer growth, and targeted therapy to attack specific cancer cells."
    },
    {
      "question": "How do doctors treat breast cancer?",
      "answer": "Doctors treat breast cancer using a combination of therapies, which may include surgery, radiation, chemotherapy, hormone therapy, and targeted therapy. The choice of treatment depends on the type and stage of the cancer, as well as the patient's overall health."
    },
    {
      "question": "What are the common treatments for breast cancer?",
      "answer": "Common treatments for breast cancer include surgery to remove the tumor, chemotherapy to kill cancer cells, radiation therapy to destroy cancer cells, hormone therapy to block the effects of hormones that fuel cancer growth, and targeted therapy to attack specific cancer cells."
    },
    {
      "question": "How is breast cancer usually treated?",
      "answer": "Breast cancer is usually treated with a combination of surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy. The specific treatment plan depends on the type of breast cancer, its stage, and the patient's overall health."
    },
    {
      "question": "What are the main treatments for breast cancer?",
      "answer": "The main treatments for breast cancer include surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy. These treatments can be used alone or in combination, depending on the type and stage of the cancer."
    },
    {
      "question": "How do oncologists treat breast cancer?",
      "answer": "Oncologists treat breast cancer using a variety of methods, including surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy. The choice of treatment depends on the specific type and stage of the cancer, as well as the patient's overall health."
    },
    {
      "question": "What are the standard treatments for breast cancer?",
      "answer": "The standard treatments for breast cancer include surgery to remove the tumor, chemotherapy to kill cancer cells, radiation therapy to destroy cancer cells, hormone therapy to block the effects of hormones that fuel cancer growth, and targeted therapy to attack specific cancer cells."
    },
     {
      "question": "What are the available treatments for breast cancer?",
      "answer": "Available treatments for breast cancer include surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy. These treatments can be used alone or in combination, depending on the type and stage of the cancer."
    },
    {
      "question": "How do you treat breast cancer?",
      "answer": "Breast cancer is treated using surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy. The treatment plan depends on the type and stage of the cancer."
    },
    {
      "question": "What treatments are used for breast cancer?",
      "answer": "Treatments for breast cancer include surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy. These treatments may be used alone or in combination."
    },
    {
      "question": "What are the ways to treat breast cancer?",
      "answer": "Breast cancer can be treated with surgery to remove the tumor, chemotherapy to kill cancer cells, radiation therapy to destroy cancer cells, hormone therapy to block hormone effects, and targeted therapy to attack specific cancer cells."
    },
    {
      "question": "How is breast cancer managed?",
      "answer": "Breast cancer is managed with a combination of treatments like surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy, tailored to the individual's condition."
    },
    {
      "question": "What are the main ways to treat breast cancer?",
      "answer": "The main ways to treat breast cancer include surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy, with the treatment choice depending on the cancer type and stage."
    },
    {
      "question": "How is breast cancer controlled?",
      "answer": "Breast cancer is controlled through treatments like surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy, aimed at eliminating or reducing the cancer cells."
    },
    {
      "question": "How do you manage breast cancer?",
      "answer": "Breast cancer is managed through various treatments such as surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy, chosen based on the cancer's characteristics."
    },
    {
      "question": "What treatments do doctors use for breast cancer?",
      "answer": "Doctors use treatments like surgery, chemotherapy, radiation therapy, hormone therapy, and targeted therapy to treat breast cancer, selecting the best options based on the patient's condition."
    },
    {
      "question": "What are the common ways to treat breast cancer?",
      "answer": "Common ways to treat breast cancer include surgery to remove the tumor, chemotherapy to kill cancer cells, radiation therapy to destroy cancer cells, hormone therapy to block hormone effects, and targeted therapy to attack specific cancer cells."
    },
    {
      "question": "How do you handle breast cancer?",
      "answer": "Breast cancer is handled using treatments such as surgery to remove the tumor, chemotherapy to kill cancer cells, radiation therapy to destroy cancer cells, hormone therapy to block hormone effects, and targeted therapy to attack specific cancer cells."
    },
    ]
}

intents = {
    "intents": [
        {
            "tag": "How is breast cancer treated",
            "patterns": [q["question"] for q in data["questions"]],
            "responses": [q["answer"] for q in data["questions"]]
        }
    ]
}

# Define the file path
file_path = "intents.json"

# Check if the file exists
if os.path.exists(file_path):
    # Load existing data from the file
    with open(file_path, "r") as infile:
        existing_data = json.load(infile)
    
    # Append the new data to the existing data
    existing_data["intents"].extend(intents["intents"])
    
    # Write the combined data back to the file
    with open(file_path, "w") as outfile:
        json.dump(existing_data, outfile, indent=4)
else:
    # If the file doesn't exist, create a new one with the combined data
    with open(file_path, "w") as outfile:
        json.dump(intents, outfile, indent=4)

print(f"Data combined and appended to '{file_path}'.")
