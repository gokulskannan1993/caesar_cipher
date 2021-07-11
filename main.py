from logic import caesar_cipher, goAgain
from resources import clear, logo


terminate = False


# Asking for user input 
clear()
print(logo)

while not terminate:
    operation = input("Enter 'encode' to encrypt or 'decode' to decrypt: ")
    text = input("Enter the message: ").lower()
    key = int(input("Enter the shift number:")) % 26


    # Switch operations according to User input 
    caesar_cipher(operation, text, key)

    # If the user wants to repeat
    again = input("Enter 'yes' to do again or 'no' otherwise: ")
    if again == "no":
        terminate = True
        print("All Done, Program is Terminated")
