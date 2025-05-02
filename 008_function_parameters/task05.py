# caesar cypher
# using a list approach
alphabet = 'abcdefghijklmnopqrstuvwxyz'

directive = input("Type encode to encrypt, type decode to decrypt:\n").lower()

if directive == 'encode':
    print("Welcome to the Casesar Cypher encryptor: ")
    message = input("Type the message you want encrypted:\n").lower()
    shift = int(input("Type the shift number:\n").lower())

    def encrypt(message, shift):
        encrypted_message = ""
        for char in message:
            if char in alphabet:
                char_index = alphabet.index(char)
                new_char_index = (char_index + shift)%26
                encrypted_message+=alphabet[new_char_index]
            else:
                encrypted_message+=char
        print(f"Here is the encoded message: {encrypted_message}")
    
    encrypt(message, shift)
elif directive == 'decode':
    print("Welcome to the Caesar Cypher decoder")
    decode_message = input("Type the message you want decrypted:\n").lower()
    decode_shift = int(input("Type the shift number:\n").lower())
    def decrypt(decode_message, decode_shift):
        decrypted_message = ""
        for char in decode_message:
            if char in alphabet:
                char_index = alphabet.index(char)
                new_char_index = (char_index - decode_shift)%26
                decrypted_message+=alphabet[new_char_index]
            else:
                decrypted_message+=char
        print(f"Here is your decoded message: {decrypted_message}")
    decrypt(decode_message, decode_shift)
else:
    print("Invalid input, please select between encode or decode")
