#chatbot 2 with fintuned model - this model was tuned specifically for an ecommerce chatbot
#the script to fintune is trainset.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Assuming the 'fine_tuned_model' directory is in the current working directory
model_path = "fine_tuned_model"

# Load the fine-tuned model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Function to chat with the chatbot
def chat(model, tokenizer):
    chat_history_ids = None
    print("Chatbot ready! Start talking to the chatbot by typing below (type 'quit' to stop):")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'quit':
            break
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        
        # Append user input to chat history
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids
        
        # Generate a response
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        
        # Get the response text
        response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        print(f"Chatbot: {response}")

# Start chatting
chat(model, tokenizer)
