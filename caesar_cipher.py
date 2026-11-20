"""Caesar Cipher Encryption Tool - encrypt/decrypt text with a user-chosen shift."""


def shift_text(text, shift):
    result = []
    for ch in text:
        if ch.isupper():
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif ch.islower():
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(ch)  # keep spaces, digits, punctuation unchanged
    return "".join(result)


def encrypt(text, key):
    return shift_text(text, key)


def decrypt(text, key):
    return shift_text(text, -key)


def get_key():
    while True:
        try:
            return int(input("Enter shift value (key, e.g. 3): ")) % 26
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=== Caesar Cipher Tool ===")
    while True:
        print("\n1) Encrypt   2) Decrypt   3) Brute-force (try all keys)   4) Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            text, key = input("Text to encrypt: "), get_key()
            enc = encrypt(text, key)
            print(f"\nOriginal : {text}\nEncrypted: {enc}\nDecrypted: {decrypt(enc, key)}")
        elif choice == "2":
            text, key = input("Text to decrypt: "), get_key()
            print(f"\nEncrypted: {text}\nDecrypted: {decrypt(text, key)}")
        elif choice == "3":
            text = input("Ciphertext: ")
            for k in range(1, 26):
                print(f"Key {k:2}: {decrypt(text, k)}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
