import string
import random

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))

    return password

#  user to specify the  length of the password
length = int(input("Enter the desired length of the password: "))

#  To Generate the password
password = generate_password(length)

#  To Display the password
print("Your generated password is: ", password)
