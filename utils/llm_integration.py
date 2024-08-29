from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
model_name = "EleutherAI/gpt-j-6B"  # Example model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model = model.to('cuda')  # Ensure CUDA is available, or use 'cpu' if not

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
    outputs = model.generate(inputs["input_ids"], max_length=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
