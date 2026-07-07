import tkinter as tk

from nltk.chat.util import Chat
from nltk.chat.util import reflections

from patterns import pairs

chatbot = Chat(pairs, reflections)

root = tk.Tk()

root.title("AI Chatbot")
root.geometry("500x500")

chat_area = tk.Text(root)
chat_area.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)


def send_message():

    user_message = entry.get()

    chat_area.insert(tk.END, "You: " + user_message + "\n")

    response = chatbot.respond(user_message)

    if response:
        chat_area.insert(tk.END, "Bot: " + response + "\n")
    else:
        chat_area.insert(tk.END, "Bot: Sorry, I don't understand.\n")

    entry.delete(0, tk.END)


send_button = tk.Button(root, text="Send", command=send_message)

send_button.pack()

root.mainloop()