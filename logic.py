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

