import random as rd

def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print(f"computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie!!")
elif a:
    print("You win!!")
else:
    print("You Lose!!")

