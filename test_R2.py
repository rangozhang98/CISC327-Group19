import tempfile
from importlib import reload
import os
import io
import sys
import src.main as app

path = os.path.dirname(os.path.abspath(__file__))

#tests all of R1.1 by checking if the output is correct for when logged in
def test_r1_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Logout successful',
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

#tests all of R1.2 by checking if the output is correct for when not logged in
def test_r1_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

#goes to all pages fails something to get sent back to landing and then goes to another
def test_r1_3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            '123',
            "login",
            'aaa@gmail.com',
            'aaa45',
            'buy',
            ' ',
            'sell',
            ' ',
            'update',
            '%',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: '
            'Email format is incorrect',
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            "---BUY---",
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---UPDATE---',
            'Enter the ticket name: Name is invalid',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Logout successful',
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

#tests when an invalid input is sent when not logged in
def test_r1_4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'a',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            "Command invalid",
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

#tests when in invalid input is sent on the login screen
def test_r1_5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'a',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Command invalid',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Logout successful',
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

#test that command invalid when user is logged in
def test_r2_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'register',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Command invalid',
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            'Logout successful',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# start registration if command is valid
def test_r2_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            ' ',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# should ask for email, user name, password, password2
def test_r2_3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'zzz@gmail.com',
            'zzzzz',
            'Zz.45',
            'Zz.45',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Confirm your password: Account registered',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# email can't be empty
def test_r2_4_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            '',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# password can't be empty
def test_r2_4_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'zzz@gmail.com',
            'zzzzz',
            '',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Password format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# email must have local part, @, and domain (negative)
def test_r2_5_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'gmail.com',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# email must have local part, @, and domain (positive)
def test_r2_5_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'zzz@gmail.com',
            '%',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# email local part can only have alphanumeric or symbols !#$%&'*+-/=?^_`{|}~ (positive)
def test_r2_5_3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'a123!b123*@gmail.com',
            '',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# email local part can only have alphanumeric or symbols !#$%&'*+-/=?^_`{|}~ (negative)
