target = int(input()) # Enter a number between 0 and 1000
# Example Input 1
# 10
# Example Output 1
# 30

total = 0
for number in range(1, target+1):
    if number % 2 == 0:
        total += number
print(total)