def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)

        else:
            result += char

    return result


# -------- Main Program --------

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted_text = encrypt(message, shift)
print("Encrypted Message:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Message:", decrypted_text)
