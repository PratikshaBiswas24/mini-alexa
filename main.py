# ==========================================
# PROJECT: VIRTUAL AI ASSISTANT (MINI ALEXA)
# ==========================================

from datetime import datetime
import random

# ------------------------------------------
# 1. GREETING AND NAME CAPTURE
# ------------------------------------------

def get_user_name():

    print("=" * 45)
    print("       MINI ALEXA - VIRTUAL ASSISTANT")
    print("=" * 45)
    print("\nAssistant: Hello! Welcome to Mini Alexa.")
    name=input("Assistant: What's your name? ").strip()

    if not name:
        name="User"
    return(name)

def build_greeting(name):
    print(f"\nAssistant: Nice to meet you, {name}!")
    print("Assistant: I am Mini Alexa, your virtual assistant.")
    print("Assistant: Type 'help' to see what I can do.")


# ------------------------------------------
# 2. DATE AND TIME FUNCTIONALITY
# ------------------------------------------

def get_current_date():
    today = datetime.now()
    return today.strftime("%d-%m-%Y")

def get_current_time():
    now = datetime.now()
    return now.strftime("%I:%M:%S %p")


# ------------------------------------------
# 3. BASIC CALCULATOR
# ------------------------------------------

def calculate(expression):
    try:
        parts = expression.split()
        if len(parts) != 4:
            return("Use this format: calculate 12 + 8")

        num1=float(parts[1])
        operator=parts[2]
        num2=float(parts[3])

        if operator=="+":
            result=num1+num2
        elif operator=="-":
            result=num1-num2
        elif operator=="*":
            result=num1*num2
        elif operator=="/":
            if num2==0:
                return("I can't divide by zero.")
            result=num1/num2
        else:
            return("Invalid operator. Use +, -, * or /.")

        if result.is_integer():
            result = int(result)

        return(f"The result is {result}")

    except ValueError:
        return("Invalid input! Please enter valid numbers.")


# ------------------------------------------
# 4. ENTERTAINMENT MODULE
# ------------------------------------------

QUOTES=[
    "Believe in yourself and all that you are.",
    "Great things take time. Keep going!",
    "Success is the sum of small efforts repeated daily.",
    "Dream big and work hard.",
    "Every day is a new opportunity to grow."
]


JOKES=[
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? Because it left its Windows open!",
    "What is a computer's favourite snack? Microchips!",
    "Why did the developer go broke? Because they used up all their cache!"
]


FACTS=[
    "Honey never spoils when stored properly.",
    "Octopuses have three hearts.",
    "A day on Venus is longer than its year.",
    "The human brain contains billions of neurons.",
    "Bananas are botanically classified as berries."
]

def get_random_quote():
    return(random.choice(QUOTES))

def get_random_joke():
    return(random.choice(JOKES))

def get_random_fact():
    return(random.choice(FACTS))


# ------------------------------------------
# 5. NUMBER GUESSING GAME
# ------------------------------------------

def play_guessing_game():
    secret_number=random.randint(1, 20)
    attempts = 5
    print("\nAssistant: Welcome to the Number Guessing Game!")
    print("Assistant: I am thinking of a number between 1 and 20.")
    print("Assistant: You have 5 attempts to guess it.")

    while (attempts>0):
        try:
            guess=int(input("\nEnter your guess: "))
            if (guess<1 or guess>20):
                print("Assistant: Please enter a number between 1 and 20.")
                continue
            attempts-=1
            if guess==secret_number:
                print("\nAssistant: Congratulations! You guessed it!")
                print("Assistant: You are absolutely correct!")
                return
            elif(guess<secret_number):
                print("Assistant: Try a higher number!")
            else:
                print("Assistant: Try a lower number!")
            print("Assistant: Attempts remaining:", attempts)
        except ValueError:
            print("Assistant: Please enter a valid whole number.")
    print("\nAssistant: Game Over!")
    print("Assistant: The correct number was", secret_number)


# ------------------------------------------
# 6. RULE-BASED AI RECOMMENDATION
# ------------------------------------------

