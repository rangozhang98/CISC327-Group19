import tempfile
from importlib import reload
import os
import io
import sys
import src_backend.backend as app

path = os.path.dirname(os.path.abspath(__file__))

#tests all of R1.1 by checking if the output is correct for when logged in
def test_buy(capsys):
    helper(
        capsys=capsys,
        terminal_input=[],
        input_valid_transactions1=['buy,torontoUser,ticket1,15.00,5'],
        input_valid_transactions2=['buy,torontoUser,ticket2,20.00,20'],
        expected_tail_of_terminal_output=[],
        test_transactions=True,
        expected_output_updatedAccounts=['aaa@gmail.com,aaa,aaa45,415.03', 'www@gmail.com,zzzzz,Zz.45,3000.00', 
        'zzz@gmail.com,zzzzz,Zz.45,3000.00', 'ddd@gmail.com,aaa,aaa45,15.03', 
        'kingston@domain.com,kingstonUser,Kingston1.,3000.00', 'ottawa@gmail.com,ottawaUser,Ottawa3.,3000.00', 
        'toronto@gmail.com,torontoUser,Toronto2.,3000.00'],
        expected_output_updatedTickets=['ticket1,15.00,30,aaa@gmail.com', 'ticket2,20.00,50,bbb@gmail.com']
    )

def test_sell(capsys):
    helper(
        capsys=capsys,
        terminal_input=[],
        input_valid_transactions1=['sell,ottawaUser,ottawaTicket,15.00,50'],
        input_valid_transactions2=['buy,torontoUser,ticket1,15.00,20'],
        expected_tail_of_terminal_output=[],
        test_transactions=True,
        expected_output_updatedAccounts=['aaa@gmail.com,aaa,aaa45,415.03', 'www@gmail.com,zzzzz,Zz.45,3000.00', 
        'zzz@gmail.com,zzzzz,Zz.45,3000.00', 'ddd@gmail.com,aaa,aaa45,15.03', 
        'kingston@domain.com,kingstonUser,Kingston1.,3000.00', 'ottawa@gmail.com,ottawaUser,Ottawa3.,3000.00', 
        'toronto@gmail.com,torontoUser,Toronto2.,3000.00'],
        expected_output_updatedTickets=['ticket1,15.00,30,aaa@gmail.com', 'ticket2,20.00,50,bbb@gmail.com']
    )

def test_registration(capsys):
    helper(
        capsys=capsys,
        terminal_input=[],
        input_valid_transactions1=['registration,torontoUser,toronto@gmail.com,Toronto2.,3000.00'],
        input_valid_transactions2=['buy,torontoUser,ticket1,15.00,20'],
        expected_tail_of_terminal_output=[],
        test_transactions=True,
        expected_output_updatedAccounts=['aaa@gmail.com,aaa,aaa45,415.03', 'www@gmail.com,zzzzz,Zz.45,3000.00', 
        'zzz@gmail.com,zzzzz,Zz.45,3000.00', 'ddd@gmail.com,aaa,aaa45,15.03', 
        'kingston@domain.com,kingstonUser,Kingston1.,3000.00', 'ottawa@gmail.com,ottawaUser,Ottawa3.,3000.00', 
        'toronto@gmail.com,torontoUser,Toronto2.,3000.00'],
        expected_output_updatedTickets=['ticket1,15.00,30,aaa@gmail.com', 'ticket2,20.00,50,bbb@gmail.com']
    )

def helper(
        capsys,
        terminal_input,
        input_valid_transactions1,
        input_valid_transactions2,
        expected_tail_of_terminal_output,
        test_transactions,
        expected_output_updatedAccounts,
        expected_output_updatedTickets
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
    
    temp_fd4, temp_file4 = tempfile.mkstemp()
    valid_transaction_list_file1 = temp_file4
    with open(valid_transaction_list_file1, 'w') as wf:
        wf.write('\n'.join(input_valid_transactions1))

    temp_fd5, temp_file5 = tempfile.mkstemp()
    valid_transaction_list_file2 = temp_file5
    with open(valid_transaction_list_file2, 'w') as wf:
        wf.write('\n'.join(input_valid_transactions2))

    # prepare program parameters
    sys.argv = [
        'backend.py',
        valid_transaction_list_file1,
        valid_transaction_list_file2
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

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]
    
    # compare accounts:
    if test_transactions:
        with open('src_backend/updated_accounts.csv', 'r') as of:
            content = of.read().splitlines()
            
            # print out the testing information for debugging
            # the following print content will only display if a 
            # test case failed:
            print('output accounts:', content)
            print('output accounts (expected):', expected_output_updatedAccounts)
            
            for ind in range(len(content)):
                assert content[ind] == expected_output_updatedAccounts[ind]

    # compare transactions:
    if test_transactions:
        with open('src_backend/updated_tickets.csv', 'r') as of:
            content = of.read().splitlines()
            
            # print out the testing information for debugging
            # the following print content will only display if a 
            # test case failed:
            print('output tickets:', content)
            print('output tickets (expected):', expected_output_updatedTickets)
            
            for ind in range(len(content)):
                assert content[ind] == expected_output_updatedTickets[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
    # remove transaction file
