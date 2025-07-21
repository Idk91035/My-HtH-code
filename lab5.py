import random
#step 1
def cat_greeting():
    print("Cat says meow")
cat_greeting()

#step 2
def generate_superhero_power():
    name = "Random man"
    power = "stealing things that are inconvient"
    print(f"{name} is a hero with the power of {power}")
generate_superhero_power()

#step 3
def generate_superhero_power1():
    superpower = "flying"
    return superpower

print(generate_superhero_power1())

#step 4
def generate_superhero_power2(user_name, power_name):
    sentence = user_name + " power is " + power_name
    return sentence
print(generate_superhero_power2(user_name = "Eva" , power_name= "shape shifting" ))

#step 5
def cat_greeting():
    counter = 1
    while counter <=5:
        print("swoem tac eht")
        counter += 1
cat_greeting()
#step 6
def generate_multiple_powers(powers):
    for power in powers:
        print(f"Superpower: {power}")

generate_multiple_powers(["Flying", "Invisibility", "Super Strength", "Telepathy", "Time Travel"])

#my own code
def generate_random_powers():
    user_names = ["Eva", "Stellar", "Justin"]
    power_names = ["Superstrength", "Flight", "Invisibility "]
    random_name = random.choice(user_names)
    random_power = random.choice(power_names)
    final_sentence = random_name + " power is " + random_power
    return final_sentence

print(generate_random_powers())



