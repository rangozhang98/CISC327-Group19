import tempfile
from importlib import reload
import os
import io
import sys
import src.frontend as app

path = os.path.dirname(os.path.abspath(__file__))

# command invalid if user is logged in
def test_r8_1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            "login",
            'aaa@gmail.com',
            'aaa45',
            'exit',
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

# Produce output file based on the program output details 
def test_r8_2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'register',
            'aaa@gmail.com',
            'aaa',
            'Aa.45',
            'Aa.45',
            "login",
            'account@gmail.com',
            'pass45',
            'buy',
            'ticket1',
            '20',
            'sell',
            'ticket1',
            '10.00',
            '20',
            '20200202',
            'update',
            'ticket1',
            '15',
            '100',
            '20200202',
            'logout',
            'exit'
        ],
        input_valid_accounts=['account@gmail.com,account,pass45,3000.00'],
        input_valid_tickets=['ticket1,10.00,30,aaa@gmail.com'],
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
            '---BUY---',
            "Enter the ticket name: Enter the ticket quantity: ---Your balance: $2720.00---",
            'buy',
            'sell',
            'update',
            'logout',
            '---SELL---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: ---Your balance: $2720.00---",
            'buy',
            'sell',
            'update',
            'logout',
            '---UPDATE---',
            "Enter the ticket name: Enter the ticket price: Enter the ticket quantity: Enter the ticket date: ---Your balance: $2720.00---",
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
        test_transactions=True,
        expected_output_transactions=[
            'registration,aaa,aaa@gmail.com,Aa.45,3000.00',
            'buy,account,ticket1,10.00,20',
            'sell,account,ticket1,10.00,20',
            'update,account,ticket1,15.00,100'
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
