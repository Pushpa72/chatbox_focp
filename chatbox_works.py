import json 
import random 
import time 
def greet_user():
    user_name=input("enter your name: ")
    print(f"Konichiwa {user_name}.welcome to the noobworld")
    return user_name

def agent_select():
    with open('json.json') as file:
        data = json.load(file)
        agents=data["agents"]
                

    print("choose your companian to guide through this journey:")
    for idx, agent in enumerate(agents, 1):
        print(f"{idx}. {agent}")
    print("4. Random agent")
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
             random_agent = random.choice(agent)
             print(f"Randomly selected agent: {random_agent}")
             return random_agent
        else:
             print("Invalid choice, please try again.")
             return agent_select()
        
def save_chat(user_name,agent_select):
    with open('json.json') as file:
        data=json.load(file)
        reply =data["reply"][agent_select]
    with open("chat_log.txt","a") as log_file:
        log_file.write(f"__history with {agent_select}___\n")
        print(f"\n{agent_select}:Yo gang I'm here to vibe with you,{user_name}.To end the chat type 'sayonara'.")

        log_file.write(f"{user_name}:{us}")
def end_chat(user_name,agent_select):
    if user_in in ["sayonara","bye","exit","quit"]
        print(f"{agent}:Sayonara,{user_name}<3 let's catch up next time.")
        log_file.write(f"{agent_select}:sayonara,{user_name}\n")
        break
def reply(agent_select):
    if user_in in reply:
        reply=reply[user_in]
        print(f"{agent_select}:{reply}")
        log_file.write(f"{agent_select}:{reply}\n")
    else:
        ran_reply=[
            f"{agent_select}: Gang I have no idea what you just said"
            f"{agent_select}: that's lowkie interesting {user_name}.tell me abt it "

        ]
        response = random.choice(ran_reply)
        print(ran_reply)
        log_file.write(f"{agent}:{ran_reply}")

def chatbox():
    user_name = greet_user()
    agent = agent_select()
    save_chat(user_name,agent)
    end_chat(user_name,agent_select)
    reply(agent_select)

    
if __name__ == "__main__":
    chatbox()
   