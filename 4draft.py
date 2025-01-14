import json
import random
import time
import datetime

def greet_user():
    user_name = input("enter your name: ")
    print(f"Konichiwa {user_name}.welcome to the noobworld")
    return user_name

def agent_load(filepath="json.json"):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["agents"], data.get("reply", {}) #Handle missing "reply" key in JSON
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return [], {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filepath}'.")
        return [], {}

def agent_display(agents):
    print("choose your companian to guide through this journey:")
    for idx, agent in enumerate(agents, 1):
        print(f"{idx}. {agent}")
    print("4. Random agent")

def agent_select(agents):
    agent_display(agents)
    while True:
        choice = input("enter your choice(1,2,3,4):")
        try:
            choice_num = int(choice) #Convert input to integer for comparison
            if 1 <= choice_num <= len(agents):
                print(f"{agents[choice_num - 1]} selected")
                return agents[choice_num - 1]
            elif choice_num == 4:
                random_agent = random.choice(agents)
                print(f"Randomly selected agent: {random_agent}")
                return random_agent
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please try again.")

def reply(agent, replies, user_in, user_name):
    if user_in in replies.get(agent, {}):
        agent_reply = replies[agent][user_in]
        print(f"{agent}:{agent_reply}")
        return agent_reply #Return the reply for logging
    else:
        ran_reply = [
            f"{agent}: Gang I have no idea what you just said",
            f"{agent}: that's lowkie interesting {user_name}.tell me abt it "
        ]
        agent_reply = random.choice(ran_reply)
        print(agent_reply)
        return agent_reply #Return the reply for logging

def end_chat(user_name, agent):
    print(f"{agent}:Sayonara,{user_name}<3 let's catch up next time.")
    return f"{agent}:Sayonara,{user_name}\n" #Return the end message for logging

def chatbox():
    user_name = greet_user()
    agents, replies = agent_load() #Load agents and replies together
    if not agents: #Check if agents loaded successfully
        return
    agent = agent_select(agents)
    if not agent: #Check if agent was selected successfully
        return
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #Create timestamp for log file name
    log_filename = f"chat_log_{timestamp}.txt" #Create log file name with timestamp
    
    with open(log_filename, "w") as log_file: #Open log file in write mode ("w") once
        log_file.write(f"__history with {agent} started at {timestamp}\n") #Write initial log message with timestamp
        log_file.write(f"\n{agent}:Yo gang I'm here to vibe with you,{user_name}.To end the chat type 'sayonara'\n.\n") #Write agent greeting to log
        print(f"\n{agent}:Yo gang I'm here to vibe with you,{user_name}.To end the chat type 'sayonara'\n.") #Print agent greeting to console

        while True:
            user_in = input(f"{user_name}: ")
            log_file.write(f"{user_name}:{user_in}\n") #Write user input to log

            if user_in.lower() in ["sayonara", "bye", "exit", "quit"]: #Make exit commands case-insensitive
                end_message = end_chat(user_name, agent) #Get the end message
                log_file.write(end_message) #Write the end message to the log
                break
            else:
                agent_reply = reply(agent, replies, user_in, user_name) #Get the agent's reply
                log_file.write(f"{agent}:{agent_reply}\n") #Write agent reply to log


if __name__ == "__main__":
    chatbox()