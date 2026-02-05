import random

question = input("Question: ")

random_answer = random.randint(1, 9)

if random_answer == 1:
    print("Yes - definitely.")
if random_answer == 2:
    print("It is decidedly so.")
if random_answer == 3:
    print("Without a doubt.")
if random_answer == 4:
    print("Reply hazy, try again.")
if random_answer == 5:
    print("Ask again later.")
if random_answer == 6:
    print("Better not tell you now.")
if random_answer == 7:
    print("My sources say no.")
if random_answer == 8:
    print("Outlook not so good.")
if random_answer == 9:
    print("Very doubtful.")
