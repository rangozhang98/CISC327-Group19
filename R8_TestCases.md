# R8

## R8.1 Purpose: Command invalid if the user has not logged in

Program Inputs:

login, test@test.com, test_password, logout, exit

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Not Logged In.

  

## R8.2 Purpose: Produce output file based on the program output details above.

Program Inputs:

login, test@test.com, test_password, logout, exit

  

Expected Tails of stdout Program Output (match the last several lines of program output):

File successfully created.

  

Expected Output File Content:

-   A file named [office_location]_transactions.csv containing the updated lists below
    
-   Updated list of format:
    

-   User related: transaction_name, user_name, user_email, user_password, balance
    
-   Ticket related: transaction_name, user_name, ticket_name, ticket_price, quantity
