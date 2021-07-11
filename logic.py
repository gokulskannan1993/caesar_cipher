from resources import alphabet

# Caesar Cipher in one Method
def caesar_cipher(operation, text, key):
    answer = ""
    for letter in text:
        position = alphabet.index(letter)

        # Short hand if/else
        shifted_position = operation == "encode" and position + key or position - key

        new_letter = alphabet[shifted_position]
        answer += new_letter
    return answer


# Ask to do again
def goAgain():
    again = input("Do you want to do another operation? Press 'Yes' to proceed or Anything else to Terminate the app").upper()
    if(again == "YES"):
        operation = input("Enter 'encode' to encrypt or 'decode' to decrypt or 'exit' to terminate: ")
    else:
        terminate = True
