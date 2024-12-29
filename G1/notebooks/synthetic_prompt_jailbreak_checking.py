from transformers import GPT2Tokenizer, GPT2Model, GPT2ForSequenceClassification
import torch
import torch.nn.functional as F

# Load GPT-2 model and tokenizer for sequence classification
model_name = "gpt2"  # General pretrained GPT-2
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2ForSequenceClassification.from_pretrained(model_name, num_labels=2)  # Binary classification
model.eval()

# Add padding token if missing (GPT-2 doesn't have one by default)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Load synthetic prompts from file
synthetic_prompt_file = "synthetic_prompt.txt"
with open(synthetic_prompt_file, "r") as file:
    prompts = file.readlines()

# Classify each prompt and count jailbreaking prompts
total_prompts = len(prompts)
jailbreaking_count = 0

# Iterate through prompts and classify
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

# Print results
print(f"Total Prompts: {total_prompts}")
print(f"Jailbreaking Prompts: {jailbreaking_count}")
print(f"Percentage of Jailbreaking Prompts: {jailbreaking_percentage:.2f}%")

# Save results to a file
output_file = "classified_prompts_gpt2.txt"
with open(output_file, "w") as out_file:
    for prompt, label in results:
        label_text = "Jailbreaking" if label == 1 else "Not Jailbreaking"
        out_file.write(f"{prompt}\t{label_text}\n")

print(f"Classified prompts saved to {output_file}")