from logic import caesar_cipher, goAgain
from resources import clear, logo




# Asking for user input on operation
clear()
print(logo)
operation = input("Enter 'encode' to encrypt or 'decode' to decrypt: ")
text = input("Enter the message: ").lower()
key = int(input("Enter the shift number:"))


# Switch operations according to User input 
caesar_cipher(operation, text, key)