def recommend_activity():
    current_hour=datetime.now().hour
    print("\nAssistant: Let me suggest an activity for you!")
    if 6<=current_hour<11:
        print("Assistant: Good morning!")
        print("Assistant: Have breakfast and start your day.")
    elif 11<=current_hour<15:
        print("Assistant: It's lunchtime!")
        print("Assistant: Take a break and enjoy your lunch.")
    elif 15<=current_hour<18:
        print("Assistant: It's afternoon!")
        print("Assistant: Go for a walk or do some exercise.")
    elif 18<=current_hour<22:
        print("Assistant: Good evening!")
        print("Assistant: Relax and enjoy your evening.")
    else:
        print("Assistant: It's time to rest.")
        print("Assistant: Get some sleep and recharge yourself.")


# ------------------------------------------
# 7. SIMPLIFIED PERCEPTRON DEMONSTRATION
# ------------------------------------------

def perceptron_demo():

    print("\nAssistant: Welcome to the Perceptron Demo!")
    try:
        input1=float(input("Enter first input: "))
        input2=float(input("Enter second input: "))
        weight1=0.5
        weight2=0.8
        bias=-0.4
        weighted_sum=(input1*weight1)+(input2*weight2)+bias
        print("\nAssistant: Calculating neuron output...")
        print("Input 1:", input1)
        print("Input 2:", input2)
        print("Weight 1:", weight1)
        print("Weight 2:", weight2)
        print("Bias:", bias)
        print("Weighted Sum:", round(weighted_sum, 2))
        if weighted_sum>0:
            output=1
        else:
            output=0
        print("Assistant: Final Neuron Output:", output)
    except ValueError:
        print("Assistant: Please enter valid numerical inputs.")


# ------------------------------------------
# 8. HELP MENU
# ------------------------------------------

def show_help():

    print("\n========== MINI ALEXA HELP MENU ==========")
    print("\nAssistant: Here are the commands I can perform:")
    print("\n1. date")
    print("   Displays the current date.")
    print("\n2. time")
    print("   Displays the current time.")
    print("\n3. calculate 12 + 8")
    print("   Performs basic mathematical calculations.")
    print("   Supported operators: +, -, *, /")
    print("\n4. quote")
    print("   Displays a random motivational quote.")
    print("\n5. joke")
    print("   Tells you a random joke.")
    print("\n6. fact")
    print("   Displays a random interesting fact.")
    print("\n7. game")
    print("   Starts the number guessing game.")
    print("\n8. recommend")
    print("   Suggests an activity based on the current time.")
    print("\n9. perceptron")
    print("   Demonstrates a simplified perceptron calculation.")
    print("\n10. help")
    print("    Displays this help menu.")
    print("\n11. exit / quit / bye")
    print("    Exits the virtual assistant.")
    print("\n==========================================")


# ------------------------------------------
# 9. MAIN PROGRAM
# ------------------------------------------

def main():
    user_name=get_user_name()
    build_greeting(user_name)

    while True:
        command=input(f"\n{user_name}: ").lower().strip()

        if command=="date":
            print("Assistant: Today's date is", get_current_date())
        elif command=="time":
            print("Assistant: The current time is", get_current_time())
        elif command.startswith("calculate"):
            result=calculate(command)
            print("Assistant:", result)
        elif command=="quote":
            print("Assistant:", get_random_quote())
        elif command=="joke":
            print("Assistant:", get_random_joke())
        elif command=="fact":
            print("Assistant:", get_random_fact())
        elif command=="game":
            play_guessing_game()
        elif command=="recommend":
            recommend_activity()
        elif command=="perceptron":
            perceptron_demo()
        elif command=="help":
            show_help()
        elif command in ["exit", "quit", "bye"]:
            print(f"Assistant: Goodbye, {user_name}! Have a great day.")
            break
        else:
            print("Assistant: I don't understand that command yet.")
            print("Assistant: Type 'help' to see the available commands.")


# ------------------------------------------
# 10. PROGRAM EXECUTION
# ------------------------------------------
if __name__=="__main__":
    main()
