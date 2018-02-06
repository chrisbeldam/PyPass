from random import choice
from string import ascii_uppercase, digits

import os

# ask user if they want to generate a new password
def generate_password():
    new_pass_gen = input("Do you wish to generate a password?(Y/N): ").upper()
    if new_pass_gen == "Y":
        # find out the length of the password
        new_pass_length = input("What length combination of letters and digits would you like your password to be?: ")
        # generate a random combination of letters based on their specified length
        new_password = ''.join(choice(ascii_uppercase + digits) for i in range(int(new_pass_length)))
        print("Your new password is:" + " " + new_password)

        assignment = input("Please type in what you wish to assign this password to: ").lower()
        # ask if they want to save the password to a text file
        save_to_file = input("Do you wish to save this to a text file?(Y/N): ").upper()
        if save_to_file == "Y":
            write_password_to_file(new_password, assignment)
            print("Your password has been saved to : " + "passwords.txt")
        view_passwords = input("Do you want to view your current passwords?(Y/N): ").upper()
        if view_passwords == "Y":
            view_current_passwords()
        more_passwords = input("Do you wish to create another password?(Y/N): ").upper()
        if more_passwords == "Y":
            os.system('clear') #Clears screen for mac and linux terminals
            generate_password()
    else:
        view_current_passwords()

def write_password_to_file(new_password, assignment):
    with open('passwords.txt', 'a+') as password:
        password.write(new_password + '-' + assignment + '\n')

def view_current_passwords():
    file = open('passwords.txt', 'r')
    print("Here is a list of your current passwords" + "\n")
    print(file.read())
    file.close()

generate_password()