def test_r2_5_4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'a123[b123]@gmail.com',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# email local part can't have consecutive .
def test_r2_5_5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'a..b@gmail.com',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# email local part can't start/end with a .
def test_r2_5_6(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            '.aaa@gmail.com',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# email local part can't start/end with a .
def test_r2_5_7(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa.@gmail.com',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# email local part can have . if they're not on the edge or consecutive
def test_r2_5_8(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'a.aa@gmail.com',
            '',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# domain must be alphanumeric (negative) 
def test_r2_5_9(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail$com',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# domain must be separated by .
def test_r2_5_10(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@maps.google.com',
            '',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# domain can't start/end with -
def test_r2_5_11(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@-gmail.com',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# domain can't start/end with -
def test_r2_5_12(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com-',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# domain can't start/end with - (positive)
def test_r2_5_13(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail-com',
            '',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# domain can't be blank
def test_r2_5_14(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# local part can't be blank
def test_r2_5_15(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            '@gmail.com',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# password can't be under 6 chars
def test_r2_6_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaaaa',
            'Aa.4',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Password format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# password must have at least one uppercase, lowercase, and special char from !#$%&'*+-/=?^_`{|}~
def test_r2_6_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaaaa',
            'aa.45',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Password format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# password must have at least one uppercase, lowercase, and special char from !#$%&'*+-/=?^_`{|}~
def test_r2_6_3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaaaa',
            'AA.45',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Password format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# password must have at least one uppercase, lowercase, and special char from !#$%&'*+-/=?^_`{|}~
def test_r2_6_4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaaaa',
            'Aaa45',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Password format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# passwords can't be different
def test_r2_7(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaaaa',
            'Aa.45',
            'aa.45',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Confirm your password: Passwords do not match',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# username can't be empty
def test_r2_8_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            '',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# Username can't have non-alphanumeric non-space chars
def test_r2_8_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaaa!',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# Username can't start/end with space
def test_r2_8_3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            ' aaa',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# Username can't start/end with space
def test_r2_8_4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaa ',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# Username can have space inside it, not at start/end
def test_r2_8_5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'A Aa',
            '',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Password format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# Username must be longer than 2 chars
def test_r2_9_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aa',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# Username must be shorter than 20 chars
def test_r2_9_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaaaaaaaaaaaaaaaaaaa',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Username format is incorrect',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# Email can't exist in account list
def test_r2_10(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Email already exists',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# If everything is correct, show message 'account registered' and print landing screen
def test_r2_12(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaa',
            'Aa.45',
            'Aa.45',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Confirm your password: Account registered',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# New account gets a balance of 3000
def test_r2_13(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaa',
            'Aa.45',
            'Aa.45',
            'login',
            'aaa@gmail.com',
            'Aa.45',
            'logout',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Confirm your password: Account registered',
            'login',
            'register',
            'exit',
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $3000.00---',
            'buy',
            'sell',
            'update',
            'logout',
            'Logout successful',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

# Append a registration transaction if succesfully registered
def test_r2_14(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaa',
            'Aa.45',
            'Aa.45',
            'exit'
        ],
        input_valid_accounts=[],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---REGISTER---',
            'Enter an email: Enter a username: Enter a password: Confirm your password: Account registered',
            'login',
            'register',
            'exit',
            'Exiting program'
        ],
        test_transactions=True,
        expected_output_transactions=['registration,aaa,aaa@gmail.com,Aa.45,3000.00']
    )

def helper(
        capsys,
        terminal_input,
        input_valid_accounts,
        input_valid_tickets,
        expected_tail_of_terminal_output,
        test_transactions,
        expected_output_transactions
):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        input_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(app)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    valid_account_list_file = temp_file2
    with open(valid_account_list_file, 'w') as wf:
        wf.write('\n'.join(input_valid_accounts))

    # temp file to store ticket list
    temp_fd3, temp_file3 = tempfile.mkstemp()
    valid_ticket_list_file = temp_file3
    with open(valid_ticket_list_file, 'w') as wf:
        wf.write('\n'.join(input_valid_tickets))

    # prepare program parameters
    sys.argv = [
        'main.py',
        'testCity',
        valid_account_list_file,
        valid_ticket_list_file
    ]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # print out the testing information for debugging
    # the following print content will only display if a 
    # test case failed:
    # print('std.in:', terminal_input)
    # print('valid accounts:', input_valid_accounts)
    # print('valid tickets:', input_valid_tickets)
    # print('terminal output:', out_lines)
    # print('terminal output (expected tail):', expected_tail_of_terminal_output)

    #----------
    print()
    print('STD.IN:', terminal_input)
    print('VALID ACCOUNTS:', input_valid_accounts)
    print('VALID TICKETS: ', input_valid_tickets)
    print()
    # formatted output comparison
    outLen = len(out_lines)
    expLen = len(expected_tail_of_terminal_output)
    endInd = outLen-expLen
    formatShort = '\033[91m'+'{:<1s}'+'\x1b[0m'+'{:<35.34s}{:<35.35s}'
    formatLong = '\033[91m'+'{:<1s}'+'\x1b[0m'+'{:<80.79s}{:<80}'
    
    #CHANGE FormatShort to FormatLong if outputs are cut off. Widen the console.
    formatStr = formatLong
    #
    print(formatStr.format('', 'EXPECTED:', 'STD.OUT:'))
    print('===============================================')
    if (endInd > 0):
        for i in range(expLen):
            print(formatStr.format('' if expected_tail_of_terminal_output[i] == out_lines[i] else '*', expected_tail_of_terminal_output[i], out_lines[i]))
        for o in range(expLen, outLen):
            print(formatStr.format('', '', out_lines[o]))
    elif (endInd < 0):
        for i in range(outLen):
            print(formatStr.format('' if expected_tail_of_terminal_output[i] == out_lines[i] else '*', expected_tail_of_terminal_output[i], out_lines[i]))
        for e in range(outLen, expLan):
            print(formatStr.format('', expected_tail_of_terminal_output[i], ''))
    else:
        for i in range(outLen):
            print(formatStr.format('' if expected_tail_of_terminal_output[i] == out_lines[i] else '*', expected_tail_of_terminal_output[i], out_lines[i]))
   #-----------

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]
    
    # compare transactions:
    if test_transactions:
        with open(sys.argv[1]+'_transactions.csv', 'r') as of:
            content = of.read().splitlines()
            
            # print out the testing information for debugging
            # the following print content will only display if a 
            # test case failed:
            print('output transactions:', content)
            print('output transactions (expected):', expected_output_transactions)
            
            for ind in range(len(content)):
                assert content[ind] == expected_output_transactions[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
    # remove transaction file
    os.remove(sys.argv[1]+'_transactions.csv')