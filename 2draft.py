import random
import json
import tkinter as tk
from tkinter import scrolledtext

# Load responses from a JSON file
responses = {
    "coffee": "The campus coffee bar is open from 8 AM to 6 PM.",
    "library": "The library is open from 9 AM to 9 PM.",
    "sports": "The sports center is open from 7 AM to 10 PM.",
    "admissions": "Admissions office is open from 9 AM to 5 PM."
}

# Random agent names
agent_names = ["Alex", "Taylor", "Jordan", "Morgan", "Jamie"]

# Random fallback responses
random_responses = [
    "I'm not sure about that.",
    "Can you rephrase your question?",
    "I'll need to check on that.",
    "Hmm, that's a tricky one."
]

# Function to respond to user questions
def respond_to_question(question):
    for keyword, response in responses.items():
        if keyword in question.lower():
            return response
    return random.choice(random_responses)

# Function to handle sending a message
def send_message():
    user_input = input_box.get()
    input_box.delete(0, tk.END)
    
    if user_input.lower() in ["bye", "exit", "quit"]:
        chat_area.insert(tk.END, f"You: {user_input}\n")
        chat_area.insert(tk.END, f"{agent_name}: Goodbye! Have a great day.\n")
        root.quit()
    else:
        chat_area.insert(tk.END, f"You: {user_input}\n")
        response = respond_to_question(user_input)
        chat_area.insert(tk.END, f"{agent_name}: {response}\n")

# Initialize the Tkinter window
root = tk.Tk()
root.title("University of Poppleton Chatbot")

# Randomly select an agent name
agent_name = random.choice(agent_names)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_area.pack(pady=10)

input_box = tk.Entry(root, width=50, font=("Arial", 12))
input_box.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

# Display initial greeting
chat_area.insert(tk.END, f"You're now chatting with {agent_name}.\n")

# Start the Tkinter event loop
root.mainloop()
