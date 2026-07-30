#Basic Rule-Based Chatbot
#Function to generate a chatbot 
def chatbot_responses(user_input):
    user_input=user_input.lower()
    if user_input== 'hi' or user_input== "hello":
        return"Hello!"
    elif user_input== "how are you?":
        return"I am fine. Thanks! What about you?"
    elif user_input=="i am fine too.":
        return"What do you do?"
    elif user_input== "i am a student.":
        return"That's great! What is your major?"
    elif user_input== "i am studying computer science as a mojor.":
        return"That sounds amazing. Let me know whenever you need help."
    elif user_input== "thanks. i would love to consult to you.":
        return"I will be responsive anytime."
    elif user_input== "bye":
        return "Have a nice day. Good bye!"
    else: 
        return "Sorry. I dont understand it."


#Main Program 
print("Welcome to the Chatbot")

while True:
    user= input("You: ")
    response= chatbot_responses(user)
    print("Bot: ",response)

    if user.lower()== 'bye':
        break



