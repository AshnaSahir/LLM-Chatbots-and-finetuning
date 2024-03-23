# implementation of a chatbot using GPT4ALL falcon model
from gpt4all import GPT4All

model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf")
#model = GPT4All("model.safetensors")

print("Hi, How can I help you? Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    output = model.generate(user_input, max_tokens=200)
    print("Bot:", output)
