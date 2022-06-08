import random

name = input("What is your name  ")
question = input("What is your dream?  ")

# Magic Answer
answer = ""

# Pre conditions
if name == "":
    print("Question: " + question)

# Create a random number
random_number = random.randint(1, 9)
# Print random number
print(random_number)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "is depend"
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Hmmmm, I think u can."
elif random_number == 5:
    answer = "Maybe."
elif random_number == 6:
    answer = "Better try to find another dream ;)."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Are you serius!."
else:
    answer = "Error"

# Let's Play

print(name + " ask: " + question)

print("Magic 8-Ball's answer: " + answer)
