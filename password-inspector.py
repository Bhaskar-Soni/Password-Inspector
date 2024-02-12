import string
import hashlib
import requests
from colorama import Fore, Style

def password_strength(password):
    # Check length
    length_score = min(len(password) // 8, 3)

    # Check for uppercase letters
    uppercase_score = 1 if any(char.isupper() for char in password) else 0

    # Check for lowercase letters
    lowercase_score = 1 if any(char.islower() for char in password) else 0

    # Check for digits
    digit_score = 1 if any(char.isdigit() for char in password) else 0

    # Check for special characters
    special_char_score = 1 if any(char in string.punctuation for char in password) else 0

    # Calculate total score
    total_score = length_score + uppercase_score + lowercase_score + digit_score + special_char_score

    # Map total score to password strength level
    if total_score < 2:
        return "Very Weak"
    elif total_score < 4:
        return "Weak"
    elif total_score < 6:
        return "Medium"
    elif total_score < 8:
        return "Strong"
    else:
        return "Very Strong"

def character_checkmarks(password):
    # Check for uppercase letters
    uppercase_check = "✔" if any(char.isupper() for char in password) else "✘"

    # Check for lowercase letters
    lowercase_check = "✔" if any(char.islower() for char in password) else "✘"

    # Check for digits
    digit_check = "✔" if any(char.isdigit() for char in password) else "✘"

    # Check for special characters
    special_char_check = "✔" if any(char in string.punctuation for char in password) else "✘"

    return uppercase_check, lowercase_check, digit_check, special_char_check

def calculate_time_to_crack(password):
    # Assume 10^12 password attempts per second for the attacker
    attempts_per_second = 10**12

    # Assume a conservative estimate of possible characters for each character position
    possible_characters = 94  # (uppercase letters + lowercase letters + digits + symbols)

    # Calculate the total possible combinations
    total_combinations = possible_characters ** len(password)

    # Calculate the time to crack in seconds
    time_to_crack_seconds = total_combinations / attempts_per_second

    # Convert the time to crack to a human-readable format
    time_to_crack_human_readable = convert_seconds_to_human_readable(time_to_crack_seconds)

    return time_to_crack_human_readable

def convert_seconds_to_human_readable(seconds):
    # If the time is less than a day, show in days, hours, minutes, seconds
    if seconds < 86400:
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        time_parts = []

        if days > 0:
            time_parts.append(f"{int(days)} days")
        if hours > 0:
            time_parts.append(f"{int(hours)} hours")
        if minutes > 0:
            time_parts.append(f"{int(minutes)} minutes")
        if seconds > 0:
            time_parts.append(f"{int(seconds)} seconds")

        return ", ".join(time_parts)
    else:
        # Convert seconds to years
        years = seconds / (365.25 * 24 * 60 * 60)

        if years >= 1e12:
            return f"{years / 1e12:.2f} trillion years"
        elif years >= 1e9:
            return f"{years / 1e9:.2f} billion years"
        elif years >= 1e6:
            return f"{years / 1e6:.2f} million years"
        else:
            return f"{int(years)} years"

def check_password_breaches(password):
    # Hash the password using SHA-1
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Send the first 5 characters of the hashed password to the HIBP API
    api_url = f'https://api.pwnedpasswords.com/range/{sha1_hash[:5]}'
    response = requests.get(api_url)

    # Check if the remaining hash is in the response
    tail = sha1_hash[5:]

    for line in response.text.split('\n'):
        suffix, count = line.split(':')
        if tail == suffix:
            # Return the count and breached site name
            return int(count), suffix

    return 0, None

def check_password_strength_terminal():
    user_password = input("Enter Password: ")
    print(" ")

    # Check if the password has been previously leaked
    count, suffix = check_password_breaches(user_password)
    if count > 0:
        print(f"{Fore.RED}Warning: This password has been previously leaked {count} times in breaches.{Style.RESET_ALL}")
        print("Choose a different password.\n")
        #return  # Exit the function if the password is breached
    else:
        print("This password has not been previously leaked.\n")

    # Check password length
    password_length = len(user_password)

    # Check and display password strength
    strength = password_strength(user_password)
    checkmarks = character_checkmarks(user_password)
    time_to_crack = calculate_time_to_crack(user_password)

    # Additional feature: Password audit check
    if password_length > 12 and any(char.isupper() for char in user_password) and any(char.islower() for char in user_password) and any(char.isdigit() for char in user_password) and any(char in string.punctuation for char in user_password):
        print(f"Audit: {Fore.GREEN}Pass{Style.RESET_ALL}")
    else:
        audit_fail_reason = f"Audit: {Fore.RED}Fail{Style.RESET_ALL}\nReason: "
        if password_length <= 12:
            audit_fail_reason += "Password length should be more than 12 characters."
        else:
            missing_char_types = [char_type for char_type, check in zip(['Uppercase', 'Lowercase', 'Numbers', 'Symbols'], [any(char.isupper() for char in user_password), any(char.islower() for char in user_password), any(char.isdigit() for char in user_password), any(char in string.punctuation for char in user_password)]) if not check]
            audit_fail_reason += f"Password should include {', '.join(missing_char_types)}."
        
        print(f"{Fore.RED}{audit_fail_reason}{Style.RESET_ALL}\n")

    print(f"\nPassword Strength: {Fore.GREEN}{strength}{Style.RESET_ALL}\n"
          f"Password Length: {password_length} characters\n\n"
          f"Character Checkmarks:\n"
          f"Uppercase: {checkmarks[0]}\n"
          f"Lowercase: {checkmarks[1]}\n"
          f"Numbers: {checkmarks[2]}\n"
          f"Symbols: {checkmarks[3]}\n\n"
          f"Time to Crack: {time_to_crack}")

# Run the modified password strength checker in the terminal
check_password_strength_terminal()