import tempfile
from importlib import reload
import os
import io
import sys
import src.frontend as app

path = os.path.dirname(os.path.abspath(__file__))

#tests all of R3.1 by checking if the command login is invalid if already logged in
def test_r3_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'login',
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

#R3.2 was tested in the landing tests in R1.3 where we tested if landing could send to every session

#tests all of R3.3 by checking if login asks for email and then entering the email and checking if it asks for
#the password then logging out and exiting the program 
def test_r3_3(capsys):
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

#Tests R3.4 which tests if the password or email is invalid and says that and doesnt allow them to login
#First a valid email is entered then an invalid password and it checks the output, then an invalid
#email is entered and it checks for this then exits the program
def test_r3_4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'ddd1#',
            'login',
            '13#!@#$@gmail.com',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=[],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Login failed',
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Login failed',
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        test_transactions=False,
        expected_output_transactions=[]
    )

#R3.4 format checking of the email and password is done in the registration and doesnt allow incorrect 
#formatting to be registered. Felt redundant and unnecesary to make the login function check this and just made the login 
#function check if the email and password are in "accounts.csv".

#Tests R3.6 by logging in and checking if the landing page is correct for when logged in then
#it logsout and exits the program
def test_r3_6(capsys):
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

#R3.7 tests if the login fails but this is already achieved in the test R3.4 where invalid emails and
#passwords are entered which fails the login because the email and password are not in the "accounts.csv"
#file making this test case unnecessary so I chose to skip like Professor Ding said could be done.

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
    print('std.in:', terminal_input)
    print('valid accounts:', input_valid_accounts)
    print('valid tickets:', input_valid_tickets)
    print('terminal output:', out_lines)
    print('terminal output (expected tail):', expected_tail_of_terminal_output)
    
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
