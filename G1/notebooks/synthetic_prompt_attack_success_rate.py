from transformers import GPT2Tokenizer, GPT2ForSequenceClassification, AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Function to classify prompts for a given model and tokenizer
def classify_prompts(model_name, tokenizer_name, num_labels, prompts, output_file):
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)
    model.eval()

    # Add padding token if missing (for GPT-2-like models)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Classify each prompt
    total_prompts = len(prompts)
    jailbreaking_count = 0
    results = []

    for prompt in prompts:
        # Tokenize prompt
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True, max_length=512)

        # Get model predictions
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            probabilities = F.softmax(logits, dim=1)
            predicted_class = torch.argmax(probabilities, dim=1).item()
            results.append((prompt.strip(), predicted_class))

            # Count jailbreaking prompts
            if predicted_class == 1:
                jailbreaking_count += 1

    # Calculate percentage of jailbreaking prompts
    jailbreaking_percentage = (jailbreaking_count / total_prompts) * 100

    # Save results to a file
    with open(output_file, "w") as out_file:
        for prompt, label in results:
            label_text = "Jailbreaking" if label == 1 else "Not Jailbreaking"
            out_file.write(f"{prompt}\t{label_text}\n")

    # Print results
    print(f"Model: {model_name}")
    print(f"Total Prompts: {total_prompts}")
    print(f"Jailbreaking Prompts: {jailbreaking_count}")
    print(f"Percentage of Jailbreaking Prompts: {jailbreaking_percentage:.2f}%")
    print(f"Classified prompts saved to {output_file}")

    return jailbreaking_percentage


# Load synthetic prompts
synthetic_prompt_file = "synthetic_prompt.txt"
with open(synthetic_prompt_file, "r") as file:
    prompts = file.readlines()

# Run classification for each model
models = [
    {
        "model_name": "bert-base-uncased",
        "tokenizer_name": "bert-base-uncased",
        "num_labels": 2,
        "output_file": "classified_prompts_bert.txt",
    },
    {
        "model_name": "Xenova/gpt-3.5-turbo",
        "tokenizer_name": "Xenova/gpt-3.5-turbo",
        "num_labels": 2,
        "output_file": "classified_prompts_gpt-3.5-turbo.txt",
    },
    {
        "model_name": "meta-llama/Llama-3.2-1B",
        "tokenizer_name": "meta-llama/Llama-3.2-1B",
        "num_labels": 2,
        "output_file": "classified_prompts_llama-3.2-1B.txt",
    },
]

# Iterate through models
for model_config in models:
    print(f"\nRunning classification for {model_config['model_name']}...")
    classify_prompts(
        model_config["model_name"],
        model_config["tokenizer_name"],
        model_config["num_labels"],
        prompts,
        model_config["output_file"],
    )
