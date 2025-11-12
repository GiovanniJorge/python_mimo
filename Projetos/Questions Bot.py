# 1. Hello
name = input("Hello! What is your name? ")
print(f"Nice to meet you, {name}!\n")

# 2. Age
age_input = input("How old are you? ")
age = int(age_input)
bot_age = 3
age_difference = age - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!\n")

# 3. Color
color = input("What's your favorite color? ")
print(f"Oh, {color} is a beautiful color!\n")

# 4. Feel
state = input("Are you alright? ")
if (state.lower() == "yes"):
  print("Good to know!\n")
else:
  print("Sad to know.\n")

# 5. Animal
animal = input("What's your favorite animal? ")
print(f"The {animal} is such a beatiful animal!")
if(animal.lower() == "dog"):
  print("And it's my favorite too!\n")
else:
  print("Mine is the dog.\n")

# 6. End
print("Ok.\nThanks for talking to me!")