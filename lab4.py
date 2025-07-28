# Task 1

continue_checking = "yes"

while continue_checking.lower() == "yes":
    age = int(input("Enter your age: "))

    if age >= 18:

        print("You are eligible to vote.")
    else:

        print("You are not eligible to vote.")

    continue_checking = input("Do you want to check another age? (yes/no)")

#Task 2

numbers = [19, -9, 0, 26, -8, 123]

for num in numbers:
    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print(f"{num} is zero.")

#Task 3

inventory = ["coal", "dirt", "diamond", "gravel", "stone"]

for block in inventory:
    print(f"A {block} has been found!")

if block == "diamond":
    print("YOU'RE RICH!")