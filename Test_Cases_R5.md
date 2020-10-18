# R5

## R5.1 Purpose: Command invalid if the user has not logged in.

Program Inputs:

login, test@test.com, test_password, buy

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Not Logged In.

## R5.2 Purpose: Starts a ticket selling session

  

Program Inputs:

login, test@test.com, test_password, buy

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Session was created successfully.

## R5.3 Purpose: Should ask for ticket name and quantity

  

### R5.3.1 - works

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Enter Ticket Name:

Enter Quantity:

  

### R5.3.2 - doesn’t work

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  

## R5.4 Purpose: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

  

### R5.4.1 - proper ticket

  

Program Inputs:

login, test@test.com, test_password, buy, ticket_name

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

### R5.4.2 - wrong spacing in ticket

  

Program Inputs:

login, test@test.com, test_password, buy, ticket_name_but_with_bad_spacing

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Ticket format is incorrect’

  

### R5.4.3 - not alphanumeric ticket

  

Program Inputs:

login, test@test.com, test_password, buy, ticket_name_but_not_alphanumeric

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Ticket format is incorrect’

  
  

## R5.5 Purpose: The name of the ticket is no longer than 60 characters

  

### R5.5.1 - correct amount

  

Program Inputs:

login, test@test.com, test_password, buy, ticket_name

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  

### R5.5.2 - more than 60

  

Program Inputs:

login, test@test.com, test_password, buy, ticket_name_but_longer

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Ticket name format is incorrect’

  

## R5.6 Purpose: The quantity of the tickets has to be more than 0, and less than or equal to the available quantity

  

### R5.6.1 - valid amount

  

Program Inputs:

login, test@test.com, test_password, buy, ticketname, quantity

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  

### R5.6.2 - less than 0

  

Program Inputs:

login, test@test.com, test_password, buy, ticket_name, neg_quantity

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Quantity format is incorrect’

  
  

### R5.6.3 - more than available amount

  

Program Inputs:

login, test@test.com, test_password, buy, ticket_name, large_ticket_quantity

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Quantity format is incorrect’

## R5.7 - The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)

  

### R5.7.1 - has enough balance

  

Program Inputs:

login, test@test.com, test_password, buy, ticket_name, quantity, account_balance

  

Expected Tails of stdout Program Output (match the last several lines of program output):

True

  

### R5.7.2 - does not have enough balance

  

Program Inputs:

  

login, test@test.com, test_password, buy, ticket_name, quantity, invalid_balance

  

Expected Tails of stdout Program Output (match the last several lines of program output):

False

## R5.8 - Append a new registration transaction if successful.

  

### R5.8.1 - transaction successful

  

Program Inputs:

./program_name Kingston ./User_Info ./Ticket_Info

login, test@test.com, test_password, buy, ticket_name, quantity, account_balance, logout, exit

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Registration Transaction successfully created.’

  

Expected Output File Content:

-   transaction_name, user_name, ticket_name, ticket_price, quantity
    

### R5.8.2 - transaction unsuccessful

  

Program Inputs:

./program_name Kingston ./User_Info ./Ticket_Info

login, test@test.com, test_password, buy, ticket_name, quantity, account_balance, logout, exit

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  
  

## R5.9 - error message

  

### R5.9.1 - proper error message

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘{} format is incorrect’

  

### R5.9.2 - not an error message

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none
