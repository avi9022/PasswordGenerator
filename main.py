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
        pass
    elif first_input.lower() == 'quit':
        print('Thanks for using "The Password Generator 3000"!')
    else:
        print("Please enter a valid input1!")
        init_program()


def check_password():
    password = input('please type in your password: ')
    is_strong = True

    if len(password) < 8:
        print('Any password should be at least 8 characters long')

    for char in password:
        if char.islower(): break
    else:
        print("Your password should include at least one lower-case character")
        is_strong = False

    for char in password:
        if char.isupper(): break
    else:
        print("Your password should include at least one upper-case character")
        is_strong = False

    for char in password:
        if char.isdigit(): break
    else:
        print("Your password should include at least one digit")
        is_strong = False

    for char in password:
        if not char.isalnum() and not char.isspace(): break
    else:
        print("Your password should include at least one special character")
        is_strong = False

    for char in password:
        if char.isspace(): print("A passwort cant contain space")

    if is_strong:
        print("Good job, your password is strong!")

    init_program()


# main program
init_program()
