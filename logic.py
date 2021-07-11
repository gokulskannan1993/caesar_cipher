from resources import alphabet

# Method to encrypt the message with key
def encrypt(message, key):
    cipher = ""

    for letter in message:
        position = alphabet.index(letter)
        shifted_position = position + key
        new_letter = alphabet[shifted_position]
        cipher += new_letter

    return cipher


# Method to decrypt the cipher text with key
def decrypt(cipher, key):
    message = ""

    for letter in cipher:
        position = alphabet.index(letter)
        shifted_position = position - key
        new_letter = alphabet[shifted_position]
        message += new_letter

    print(message)



decrypt("a", 1)

