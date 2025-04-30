print("🤖 Hello! I'm ChatBot. Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi there!")
    elif user == "how are you":
        print("Bot: I'm just code, but I'm good! 😊")
    elif user == "what is your name":
        print("Bot: I'm your friendly Python ChatBot!")
    elif user == "bye":
        print("Bot: Goodbye! 👋")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")

