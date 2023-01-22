import random

def get_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def get_guess():
    guess = []
    while len(guess) != 3:
        guess = list(input("What is your guess? "))
        if len(guess) == 3:
            return guess
        else:
            print("ERROR! ERROR! ERROR! Oh god what have you done?!")
        

def generate_clues(secret_code, guess):
    if guess == secret_code:
        clues = ("You Won!")
        return clues

    clues = []

    for ind,num in enumerate(guess):
        if num == secret_code[ind]:
            clues.append("Match!")
        elif num in secret_code:
            clues.append("Close!")
    if clues == []:
        clues.append("Nope!")
        return clues
    else:
        return clues
print("")
print("Welcome to Code Breaker!")
print("To crack the code, you'll be attempting to guess a 3 digit code")
print("If any of the numbers match the exact spot it is at you'll get a 'Match!'")
print("If any of the numbers are in the code but in the wrong spot, it will return 'Close!'")
print("Please, do not input anything other than 3 digit code attempts..")
print("")

secret_code = get_code()
print("Generated code, please guess a 3 digit code")

clueReports = []

while clueReports != "You Won!":
    guess = get_guess()
    clueReports = generate_clues(secret_code, guess)
    print("Here is the result of your guess: ")
    if (type(clueReports)) == str:
      print(clueReports)
    elif type(clueReports) == list:
        for clues in clueReports:
         print(clues)

