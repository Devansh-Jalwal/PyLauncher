import random
print("")
print(" ____________________")
print("|Welcome To Baseball!|")
print("|____________________|")
print("")
print(" __________________________________________")
print("|Rules: Enter a number between 1 and 3.    |")
print("|If your number matches the CPU's number,  |")
print("|you score that number of Score.           |")
print("|If it doesn't match, your turn ends.      |")
print("|You only have one Strike                  |")
print("|You will get a chance to bowl the CPU too!|")
print("|__________________________________________|")

score = 0
score_cpu = 0

# Player's Turn
print("Your Turn")
print("")

while True:
    y = random.randint(1, 3)

    x = int(input("Enter a number between 1 and 3: "))

    if x < 1 or x > 3:
        print("Please enter a number between 1 and 3.")
        continue

    print(f"You Chose {x}")
    print(f"The CPU Chose {y}")

    if x == y:
        print("The Score Matched!")
        score += x
        print(f"Your Score: {score}")
    else:
        print("OUT!")
        print(f"Your Final Score Was {score}")
        break

    print()

# CPU's Turn
print("")
print("CPU's Turn")
print("")

while True:
    p = random.randint(1, 3)

    q = int(input("Enter a number between 1 and 3 for the CPU: "))

    if q < 1 or q > 3:
        print("Please enter a number between 1 and 3.")
        continue

    print(f"CPU Chose {p}")
    print(f"You Chose {q}")

    if q == p:
        print("The Score Matched!")
        score_cpu += q
        print(f"CPU Score: {score_cpu}")
    else:
        print("CPU OUT!")
        print(f"The CPU Scored {score_cpu}")
        break

    print()

print("")
print("Final Scores")
print(f"You: {score}")
print(f"CPU: {score_cpu}")
print("")

if score_cpu == score:
    print("It's A Tie!")
elif score_cpu > score:
    print("The CPU Won!")
else:
    print("You Won!")