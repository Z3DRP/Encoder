#! /user/bin/env/python3

#letter code by Zach Palmer
from LetterCodeLogic import LetterCodeLogic

def main():
    print("Welcome to Letter Code")

    choice = getChoice()
    while choice != 0:
        if choice == 1:
            cesar = isCesar("Are you encoding a Cesar Message ")
            if not cesar:
                msg = input("Enter your message to encode : ")
                result = LetterCodeLogic.Encode(msg)
                print(f"Your Encoded message is :\n {result}")
            else:
                msg = input("Enter your message to encode : ")
                Os = getOffset("Enter offset")
                result = LetterCodeLogic.EncodeCesar(msg,Os)
                print(f"Your Cesar Shift message is :\n {result}") 
        elif choice == 2:
            cesar = isCesar("Are you decoding a Cesar Message ")
            if not cesar:
                msg = input("Enter your numbers to decode (seperated by comas) : ")
                result = LetterCodeLogic.Decode(msg)
                print(f"Your decoded message is :\n {result}")
            else:
                msg = input("Enter message to decode (seperated by comas) : ")
                Os = getOffset("Enter offset to reverse shift ")
                result = LetterCodeLogic.DecodeCesar(msg,Os)
                print(f"Your decoded Cesar message is :\n {result}")
        else:
            print("i dont understand ur request")

        choice = getChoice()
    print("thanks for using the letter code program")

def getChoice():
    goodChoice = False
    while not goodChoice:
        try:
            chc = int(input("Enter Operation: 1-encode, 2-decode, 0-quit : "))
            if chc not in range(0,3):
                print("Error unknown operation, enter 1, 2 or 0")
                goodChoice = False
            else:
                goodChoice = True
        except ValueError:
            print("Error operation must be numeric")
    return chc
    
def isCesar(prompt):
    checked = False
    while not checked:
        try:
            answer = input(f"{prompt} (Y/N) : ")
            if answer.lower() == "y":
                isCesar = True
                checked = True
            elif answer.lower() == "n":
                isCesar = False
                checked = True
            else:
                print("Enter Y for yes or N for no")
        except ValueError:
            print("Error enter Y for yes and N for no")
    return isCesar

def getOffset(prompt):
    goodOs = False
    while not goodOs:
        try:
            os = int(input(f"{prompt} : "))
            if os < -5 or os > 5:
                print("Error offset must be between -5 and 5")
                goodOs = False
            else:
                goodOs = True
        except ValueError:
            print("Error offset must be numeric")
    return os
                     
    
        
            




if __name__ == "__main__":
    main()
