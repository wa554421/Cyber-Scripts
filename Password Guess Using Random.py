from random import choice
import os

# Input the user's password
u_pwd = input("Enter a Password: ")

# Define the list of possible characters
pwd = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

# Initialize variables
pw = ""
attempts = 0  # To count the number of attempts

# Start the password cracking
print("Cracking the password... please wait!")

while pw != u_pwd:
    pw = ""  # Reset the password guess for each attempt
    for i in range(len(u_pwd)):
        # Randomly choose characters and build the password
        guessed_char = choice(pwd)
        pw += guessed_char

    attempts += 1  # Increment the attempts counter

    # Provide progress feedback occasionally
    if attempts % 1000 == 0:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen (platform independent)
        print(f"Attempts: {attempts}, Current Guess: {pw}")

# Output the result
print("\nPassword successfully cracked!")
print(f"Your password is: {pw}")
print(f"Total attempts: {attempts}")
