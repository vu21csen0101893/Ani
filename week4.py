import random
import string

def generate_password(length=12):
    """
    Generate a strong, secure password with the specified length.
    The password will include uppercase letters, lowercase letters,
    numbers, and special characters.
    """
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def generate_multiple_passwords(num_passwords=5, length=12):
    """
    Generate multiple strong, secure passwords with the specified length.
    """
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    print("Welcome to the Strong Password Generator!")
    print("----------------------------------------")
    
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))
        
        if num_passwords <= 0 or password_length <= 0:
            print("Please enter valid positive integers for number of passwords and password length.")
        else:
            passwords = generate_multiple_passwords(num_passwords, password_length)
            print("\nGenerated Passwords:")
            for i, password in enumerate(passwords, 1):
                print(f"Password {i}: {password}")
    except ValueError:
        print("Please enter valid integers for number of passwords and password length.")
