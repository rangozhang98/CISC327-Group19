import tempfile
from importlib import reload
import os
import io
import sys
import src.main as app

path = os.path.dirname(os.path.abspath(__file__))

#tests all of R4.1 by checking if the output is correct when trying to sell while not logged in
def test_r5_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'buy',
            'exit'
        ],
        input_valid_accounts=['ddd@gmail.com,aaa,aaa45,415.03'],
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
        expected_output_transactions=[
        ]
    )

#tests all of R4.2 by checking if the output is correct when a session starts after a proper login and sell option
def test_r5_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'ddd@gmail.com',
            'aaa45',
            'buy',
            ' ',
            'logout',
            'exit'
        ],
        input_valid_accounts=['ddd@gmail.com,aaa,aaa45,415.03'],
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
            '---BUY---',
            "Enter the ticket name: Ticket name is invalid",
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

#tests all of R4.3 by checking if the output is correct and proper fields are being requested
def test_r5_3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'ddd@gmail.com',
            'aaa45',
            'buy',
            'ticket1',
            '10',
            'logout',
            'exit'
        ],
        input_valid_accounts=['ddd@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=['ticket1,10.00,30,aaa@gmail.com'],
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
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: ---Your balance: $275.03---",
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

#tests all of R4.4 by checking if the output is correct when valid and invalid ticket names are provided
def test_r5_4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'ddd@gmail.com',
            'aaa45',
            'buy',
            ' ',
            'buy',
            '%',
            'buy',
            'oain%wdi',
            'buy',
            'asd ',
            'buy',
            'tick et3',
            '-1',
            'buy',
            'ticket1',
            '10',
            'logout',
            'exit'
        ],
        input_valid_accounts=['ddd@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=['ticket1,10.00,30,aaa@gmail.com', 'tick et3,10.00,30,aaa@gmail.com'],
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
             '---BUY---',
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
             '---BUY---',
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
             '---BUY---',
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
             '---BUY---',
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
             '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: Ticket quantity is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: ---Your balance: $275.03---",
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

#tests all of R4.3 by checking if the output is correct when passed a ticketname of len > 60
def test_r5_5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'ddd@gmail.com',
            'aaa45',
            'buy',
            'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm1',
            'buy',
            'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm',
            '10',
            'logout',
            'exit'
        ],
        input_valid_accounts=['ddd@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=['ticket1,10.00,30,aaa@gmail.com', 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm,10.00,30,aaa@gmail.com'],
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
            '---BUY---',
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: ---Your balance: $275.03---",
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

#tests all of R4.6 by checking if the output is correct when passed invalid quantity numbers
def test_r5_6(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'ddd@gmail.com',
            'aaa45',
            'buy',
            'ticket1',
            '-1',
            'buy',
            'ticket1',
            '101',
            'buy',
            'ticket1',
            '0',
            'buy',
            'ticket1',
            '10',
            'buy',
            'ticket1',
            '20',
            'buy',
            'ticket1',
            '20',
            'logout',
            'exit'
        ],
        input_valid_accounts=['ddd@gmail.com,aaa,aaa45,999415.03'],
        input_valid_tickets=['ticket1,10.00,30,aaa@gmail.com'],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $999415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: Ticket quantity is invalid",
            '---Your balance: $999415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: Ticket quantity is invalid",
            '---Your balance: $999415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: ---Your balance: $999415.03---",
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: ---Your balance: $999275.03---",
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: ---Your balance: $998995.03---",
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: Ticket quantity is invalid",
            '---Your balance: $998995.03---',
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

#tests all of R4.7 by checking if the output is correct when passed prices out of the range
def test_r5_7(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'ddd@gmail.com',
            'aaa45',
            'buy',
            'ticket1',
            '2',
            'buy',
            'ticket1',
            '1',
            'logout',
            'exit'
        ],
        input_valid_accounts=['ddd@gmail.com,aaa,aaa45,15.03'],
        input_valid_tickets=['ticket1,10.00,30,aaa@gmail.com'],
        expected_tail_of_terminal_output=[
            "login",
            "register",
            "exit",
            '---LOG IN---',
            'Enter your email: Enter your password: Account logged in',
            '---Your balance: $15.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: Balance is too low",
            '---Your balance: $15.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: ---Your balance: $1.03---",
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

#tests all of R4.8 by checking if the output is correct when passed a combination of valid and invalid dates
def test_r5_8(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'ddd@gmail.com',
            'aaa45',
            'buy',
            'ticket1',
            '10',
            'logout',
            'exit'
        ],
        input_valid_accounts=['ddd@gmail.com,aaa,aaa45,415.03'],
        input_valid_tickets=['ticket1,10.00,30,aaa@gmail.com'],
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
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: ---Your balance: $275.03---",
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
        input_valid_accounts,
        input_valid_tickets,
        expected_tail_of_terminal_output,
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
    transaction_summary_file = temp_file

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
        #print('output transactions:', content)
        #print('output transactions (expected):', expected_output_transactions)
        
        for ind in range(len(content)):
            assert content[ind] == expected_output_transactions[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
    # remove transaction file
    os.remove(sys.argv[1]+'_transactions.csv')