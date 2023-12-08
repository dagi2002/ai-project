from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Abebe')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

# Get a response for some unexpected input
while True:
    request = input('User: ')
    response = chatbot.get_response(request)
    print('Abebe: ', response)
