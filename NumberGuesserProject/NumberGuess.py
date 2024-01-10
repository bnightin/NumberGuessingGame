import random

def getLowerBound():
    lower_bound = input("What do you want the lower bound to be for the number? ").strip()
    if checkIfDigit(lower_bound) == False:
        print("Please enter a number")
        return getLowerBound()
    return int(lower_bound)

def getUpperBound():
    upper_bound = input("What do you want the upper bound to be for the number? ").strip()
    if checkIfDigit(upper_bound) == False:
            print("Please enter a number")
            return getUpperBound()
    return int(upper_bound)

def generateNumber():
    global randNum
    lower_bound = getLowerBound()
    upper_bound = getUpperBound()
    randNum = random.randint(lower_bound,upper_bound)
    print(randNum)
    return randNum

def checkIfDigit(input):
    if input.isdigit() == False:
        return False
    return True

def guessNumber():
     count = 0
     isCorrect = False
     while isCorrect == False:
        guess = input("What do you want to guess: ").strip()
        if checkIfDigit(guess) == False:
            print("Please enter")
            return guessNumber()
        count += 1
        if int(guess) > randNum:
            print("Your guess was too high, try lower. ")
        if int(guess) < randNum:
            print("Your guess was too low, try higher. ")
        if int(guess) == randNum:
            print(f"You guessed correctly! It took {count} guesses!")
            isCorrect = True
        
def main():
    generateNumber()
    guessNumber()

main()
