# R7

## R7.1 Purpose: Command invalid if the user has not logged in

Program Inputs:

login, test@test.com, test_password, logout

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Not Logged In.

  

## R7.2 Purpose: Invalidate login user and go back to the landing session/screen

Program Inputs:

login, test@test.com, test_password, logout

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Successfully logged out.

/landing
