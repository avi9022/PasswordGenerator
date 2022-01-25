import random
import string


def init_program():
    first_input = input("""
Please type in one of these options:
"Check" - to check if your password is strong
"Generate" - to generate  a new password
"Quit" - to quit the program
Your input: """)

    if first_input.lower() == 'check':
        check_password()

    elif first_input.lower() == 'generate':
        print(generate())
        init_program()
    elif first_input.lower() == 'quit':
        print('Thanks for using "The Password Generator 3000"!')
    else:
        print("Please enter a valid input!")
        init_program()


def check_lower(password):
    for char in password:
        if char.islower(): return True
    return False


def check_upper(password):
    for char in password:
        if char.isupper(): return True
    return False


def check_digits(password):
    for char in password:
        if char.isdigit(): return True
    return False


def check_special(password):
    for char in password:
        if not char.isalnum() and not char.isspace(): return True
    return False


def check_space(password):
    for char in password:
        if char.isspace(): return True
    return False


def check_password():
    password = input('please type in your password: ')
    is_strong = True

    if len(password) < 8:
        print('Any password should be at least 8 characters long')

    if not check_lower(password):
        print("Your password should include at least one lower-case character")
        is_strong = False

    if not check_upper(password):
        print("Your password should include at least one upper-case character")
        is_strong = False

    if not check_digits(password):
        print("Your password should include at least one digit")
        is_strong = False

    if not check_special(password):
        print("Your password should include at least one special character")
        is_strong = False

    if is_strong:
        print("Good job, your password is strong!")

    init_program()


def check_for_enough_space(chars, num):
    chars_needed_to_add = 0
    if not check_lower(chars): chars_needed_to_add += 1
    if not check_upper(chars): chars_needed_to_add += 1
    if not check_digits(chars): chars_needed_to_add += 1
    if not check_special(chars): chars_needed_to_add += 1
    if num - len(chars) < chars_needed_to_add:
        return False
    else:
        return True


def generate():
    new_password = ""
    # check for valid password length
    while True:
        try:
            num_of_digits = int(input("Please type how long would you like the password to be: "))
        except ValueError:
            print("Please input a valid answer!")
            continue
        if num_of_digits < 8 or num_of_digits > 15:
            print("A strong password should be at least 8 characters and up to 15!")
            continue
        else:
            break

    while True:
        asked_chars = input("please enter all the characters that must be included: ")
        if check_space(asked_chars):
            print("A password cant contain space")
            continue
        if not check_for_enough_space(asked_chars, num_of_digits):
            print("There isn't enough room to add all the necessary characters for a strong password!")
            continue
        new_password += asked_chars
        break

    if not check_lower(new_password):
        new_password += random.choice(string.ascii_lowercase)
    if not check_upper(new_password):
        new_password += random.choice(string.ascii_uppercase)
    if not check_digits(new_password):
        new_password += random.choice(string.digits)
    if not check_special(new_password):
        new_password += random.choice(string.punctuation)

    while len(new_password) < num_of_digits:
        new_password += random.choice(string.ascii_letters)

    # randomizing the characters in the new  password
    char_list = list(new_password)
    random.shuffle(char_list)
    new_password = ''.join(char_list)

    return new_password


# main program
init_program()
