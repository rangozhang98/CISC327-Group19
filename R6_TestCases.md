# R6

## R6.1 Purpose: Command invalid if the user has not logged in.

Program Inputs:

login, test@test.com, test_password, update

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Not Logged In.

  
  

## R6.2 Purpose: Starts a ticket selling session

  

Program Inputs:

login, test@test.com, test_password, update

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Session was created successfully.

  

## R6.3 Purpose: Should ask for ticket name, price, quantity and date

  

### R6.3.1 - works

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Enter Ticket Name:

Enter Price:

Enter Quantity:

Enter Date (YYYYMMDD):

### R6.3.2 - doesn’t work

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  

## R6.4 Purpose: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

  

### R6.4.1 - proper ticket

  

Program Inputs:

login, test@test.com, test_password, ticket_name

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

### R6.4.2 - wrong spacing in ticket

  

Program Inputs:

login, test@test.com, test_password, buy, wrong_spacing__ticket_name

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Ticket format is incorrect’

  

### R6.4.3 - not alphanumeric ticket

  

Program Inputs:

login, test@test.com, test_password, buy, programming_ticket_name

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Ticket format is incorrect’

  
  

## R6.5 Purpose: The name of the ticket is no longer than 60 characters

  

### R6.5.1 - correct amount

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, ticket_quantity

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  

### R6.5.2 - more than 60

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, large_ticket_quantity

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Ticket name format is incorrect’

  

## R6.6 Purpose: The quantity of the tickets has to be more than 0, and less than or equal to 100

  

### R6.6.1 - valid amount

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, ticket_quantity

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  

### R6.6.2 - less than 0

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, neg_ticket_quantity

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Quantity format is incorrect’

  
  

### R6.6.3 - more than 100

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, large_ticket_quantity

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Quantity format is incorrect’

## R6.7 Purpose: Price has to be of range [10, 100]

  

### R6.7.1 - valid amount

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, ticket_quantity, ticket_price

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

### R6.7.2 - less than 10

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, ticket_quantity, low_ticket_price

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Price format is incorrect’

  
  

### R6.7.3 - more than 100

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, ticket_quantity, large_ticket_price

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Price format is incorrect’

  
  
  

## R6.8 - Date must be given in the format YYYYMMDD (e.g. 20200901)

  

### R6.8.1 - date correct

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, ticket_quantity, ticket_price, date

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  

### R6.8.2 - incorrect date format

  

Program Inputs:

login, test@test.com, test_password, update, ticket_name, ticket_quantity, ticket_price, wrong_formating_date

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Date format is incorrect’

## R6.9 - Append a new registration transaction if successful.

  

### R6.9.1 - Successful registration

  

Program Inputs:

login, test@test.com, test_password, update, logout, exit

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Registration Transaction successfully created.’

  

Expected Output File Content:

-   transaction_name, user_name, ticket_name, ticket_price, quantity
    

### R6.9.2 - Unsuccessful registration

  

Program Inputs:

login, test@test.com, test_password, update, logout, exit

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  
  

## R6.10 - error message.

  

### R6.10.1 - proper error message

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘{} format is incorrect’

  

### R6.10.2 - not an error message

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none
