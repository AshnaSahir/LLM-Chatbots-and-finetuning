This is a repository containing 3 chatbot projects. 
  1. A basic chatbot implemented with Falcon LLM (Using GPT4All, Nomic AI) - file name: ashbot.py
     
     <img width="481" alt="image" src="https://github.com/AshnaSahir/LLM-Chatbots-and-finetuning/assets/164536293/c7d78390-989b-43fd-bafe-abeecd5a92f1">

  2. A Dubai Assistant chatbot implemented with Open AI API, prompt engineered to provide information regarding anything in Dubai beneficial for tourists, expats and locals. The chatbot can also communicate in Arabic - file names: app.py and index.html
     
     <img width="663" alt="image" src="https://github.com/AshnaSahir/LLM-Chatbots-and-finetuning/assets/164536293/a910bed1-4a86-4b7b-9ba9-5261a371084d">

  3. An ecommerce chatbot, implemented by finetuning the Microsoft Dialogpt - small model with an ecommerce data set (ecommercedataset.txt). file names: ashbot2.py and trainset.py
     
     <img width="845" alt="image" src="https://github.com/AshnaSahir/LLM-Chatbots-and-finetuning/assets/164536293/3e5ef198-5457-4bb7-9c7c-9c2de850f821">

Usage Guidelines:

1. For the first project I have used Falcon LLM from GPT4All. In case you want to try a different model, you can include the respective .gguf model file. This chatbot currently runs only in the terminal. 
2. For the second project, you have to create an Open AI account and use your API key in the app.py file. This project uses flask to run the server and requires the index.html within templates folder to render the front end. This has also been prompt engineered to make it specefic for a Dubai Assistant Chatbot, you can adjust it in app.py based on your requirement.
3. For the third project, I have used a small model dialogpt for finetuning based on an ecommercedataset I generated. I selected this model because it requires minimal resources to finetune. If your system has the resources, you can use the same code to finetune a larger model using the trainset.py file.
