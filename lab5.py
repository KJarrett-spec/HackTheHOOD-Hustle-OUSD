#Lab 5 Kwame Jarrett

#Cat Function
def cat_greeting(word):
    print(f'Cat says{word}')
    print(f'Cat says {word}')
cat_greeting("meoew!")

#Step 2
def generate_superhero_power():
    name = "Tony"
    power = "flying and being a billionaire"
    print(f"{name}'s superpower consists of flying and being a billionaire.")

#Step 3
def generate_superhero_power1():
    power = "flying and being a billionaire"
    return power

print(generate_superhero_power1())

#Step 4
def generate_super_power2(user_name, user_power):
    message = user_name + "has the power of" + "super_power" + "!"
    return message

    print(generate_superhero_power("Tony", "flying and being a billionaire"))

#Step 5
def cat_greeting_loop():
    #    for i in range(5):
    #    print(f'The cat says {greeting}')
    greetings = ["meow", "purr", "hiss", "mew", "yowl"]

    for greeting in greetings:
        print(f'The cat says {greeting}')

#Step 6
def generate_multiple_superhero_powers(powers):
    for i in powers:
        print(i)

powers_test = ["super strength", "invisibility", "teleportation", "time travel"]
generate_multiple_superhero_powers(powers_test)