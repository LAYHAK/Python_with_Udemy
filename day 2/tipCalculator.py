# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to tip Calculator")
bill = float(input("How much Bill in total?\n"))
split = int(input("How many people you want to split?\n"))
tip_percent = int(input("How many percent of tip you want to pay? 10 ,12 ,15 \n"))
# tip = (tip_percent/100*bill+bill)/split
tip = bill / split * (1 + tip_percent / 100)
print(f"Each person should pay: ${round(tip,2)}")
