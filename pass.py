from random import choice
from string import ascii_uppercase, digits

import os

def generate_password():
    print("###### Welcome to PyPass manager ######" + "\n")
    view_passwords = input("Do you want to view your current passwords?(Y/N): ").upper()
    if view_passwords == "Y":
        view_current_passwords()
    # find out the length of the password
    new_pass_length = input("What length combination of letters and digits would you like your new password to be?: ")
    while int(new_pass_length) < 4:
        new_pass_length = input("You need to have at least 4 characters/digits: ")
    # generate a random combination of letters based on their specified length
    new_password = ''.join(choice(ascii_uppercase + digits) for i in range(int(new_pass_length)))
    print("Your new password is:" + " " + new_password)
    assignment_name = input("Please type in what you wish to assign this password to: ").lower()
    # ask if they want to save the password to a text file
    save_to_file = input("Do you wish to save this to a text file?(Y/N): ").upper()
    if save_to_file == "Y":
        write_password_to_file(new_password, assignment_name)
        print(new_password + " " + "Saved")
    more_passwords = input("Do you wish to create another password?(Y/N): ").upper()
    if more_passwords == "Y":
        if os.name != "nt":
            os.system("clear") #Clears screen for mac and linux terminals
            generate_password()
        else:
            os.system("cls")
            generate_password()
        
def write_password_to_file(new_password, assignment_name):
    with open("passwords.txt", "a+") as password:
        password.write(new_password + "-" + assignment_name + "\n")

def view_current_passwords():
    file = open("passwords.txt", "r")
    if os.stat('/home/chris/Development/PyPass/passwords.txt').st_size == 0:
        print("You currently have no passwords" + "\n")
    else:
        print("Here is a list of your current passwords" + "\n")
        print(file.read())
    file.close()

generate_password()