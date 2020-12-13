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
        a_transactions=['buy,torontoUser,ticket1,15.00,5'],
        b_transactions=['buy,torontoUser,ticket2,20.00,20'],
        expected_tail_of_terminal_output=[],
        expected_output_updatedAccounts=['aaa@gmail.com,aaa,aaa45,415.03', 'www@gmail.com,zzzzz,Zz.45,3000.00', 
        'zzz@gmail.com,zzzzz,Zz.45,3000.00', 'ddd@gmail.com,aaa,aaa45,15.03', 
        'ottawa@gmail.com,ottawaUser,Ottawa3.,3000.00', 
        'toronto@gmail.com,torontoUser,Toronto2.,3000.00'],
        expected_output_updatedTickets=['ticket1,15.00,30,aaa@gmail.com', 'ticket2,20.00,50,bbb@gmail.com']
    )

def test_sell(capsys):
    helper(
        capsys=capsys,
        terminal_input=[],
        a_transactions=['sell,ottawaUser,ottawaTicket,15.00,50'],
        b_transactions=['buy,torontoUser,ticket1,15.00,20'],
        expected_tail_of_terminal_output=[],
        expected_output_updatedAccounts=['aaa@gmail.com,aaa,aaa45,415.03', 'www@gmail.com,zzzzz,Zz.45,3000.00', 
        'zzz@gmail.com,zzzzz,Zz.45,3000.00', 'ddd@gmail.com,aaa,aaa45,15.03', 
        'ottawa@gmail.com,ottawaUser,Ottawa3.,3000.00', 
        'toronto@gmail.com,torontoUser,Toronto2.,3000.00'],
        expected_output_updatedTickets=['ticket1,15.00,30,aaa@gmail.com', 'ticket2,20.00,50,bbb@gmail.com']
    )

def test_registration(capsys):
    helper(
        capsys=capsys,
        terminal_input=[],
        a_transactions=['registration,torontoUser,toronto@gmail.com,Toronto2.,3000.00'],
        b_transactions=['buy,torontoUser,ticket1,15.00,20'],
        expected_tail_of_terminal_output=[],
        expected_output_updatedAccounts=['aaa@gmail.com,aaa,aaa45,415.03', 'www@gmail.com,zzzzz,Zz.45,3000.00', 
        'zzz@gmail.com,zzzzz,Zz.45,3000.00', 'ddd@gmail.com,aaa,aaa45,15.03', 
        'ottawa@gmail.com,ottawaUser,Ottawa3.,3000.00', 
        'toronto@gmail.com,torontoUser,Toronto2.,3000.00'],
        expected_output_updatedTickets=['ticket1,15.00,30,aaa@gmail.com', 'ticket2,20.00,50,bbb@gmail.com']
    )

def helper(
        capsys,
        terminal_input,
        a_transactions,
        b_transactions,
        expected_tail_of_terminal_output,
        expected_output_updatedAccounts,
        expected_output_updatedTickets
):
    # Helper function for testing

    # cleanup package
    reload(app)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()

    
    temp_fd2, temp_file2 = tempfile.mkstemp()
    temp_a_transactions = temp_file2
    with open(temp_a_transactions, 'w') as wf:
        wf.write('\n'.join(a_transactions) + '\n')

    temp_fd3, temp_file3 = tempfile.mkstemp()
    temp_b_transactions = temp_file3
    with open(temp_b_transactions, 'w') as wf:
        wf.write('\n'.join(b_transactions) + '\n')

    # prepare program parameters
    sys.argv = [
        'backend.py',
        temp_a_transactions,
        temp_b_transactions
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
    with open('src_backend/updated_accounts.csv', 'r') as of:
        content = of.read().splitlines()
        
        # print out the testing information for debugging
        # the following print content will only display if a 
            # the following print content will only display if a 
        # the following print content will only display if a 
        # test case failed:
        print('updated accounts:', content)
        print('updated accounts (expected):', expected_output_updatedAccounts)
        
        for ind in range(len(content)):
            assert content[ind] == expected_output_updatedAccounts[ind]

    # compare transactions:
    with open('src_backend/updated_tickets.csv', 'r') as of:
        content = of.read().splitlines()
        
        # print out the testing information for debugging
        # the following print content will only display if a 
        # test case failed:
        print('updated tickets:', content)
        print('updated tickets (expected):', expected_output_updatedTickets)
        
        for ind in range(len(content)):
            assert content[ind] == expected_output_updatedTickets[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
    # remove transaction file
