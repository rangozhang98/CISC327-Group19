import tempfile
from importlib import reload
import os
import io
import sys
import src.main as app

path = os.path.dirname(os.path.abspath(__file__))

#tests all of R1.1 by checking if the output is correct for when logged in
def test_r1_1(capsys):
    """Testing r2. Self-contained (i.e. everything in the code approach)
    [my favorite - all in one place with the code]

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'logout',
            'exit'
        ],
        intput_valid_accounts=[
        ],
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
        expected_output_transactions=[
        ]
    )

#tests all of R1.2 by checking if the output is correct for when not logged in
def test_r1_2(capsys):
    """Testing r2. Self-contained (i.e. everything in the code approach)
    [my favorite - all in one place with the code]

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'exit'
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            'Exiting program'
        ],
        expected_output_transactions=[
        ]
    )

#goes to all pages fails something to get sent back to landing and then goes to another
def test_r1_3(capsys):
    """Testing r2. Self-contained (i.e. everything in the code approach)
    [my favorite - all in one place with the code]

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
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
        intput_valid_accounts=[
        ],
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
        expected_output_transactions=[
        ]
    )

#tests when an invalid input is sent when not logged in
def test_r1_4(capsys):
    """Testing r2. Self-contained (i.e. everything in the code approach)
    [my favorite - all in one place with the code]

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
    helper(
        capsys=capsys,
        terminal_input=[
            'a',
            'exit'
        ],
        intput_valid_accounts=[
        ],
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
        expected_output_transactions=[
        ]
    )

#tests when in invalid input is sent on the login screen
def test_r1_5(capsys):
    """Testing r2. Self-contained (i.e. everything in the code approach)
    [my favorite - all in one place with the code]

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
    """
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
        intput_valid_accounts=[
        ],
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
        expected_output_transactions=[
        ]
    )

def helper(
        capsys,
        terminal_input,
        expected_tail_of_terminal_output,
        intput_valid_accounts,
        expected_output_transactions
):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        intput_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(app)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    valid_account_list_file = temp_file2
    with open(valid_account_list_file, 'w') as wf:
        wf.write('\n'.join(intput_valid_accounts))

    # prepare program parameters
    sys.argv = [
        'main.py',
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
    print('valid accounts:', intput_valid_accounts)
    print('terminal output:', out_lines)
    print('terminal output (expected tail):', expected_tail_of_terminal_output)

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]
    
    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
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
