from resources import alphabet


# Caesar Cipher Method for encoding and decoding
def caesar_cipher(operation, text, key):
    answer = ""

    if operation == 'decode':
        key *= -1

    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            shifted_position =  position + key 

            new_letter = alphabet[shifted_position]
            answer += new_letter
        else:
            answer += character
    print(f"The {operation}d text is '{answer}'")


# Ask to do again
def goAgain():
    again = input("Do you want to do another operation? Press 'Yes' to proceed or Anything else to Terminate the app").upper()
    if(again == "YES"):
        operation = input("Enter 'encode' to encrypt or 'decode' to decrypt or 'exit' to terminate: ")
    else:
        terminate = True
