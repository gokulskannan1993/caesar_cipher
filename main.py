from logic import caesar_cipher, goAgain
from resources import clear




# Asking for user input on operation
clear()
operation = input("Enter 'encode' to encrypt or 'decode' to decrypt or 'exit' to terminate: ")
text = input("Enter the message: ").lower()
key = int(input("Enter the shift number:"))


# Switch operations according to User input 
print(caesar_cipher(operation, text, key))

