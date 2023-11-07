names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
random_number = random.randint(0, len(names) - 1)
print(f"{names[random_number]} is going to buy the meal today!")
