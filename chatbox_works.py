import json 
import random 
import time 
def greet_user():
    user_name=input("enter your name: ")
    print(f"Konichiwa {user_name}.welcome to the noobworld")
    return user_name

def agent_load():
    with open('json.json') as file:
        data = json.load(file)
        return data["agents"]
                
def agent_display(agents):
    print("choose your companian to guide through this journey:")
    for idx, agent in enumerate(agents, 1):
        print(f"{idx}. {agent}")
    print("4. Random agent")

def agent_select(agents):
    agent_display(agents)
    while True:
        choice=input("enter your choice(1,2,3,4):")
        if choice == '1':
            print("Ventress selected")
            return "Ventress"
        elif choice == '2':
            print("Kane selected")
            return "Kane"
        elif choice == '3':
              print("Lena selected")
              return"Lena"
        elif choice == '4':
             random_agent = random.choice(agents)
             print(f"Randomly selected agent: {random_agent}")
             return random_agent
        else:
             print("Invalid choice, please try again.")
            
        
def save_chat(user_name,agent,user_in):
    with open('json.json') as file:
        data=json.load(file)
        replies =data["reply"][agent]

    with open("chat_log.txt","a") as log_file:
        log_file.write(f"__history with {agent}\n")
        print(f"\n{agent}:Yo gang I'm here to vibe with you,{user_name}.To end the chat type 'sayonara'\n.")
        log_file.write(f"{user_name}:{user_in}\n")

def end_chat(user_name,agent,log_file):
        print(f"{agent}:Sayonara,{user_name}<3 let's catch up next time.")
        log_file.write(f"{agent}:sayonara,{user_name}\n")
    

def reply(agent,log_file,user_in,user_name):
    with open('json.json') as file:
        data = json.load(file)
        replies = data["reply"].get(agent, {})

    if user_in in replies:
        reply=replies[user_in]
        print(f"{agent}:{reply}")
        log_file.write(f"{agent}:{reply}\n")
    else:
        ran_reply=[
            f"{agent}: Gang I have no idea what you just said",
            f"{agent}: that's lowkie interesting {user_name}.tell me abt it "

        ]
        agent_reply = random.choice(ran_reply)
        print(agent_reply)
        log_file.write(f"{agent}:{agent_reply}")

def chatbox():
    user_name = greet_user()
    agents=agent_load()
    agent=agent_select(agents)
   

    with open("chat_log.txt", "a") as log_file:  # Open the chat log file
        while True:  # Start the conversation loop
            user_in = input(f"{user_name}: ")  # Get user input
            if user_in in ["sayonara", "bye", "exit", "quit"]:  # Check if user wants to end chat
                end_chat(user_name, agent, log_file)  # End the chat
                break  # Exit the loop and stop the conversation
            else:
                reply(agent,log_file,user_in,user_name)

if __name__ == "__main__":
    chatbox()
   