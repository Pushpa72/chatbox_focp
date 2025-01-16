import json 
import random 
import datetime

def greet_user():
    user_name=input("enter your name: ")
    while not user_name:
        print("Yo Gang..please enter your name")
    print(f"Konichiwa {user_name}.welcome to the botworld")
    return user_name

def agent_load():
    with open('json.json') as file:
        data = json.load(file)
        return data["agents"]
                
def agent_display(agents):
    print("choose your companian to guide through this journey\nwe have 3 agents to choose form each with their unique sector library,canteen,admission respectively.")
    for idx, agent in enumerate(agents, 1):
        print(f"{idx}. {agent}")
    print("4. Random agent")

def agent_select(agents):
    agent_display(agents)
    while True:
        choice=input("enter your choice:")
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

    with open("chat_log.txt","a") as log_file:
        log_file.write(f"\n__chat history with {agent}\n")
        print(f"\n{agent}:Yo gang I'm here to vibe with you,{user_name}.To end the chat type 'sayonara'\n.")
        log_file.write(f"{user_name}:{user_in}\n")

def end_chat(user_name,agent,log_file,session_summary):
        print(f"{agent}:Sayonara,{user_name}<3 let's catch up next time.")
        log_file.write(f"{agent}:sayonara,{user_name}\n")
        print("\nSession Summary:")
        print("-" * 20)
        print(f"User: {user_name}")
        print(f"Agent: {agent}")
        print(f"Total Interactions: {len(session_summary)}")

def random_disconnect(agent,user_name,log_file):
    d_msg=[
        f"{agent}:oopsie!lost connection,{user_name}.see you later",
        f"{agent}:Gotta run!!,bye byeeee {user_name}",
    ]
    msg=random.choice(d_msg)
    print(msg)
    log_file.write(f"{agent}:{msg}\n")
    

def reply(agent,log_file,user_in,user_name,session_summary):
    log_file.write(f"\n{user_name}: {user_in}\n")

    with open('json.json') as file:
        data = json.load(file)
        replies = data["reply"].get(agent, {})
    user_in_lower = user_in.lower()

    search_key = None
    for key, value in replies.items():
        if key.lower() in user_in_lower: 
            search_key = value
            break

    if search_key:
        print(f"{agent}:{search_key}")
        log_file.write(f"\n{agent}:{search_key}\n")
    else:
        ran_reply=([
            f"{agent}: Gang I have no idea what you just said",
            f"{agent}: that's lowkie interesting {user_name}.tell me abt it "

        ])
        agent_reply = random.choice(ran_reply)
        print(agent_reply)
        log_file.write(f"{agent}:{agent_reply}")
        session_summary.append({"user": user_in, "agent": agent_reply})
def chatbox():
    user_name = greet_user()
    agents=agent_load()
    agent=agent_select(agents)
    print(f"\n{agent}:Yo gang I'm here to vibe with you,{user_name}.To end the chat type 'sayonara'\n.")
   
    session_summary=[]
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"Chat session started at {datetime.datetime.now()}\n")
        while True:  
            user_in = input(f"{user_name}: ").lower() 
            if user_in in ["sayonara", "bye", "exit", "quit"]:  
                end_chat(user_name, agent, log_file,session_summary)  
                break  
            else:
                reply(agent,log_file,user_in,user_name,session_summary)
                session_summary.append({"user": user_in, "agent": reply})
if __name__ == "__main__":
    chatbox()
   