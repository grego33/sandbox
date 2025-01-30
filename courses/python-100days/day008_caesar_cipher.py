import string


alphabet = list(string.ascii_lowercase)
charset = alphabet + alphabet

def shift(message: str, offset: int) -> str:
    new_message = ""
    for letter in message:
        location = alphabet.index(letter)
        # alpha_palindrome = alphabet + alphabet.reverse()
        new_letter = charset[location + offset]
        new_message += new_letter

    return new_message

def encrypt(message: str, offset: int) -> str:
    return shift(message, offset)

def decrypt(message: str, offset: int) -> str:
    return shift(message, -offset)


print("This program will encrypt and decrypt your message using a Caesar Cipher\n\n")

message = input("Enter the message you would like to encrypt \n > ")
offset = int(input("Enter the secret code number (0-94): "))

print(f"The encrypted message is:\n-----------\n{encrypt(message, offset)}\n---------\n")


