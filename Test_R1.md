# R1
## R1.1 
### If logged in, show the menu item buy, sell, update, and logout. Also, print out the user's balance.
### Purpose: Test that appropriate commands and balance are printed

Program Inputs:
`login, test@test.com, test_password`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Your balance is: $____`
`Available commands:`
`/buy`
`/sell`
`/update`
`/logout`

## R1.2 
### If not logged in, show the menu item login, register, and exit.
### Purpose: Test that appropriate commands are printed

Program Inputs:
`none`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Available commands:`
`/login`
`/register`
`/exit`

## R1.3
### The landing screen can take commands and go to corresponding sessions
## R1.3.1 
### Purpose: Test if 'buy' command loads buy session

Program Inputs:
`login, test@test.com, test_password, buy`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Session was created successfully.`

## R1.3.2 
### Purpose: Test if 'sell' command loads sell session

Program Inputs:
`login, test@test.com, test_password, sell`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Session was created successfully.`

## R1.3.3 
### Purpose: Test if 'update' command loads update session

Program Inputs:
`login, test@test.com, test_password, update`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Session was created successfully.`

## R1.3.4 
### Purpose: Test if 'logout' command logs user out

Program Inputs:
`login, test@test.com, test_password, logout`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Logout successful.`

## R1.3.5 
### Purpose: Test if 'login' command loads login session

Program Inputs:
`login`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Session was created successfully.`

## R1.3.6 
### Purpose: Test if 'register' command loads register session

Program Inputs:
`register`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Session was created successfully.`

## R1.3.7 
### Purpose: Test if 'exit' command starts program exit

Program Inputs:
`login, test@test.com, test_password, logout, exit`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Logout successful.`
`Exiting program...`

  

## R1.4
### If not logged in, only login and register commands are accepted
### Purpose: Check that the wrong commands aren't accepted

Program Inputs:
`buy`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Command not accepted. Log in or register to see a list of available commands.`

## R1.5
### If logged in, only buy, sell, and logout commands are accepted
### Purpose: Check that the wrong commands aren't accepted

Program Inputs:
`login, test@test.com, test_password, update`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Command is not accepted at this time.`
