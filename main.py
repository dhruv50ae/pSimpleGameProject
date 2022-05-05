import random


def getGuess():
    return list(input("What is your guess?\n"))


def generateCode():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]


def generateClues(code, userGuess):
    if userGuess == code:
        return "Code cracked!"

    clues = []
    for ind, num in enumerate(userGuess):
        if num == code[ind]:
            clues.append('match')
        elif num in code:
            clues.append("close")
    if clues == []:
        return ["Nope"]
    else:
        return clues


print("Welcome to Code Breaker!")

secretCode = generateCode()

clueReport = []

while clueReport != "Code cracked!":
    guess = getGuess()
    clueReport = generateClues(guess, secretCode)
    print("Here's the result of your guess: ")
    for clue in clueReport:
        print(clue)


x = getGuess()
print(x)
