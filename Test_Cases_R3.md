# R3

## R3.1 Purpose: Command invalid if the user has logged in.

Program Inputs:

login, test@test.com, test_password

Expected Tails of stdout Program Output (match the last several lines of program output):

Successfully Logged In.

Already logged in.


Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

## R3.2 Purpose: Starts a login session

  

Program Inputs:

login, test@test.com, test_password

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Session was created successfully.

  
  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

## R3.3 Purpose: Should ask for email and password

  

### R3.3.1 - works

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Enter Email:

Enter Password:

  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

### R3.3.2 - doesn’t work

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

## R3.4 Purpose: email, password all have to satisfy the same required as defined in R1

  

### R3.4.1 - proper email and password

  

Program Inputs:

login, test@test.com, test_password

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Login Successful.

  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

### R3.4.2 - proper email, wrong password

  

Program Inputs:

login, test@test.com, wrong_test_password

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Login Failed.

‘Password format is incorrect’

  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

### R3.4.3 - proper password, wrong email

  

Program Inputs:

login, test.test.com, test_password

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Login Failed.

‘Email format is incorrect’

  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

### R3.4.4 - wrong email and password

  

Program Inputs:

login, test.test.com, wrong_test_password

  

Expected Tails of stdout Program Output (match the last several lines of program output):

Login Failed.

‘Email format is incorrect’

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

## R3.5 Purpose: For any formatting errors, show message '{} format is incorrect.'.format(the_corresponding_attribute), end the login session, and print the landing screen

  

### R3.5.1 - works

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘{} format is incorrect.’

  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

### R3.5.2 - doesn’t work

  

Program Inputs:

none

  

Expected Tails of stdout Program Output (match the last several lines of program output):

none

  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

## R3.6 Purpose: If email/password are correct, show message 'account logged in', end the login session/process, and print the landing screen according to R1

  
  

Program Inputs:

login, test@test.com, test_password

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Account logged in’

Session terminated.

/landing

  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    

## R3.7 - Otherwise, show message 'login failed', end login session/process, and print the landing screen according to R1

  

Program Inputs:

login, test.test.com, wrong_test_password

  

Expected Tails of stdout Program Output (match the last several lines of program output):

‘Login failed’

Session terminated.

/landing

  

Expected Output File Content:

-   Not applicable to this requirement. (but will be used for other requirements)
    
