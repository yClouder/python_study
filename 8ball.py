import random
possibleAns = ["It is certain.",  "It is decidedly so.",  "Without a doubt.",  "Yes – definitely.",  "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
user_input = ""

def call8ball():
    rock = random.randint(0,15)
    if user_input == "shake":
        return print(possibleAns[rock])
    elif user_input == "quit":
        pass
    else:
        return print("Please shake the ball.")

while user_input != "quit":
    user_input = input("Ask one question and shake the ball(Insert SHAKE to shake) or /'q/' to quit: ")
    call8ball()

print("Goodbye!")