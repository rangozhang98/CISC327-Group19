# R4
## R4.1
### Command invalid if the user has not logged in
### Purpose: Test that command doesn't run without login

Program Inputs:
`sell`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Command is invalid. You must log in to use it.`

## R4.2
### Starts a ticket selling session
### Purpose: Test that sell session starts with command

Program Inputs:
`login, test@test.com, test_password, sell`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Session was created successfully.`

## R4.3
### Should ask for ticket name, price, quantity, date
### Purpose: Test that program asks for these arguments

Program Inputs:
`none`

Expected Tails of stdout Program Output (match the last several lines of program output):

`To sell, enter the ticket name, price, quantity, and date.`

## R4.4
### The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

## R4.4.1
### Purpose: Test ticket name as alphanumeric (negative case)

Program Inputs:
`login, test@test.com, test_password, sell, ticket_1, 10.23, 300, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket name must be alphanumeric.`

## R4.4.2 
### Purpose: Test that ticket name first/last characters aren't spaces (negative case)

Program Inputs:
`login, test@test.com, test_password, sell, ticket1 , 10.23, 300, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Space cannot be the first or last character in ticket's name.`

## R4.4.3 
### Purpose: Test that valid ticket name is accepted (positive case)

Program Inputs:
`login, test@test.com, test_password, sell, ticketname 1, 10.23, 300, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket was created successfully.`

## R4.5 
### The name of the ticket is no longer than 60 characters

## R4.5.1 
### Purpose: Test if valid ticket name is accepted (negative case)

Program Inputs:
`login, test@test.com, test_password, sell, abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz, 10.23, 300, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket name must not exceed 60 characters.`

## R4.5.2 
### Purpose: Test if valid ticket name is accepted (positive case)

Program Inputs:
`login, test@test.com, test_password, sell, shortname, 10.23, 300, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket was created successfully.`

## R4.6
### The quantity of the tickets has to be more than 0, and less than or equal to 100.

## R4.6.1 
### Purpose: Test for valid ticket quantity (negative case)

Program Inputs:
`login, test@test.com, test_password, sell, ticketname, 10.23, 0, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket quantity must be above 0 and up to 100.`

## R4.6.2 
### Purpose: Test for valid ticket quantity (negative case)

Program Inputs:
`login, test@test.com, test_password, sell, ticketname, 10.23, 101, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket quantity must be above 0 and up to 100.`

## R4.6.3 
### Purpose: Test for valid ticket quantity (positive case)

Program Inputs:
`login, test@test.com, test_password, sell, ticketname, 10.23, 1, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket was created successfully.`

## R4.7
### Price has to be of range [10, 100]

## R4.7.1 
### Purpose: Test for valid ticket price (negative case)

Program Inputs:
`login, test@test.com, test_password, sell, ticketname, 9.99, 1, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket price must be in range [10, 100].`
  
## R4.7.2 
### Purpose: Test for valid ticket price (negative case)

Program Inputs:
`login, test@test.com, test_password, sell, ticketname, 100.1, 1, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket price must be in range [10, 100].`
  
## R4.7.3 
### Purpose: Test for valid ticket price (positive case)

Program Inputs:
`login, test@test.com, test_password, sell, ticketname, 10.50, 1, 20200402`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket was created successfully.`

## R4.8
### Date must be given in the format YYYYMMDD (e.g. 20200901)

## R4.8.1 
### Purpose: Test for valid ticket date (negative case)

Program Inputs:
`login, test@test.com, test_password, sell, ticketname, 10.50, 1, 2020-03-20`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket date must be in the format YYYYMMDD.`

  

## R4.8.2 
### Purpose: Test for valid ticket date (positive case)

Program Inputs:
`login, test@test.com, test_password, sell, ticketname, 10.50, 1, 20200320`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket was created successfully.`

## R4.9
### Append a new registration transaction if successfully sold.

## R4.9.1 
### Purpose: Test that registration transaction is created with successful selling (negative case)

Program Inputs:
`./program_name Kingston ./Invalid_File ./Ticket_Info`

`login, test@test.com, test_password, sell, ticketname, 10.50, 1, 20200320, logout, exit`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Could not create ticket or transaction registration.`
`Logout successful.`
`Exiting program...`

Expected Output File Content:

`none`

## R4.9.2 
### Purpose: Test that registration transaction is created with successful selling (positive case)

Program Inputs:
`./program_name Kingston ./User_Info ./Ticket_Info`

`login, test@test.com, test_password, sell, ticketname, 10.50, 1, 20200320, logout, exit`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Ticket was created successfully.`
`Logout successful.`
`Exiting program...`

Expected Output File Content:

`transaction123, user_name, ticketname, 10.50, 1`

## R4.10 
### For any errors, show an error message
### Purpose: Check if error message is outputted

Program Inputs:
`./program_name Kingston ./Invalid_File ./Ticket_Info`

`login, test@test.com, test_password, sell, ticketname, 10.50, 1, 20200320`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Error: Invalid file name`
`Could not create ticket or transaction registration.`
