from nltk.chat.util import Chat
from nltk.chat.util import reflections

from patterns import pairs

name = input("Enter your name: ")

print(f"Welcome {name}")

chatbot = Chat(pairs, reflections)

while True:

    user = input("You : ")

    if user.lower() == "quit":
        print(f"Goodbye {name}!")
        break

    response = chatbot.respond(user)

    if response:
        print("Bot :", response)

    else:
        print(f"Bot : Sorry {name}, I don't understand.")