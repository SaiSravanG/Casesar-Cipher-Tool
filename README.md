# Casesar-Cipher-Tool
A Python program that encrypts and decrypts text using the Caesar Cipher technique with a shift value (key) chosen by the user.

**Technologies Used:** Python 3 (standard library only)

**Caesar Cipher:** One of the oldest and simplest encryption methods. Each letter of the message is moved forward by a fixed number of positions in the alphabet. Example: with key 3, A becomes D, B becomes E and Z wraps around to C. Decryption moves the letters back by the same number.

## How it works
- The user picks Encrypt, Decrypt or Brute-force from a menu
- The user enters the text and the shift value
- Upper and lowercase letters are shifted separately; spaces, numbers and symbols stay the same
- Both the encrypted and the decrypted text are displayed

## Setup Instructions
1. Install Python 3.8 or above
2. Download or clone this repository
3. Open Command Prompt in the Task-2 folder and run: `python caesar_cipher.py`
4. Follow the menu

## Results
```
Original : Meet me at 5 PM, Sai!
Key      : 5
Encrypted: Rjjy rj fy 5 UR, Xfn!
Decrypted: Meet me at 5 PM, Sai!
```
The Brute-force option tries all 25 keys on a ciphertext, which shows why this cipher is not secure.

## Security Risks
Because there are only 25 possible keys, the Caesar Cipher can be broken in seconds by trying every key or by frequency analysis. It is good for learning how encryption works but must not be used to protect real data. Modern encryption such as AES uses far larger key spaces.
