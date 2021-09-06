from time import sleep
import sys
import os
import random

combination_tried = False
player_score = 0
player_name = "User"

# Clears the terminal when called
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# These constants are required for the type writer function
BLACK, RED, GREEN, RED, BLUE, MAGENTA, CYAN, WHITE = range(8)

# Prints a string to the terminal one letter at a time. The default value for text is an empty string to prevent any errors
def type_writer(text = "", colour = WHITE, speed = 0.03):
    for i in text:
        # Don't worry about this code. It's looks a little bit complicated but it seems to work...
        output = "\x1b[1;%dm" % (30+colour) + i + "\x1b[0m"
        sys.stdout.write(output)
        sys.stdout.flush()
        
        # Wait for a fraction of a second before displaying the next letter
        sleep(speed)
   
    sleep(1)
    # Print a blank line after displaying the entire input text
    print("\n")

#  account variables = account name, account number, account balance
account_number = 87654321
account_name = "RICH AF"
account_balance= "54321"
pound_sign = "£"
pound_figures = ".00"
minimum_withdraw = "10"

# my functions =  hello(), enter_pin(), services(), cash_withdraw(), check_account():

def hello():
    print("")
    type_writer("Welcome To Your Own Personal Virtual Cash Machine ", RED, 0.1)
    print("")
    type_writer("Press Y To Continue Or N To Quit", BLUE, 0.1)
    print("")
    ask_hello = input("")
    print("")
    if "y" or "Y" in ask_hello:
        enter_pin()
    elif "N" or "n" in ask_hello:
        hello()
    else:
        hello()

def enter_pin():
    PIN="6789"
    attempt = ""
    attempt_count = 0
    attempt_limit = 3
    used_attempts = False
    type_writer("Enter PIN:",GREEN, 0.1)
    while attempt != PIN and not(used_attempts):

        if attempt_count < attempt_limit:
            attempt = input("")
            attempt_count += 1
        else:
            used_attempts = True

    if used_attempts:
        print("")
        type_writer("Wrong PIN Entered!", RED, 0.1)
        print("")
        print("Maximum Attempts Allowed Reached!", RED, 0.1)
        hello()
    else:
        print("")
        type_writer("Correct PIN Entered", RED, 0.1) 
        print("")
        type_writer("Checking Your Balance, Please Wait... ", RED, 0.1)
        print("")
        type_writer("Your Balance is {}{}{} ".format(pound_sign,account_balance,pound_figures), RED, 0.1)
        print("")
        services()

def services():
    print("")
    type_writer("Which Service Would You Like? 1. or 2.",BLUE, 0.1)
    print("")
    type_writer("1. For Withdrawing Cash ",GREEN, 0.1)
    print("")
    type_writer("2. For Checking Account ",GREEN, 0.1)
    print("")
    ask_service = input("")
    if "1" in ask_service:
        cash_withdraw()
    elif "2" in ask_service:
        check_account()
    else:
        services()

def cash_withdraw():
    print("")
    print("")
    type_writer("How Much Would You Like To Withdraw? ", BLUE, 0.1)
    withdraw_amount = ""
    withdraw_limit = account_balance
    can_withdraw = False
    new_balance = account_balance - withdraw_amount
    print("")
    print("")
    withdraw_amount = input("")
    print("")
    while withdraw_amount < withdraw_limit:
        can_withdraw = True
        if can_withdraw:
            type_writer("Okay, Dispensing {}{}{}, Please Wait... ".format(pound_sign,withdraw_amount,pound_figures), RED, 0.1)
            print("")
            type_writer("Take Your Cash! ", RED, 0.1)
            print("")
            type_writer("Your Balance Is Now {}{}{} ".format(pound_sign,new_balance,pound_figures), RED, 0.1)
            services()
    while withdraw_amount > withdraw_limit:
        can_withdraw = False
        if not(can_withdraw):
            print("")
            type_writer("There Is Only {}{}{} Available In Your Account. ".format(pound_sign,account_balance,pound_figures), RED, 0.1)
            print("")
            cash_withdraw()
    while withdraw_amount < 10: 
        can_withdraw = False
        if not(can_withdraw):
            print("")
            type_writer("The Minimum Amount You Can Withdraw Is {}{}{} ".format(pound_sign,minimum_withdraw,pound_figures), RED, 0.1)
            print("")
            type_writer("There Is {}{}{} Available In Your Account. ".format(pound_sign,account_balance,pound_figures), RED, 0.1)
            cash_withdraw()
    services()

def check_account():
    print("")
    type_writer("Checking Your Account Details, Please Wait... ", RED, 0.1)
    print("")
    type_writer("Account Number: {}".format(account_number), RED, 0.1)
    print("")
    type_writer("Account Name: {}".format(account_name), RED, 0.1)
    print("")
    type_writer("Account Balance: {}{}{}".format(pound_sign,account_balance,pound_figures))
    print("")
    type_writer("Would You Like Another Service? Y or N",BLUE, 0.1)
    print("")
    ask_account = input("")
    print("")
    if "y" or "Y" in ask_account:
        services()
hello()