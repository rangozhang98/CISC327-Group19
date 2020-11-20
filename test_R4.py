import tempfile
from importlib import reload
import os
import io
import sys
import src.main as app

path = os.path.dirname(os.path.abspath(__file__))

#tests all of R4.1 by checking if the output is correct when trying to sell while not logged in
def test_r4_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'sell',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
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
        expected_output_transactions=[
        ]
    )

#tests all of R4.2 by checking if the output is correct when a session starts after a proper login and sell option
def test_r4_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'sell',
            ' ',
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
            '---SELL---',
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
        test_transactions=False,
        expected_output_transactions=[
        ]
    )

#tests all of R4.3 by checking if the output is correct and proper fields are being requested
def test_r4_3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'sell',
            'ticket1',
            '10',
            '5',
            '20200101',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
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
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: ---Your balance: $415.03---",
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
        expected_output_transactions=[
        ]
    )

#tests all of R4.4 by checking if the output is correct when valid and invalid ticket names are provided
def test_r4_4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'sell',
            ' ',
            'sell',
            '%',
            'sell',
            'oain%wdi',
            'sell',
            'asd ',
            'sell',
            'tick et3',
            '5',
            'sell',
            'ticket1',
            '10',
            '5',
            '20200101',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
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
             '---SELL---',
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
             '---SELL---',
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
             '---SELL---',
            "Enter the ticket name: Enter the ticket price: Ticket price is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: ---Your balance: $415.03---",
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
        expected_output_transactions=[
        ]
    )

#tests all of R4.3 by checking if the output is correct when passed a ticketname of len > 60
def test_r4_5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'sell',
            'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm1',
            'sell',
            'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm',
            '10',
            '5',
            '20200101',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
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
            '---SELL---',
            "Enter the ticket name: Ticket name is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: ---Your balance: $415.03---",
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
        expected_output_transactions=[
        ]
    )

#tests all of R4.6 by checking if the output is correct when passed invalid quantity numbers
def test_r4_6(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'sell',
            'ticket1',
            '10',
            '-1',
            'sell',
            'ticket1',
            '10',
            '101',
            'sell',
            'ticket1',
            '10',
            '0',
            'a',
            'sell',
            'ticket1',
            '10',
            '100',
            'a',
            'sell',
            'ticket1',
            '10',
            '5',
            '20200101',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
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
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Ticket quantity is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Ticket quantity is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: ---Your balance: $415.03---",
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
        expected_output_transactions=[
        ]
    )

#tests all of R4.7 by checking if the output is correct when passed prices out of the range
def test_r4_7(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'sell',
            'ticket1',
            '-1',
            'sell',
            'ticket1',
            '5',
            'sell',
            'ticket1',
            '101',
            'sell',
            'ticket1',
            '100',
            '-1',
            'sell',
            'ticket1',
            '10',
            '-1',
            'sell',
            'ticket1',
            '20',
            '5',
            '20200101',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
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
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Ticket price is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Ticket price is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Ticket price is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Ticket quantity is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Ticket quantity is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: ---Your balance: $415.03---",
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
        expected_output_transactions=[
        ]
    )

#tests all of R4.8 by checking if the output is correct when passed a combination of valid and invalid dates
def test_r4_8(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'sell',
            'ticket1',
            '10',
            '5',
            'Oct82020',
            'sell',
            'ticket1',
            '10',
            '5',
            '01012020',
            'sell',
            'ticket1',
            '10',
            '5',
            'Oct 08, 2020',
            'sell',
            'ticket1',
            '10',
            '5',
            '20201604',
            'sell',
            'ticket1',
            '10',
            '5',
            '20200132',
            'sell',
            'ticket1',
            '10',
            '5',
            '20190229',
            'sell',
            'ticket1',
            '10',
            '5',
            '20210101',
            'sell',
            'ticket1',
            '10',
            '5',
            '20200431',
            'sell',
            'ticket1',
            '10',
            '5',
            '20200229',
            'sell',
            'ticket1',
            '10',
            '5',
            '20200101',
            'logout',
            'exit'
        ],
        input_valid_accounts=['aaa@gmail.com,aaa,aaa45,415.03'],
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
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: Ticket date is invalid",
            '---Your balance: $415.03---',
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: ---Your balance: $415.03---",
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: ---Your balance: $415.03---",
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
        expected_output_transactions=[
        ]
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