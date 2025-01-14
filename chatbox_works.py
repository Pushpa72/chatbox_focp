import random
def greet_user():
    user_name=input("enter your name: ")
    print(f"Konichiwa {user_name}")
    return user_name
def agent_select():
    print("here are thents:")
    print("1.Ventress")
    print("2. Kane")
    print("3. Lena")
    print("4.random agent")
    choice=input("enter your choice(1,2,3,4):")
    if choice == '1':
        print("Ventress selected")
        return "Ventress"
    elif choice == '2':
        print("Kane selected")
        return "Kane"
    elif choice == '3':
        print("Lena selected")
        return "Lena"
    elif choice == '4':
        agent = ["Ventress", "Kane", "Lena"]
        random_agent = random.choice(agent)
        print(f"Randomly selected agent: {random_agent}")
        return random_agent
    else:
        print("Invalid choice, please try again.")
        return agent_select()
    
if __name__ == "__main__":
    user_name = greet_user()  
    selected_agent = agent_select()  
   