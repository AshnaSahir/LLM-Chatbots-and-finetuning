#implementation of a chatbot that provides information about Dubai. 
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import openai

app = Flask(__name__)
socketio = SocketIO(app)

# Set your OpenAI API key here
openai.api_key = 'enter your open ai key here'

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    user_input = data['message']
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
      {"role": "system", "content": "You are a helpful assistant to provide any sort of information about Dubai. Your name is DubaiBot. If you are asked about anything outside Dubai, you can answer that you are here to only answer questions about Dubai. You have knowledge about Visas in Dubai, Living expenses and conditions etc. If you don't have the answer to any question, you can say that this is currently beyond your knowledge and that the user can rely on a web search for the answer.  "},
      {"role": "user", "content": user_input}
   ]
    ).choices[0].message.content
    emit('receive_message', {'user_message': user_input, 'bot_message': response})

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5002)


