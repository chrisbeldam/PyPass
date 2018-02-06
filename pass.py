from random import choice
from string import ascii_uppercase, digits

# ask user if they want to generate a new password
def generate_password():
    new_pass_gen = input("Do you wish to generate a new password?(Y/N): ").upper()
    if new_pass_gen == "Y":
        # find out the length of the password
        new_pass_length = input("What length combination of letters and digits would you like your password to be?: ")
        # generate a random combination of letters based on their specified length
        new_password = ''.join(choice(ascii_uppercase + digits) for i in range(int(new_pass_length)))
        print("Your new password is:" + " " + new_password)
        # ask if they want to save the password to a text file
        save_to_file = input("Do you wish to save this to a text file?(Y/N): ").upper()
        if save_to_file == "Y":
            write_password_to_file(new_password)
            print("Your password has been saved to : " + "passwords.txt")
        view_passwords = input("Do you want to view your current passwords?(Y/N): ").upper()
        if view_passwords == "Y":
            view_current_passwords()
        more_passwords = input("Do you wish to create another password?(Y/N): ").upper()
        if more_passwords == "Y":
            generate_password()
    else:
        print("Here are you current passwords")
        view_current_passwords()

def write_password_to_file(new_password):
    with open('passwords.txt', 'w') as password:
        password.write(new_password + '\n')

def view_current_passwords():
    file = open('passwords.text', 'r')
    print(file.read())
    pass

generate_password()