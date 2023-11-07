# 1. Create a greeting for your program.

# 2. Ask the user for the city that they grew up in.

# 3. Ask the user for the name of a pet.

# 4. Combine the name of their city and pet and show them their band name.

# 5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end
print('''
                                                     88                                                                 ad88            88                                 88            
                                               ,d    ""                                                                d8"              ""                                 88            
                                               88                                                                      88                                                  88            
 ,adPPYb,d8 8b,dPPYba,  ,adPPYba,  ,adPPYba, MM88MMM 88 8b,dPPYba,   ,adPPYb,d8    88,dPYba,,adPYba,  8b       d8    MM88MMM 8b,dPPYba, 88  ,adPPYba, 8b,dPPYba,   ,adPPYb,88 ,adPPYba,  
a8"    `Y88 88P'   "Y8 a8P_____88 a8P_____88   88    88 88P'   `"8a a8"    `Y88    88P'   "88"    "8a `8b     d8'      88    88P'   "Y8 88 a8P_____88 88P'   `"8a a8"    `Y88 I8[    ""  
8b       88 88         8PP""""""" 8PP"""""""   88    88 88       88 8b       88    88      88      88  `8b   d8'       88    88         88 8PP""""""" 88       88 8b       88  `"Y8ba,   
"8a,   ,d88 88         "8b,   ,aa "8b,   ,aa   88,   88 88       88 "8a,   ,d88    88      88      88   `8b,d8'        88    88         88 "8b,   ,aa 88       88 "8a,   ,d88 aa    ]8I  
 `"YbbdP"Y8 88          `"Ybbd8"'  `"Ybbd8"'   "Y888 88 88       88  `"YbbdP"Y8    88      88      88     Y88'         88    88         88  `"Ybbd8"' 88       88  `"8bbdP"Y8 `"YbbdP"'  
 aa,    ,88                                                          aa,    ,88                           d8'                                                                            
  "Y8bbdP"                                                            "Y8bbdP"                           d8'                                                                             


''')

city = input("What's name of the city you live in?\n")
pet = input("What is your pet's name?\n")

print("Your Band name could be " + pet + " " + city)
