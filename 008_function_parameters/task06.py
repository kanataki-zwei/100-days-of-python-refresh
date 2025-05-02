# combine encrypt and decrypt in one function
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print("Welcome to the Caesar Cypher encryptor and decryptor program!\n")
on_state = True
while on_state == True:
    directive = input("Type encode to encrypt, type decode to decrypt:\n").lower()
    if directive == "encode" or directive == "decode":
        message = input(f"Type the message you want to {directive}: \n").lower()
        shift = int(input("Type the number of shifts: \n"))
        def caesar_cypher(message, shift):
            output_message = ""
            if directive == 'encode':
                print("encrypting message")
                for char in message:
                        if char in alphabet:
                            char_index = alphabet.index(char)
                            new_char_index = (char_index+shift)%26
                            output_message+=alphabet[new_char_index]
                        else:
                            output_message+=char
                print(f"Encryption complete. Your encrypted message is: {output_message}")
            else:
                print("decrypting message")
                for char in message:
                    if char in alphabet:
                        char_index = alphabet.index(char)
                        new_char_index = (char_index-shift)%26
                        output_message+=alphabet[new_char_index]
                    else:
                        output_message+=char
                print(f"Decryption complete. Your decrypted message is: {output_message}")
            return output_message
        caesar_cypher(message, shift)
        proceed = input("Type 1 to keep using the program, type 2 to exit:\n")
        if proceed == "1":
             print("_____________")
        else:
             print("Thank you for using the caesar cypher program!\n See you soon!")
             on_state = False
    else:
            print("Invalid choice selected!")