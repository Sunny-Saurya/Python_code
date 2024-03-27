import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker .1.2. Created by Sunny")
    while True:
        x = input("Enter what do you want to say : ")
        if x == "q":
            os.system("Say 'bye bye my friend will talk to you later.")
            break
        command = f"say {x}"
        os.system(command)