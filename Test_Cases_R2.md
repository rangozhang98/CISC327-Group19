# R2
## R2.1 - Command Invalid if the user has logged in

### R2.1.1 Purpose: Notify user that they need to log in

Program Inputs:

`/login`  

Expected Tails of stdout Program Output (match the last several lines of program output):

`Successfully Logged In.`
`Already logged in.`

## R2.2 - Starts a registration session

### R2.2 Purpose: Test if session is started

Program Inputs:

`/register`

Expected Tails of stdout Program Output (match the last several lines of program output):

`Session was created successfully.`

## R2.3 - Should ask for email, user name, password, password2

### R2.3 Purpose: Asks for the required information

 

Program Inputs:

`/register`

  

Expected Tails of stdout Program Output (match the last several lines of program output):

`Please enter an email, user name, and password to register.`

  

## R2.4 - Email and password cannot both be empty

### R2.4.1 Purpose: Checks if the email and password fields are empty

  

Program Inputs:

`none`

  

Expected Tails of stdout Program Output (match the last several lines of program output):

`Fill in an email and password for registration`

  
  

## R2.5 - Email has to follow addr-spec defined in RFC 5322 (see [https://en.wikipedia.org/wiki/Email_address](https://en.wikipedia.org/wiki/Email_address) for a human-friendly explanation)

### R2.5.1 Purpose: Checks to see if a valid email was presented (single @ sign with a domain after) (Positive Case)

  

Program Inputs:

`Email`

  
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The email entered is valid`

  
  

## R2.6 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character

### R2.6.1 Purpose: Checks if the password is complex enough (Positive Case)

  

Program Inputs:

`Valid Password`

  
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The password you have entered is valid`

### R2.6.1 Purpose: Checks to see if a valid email was presented (single @ sign with a domain after) (Negative Case)

  

Program Inputs:

`Invalid password
`
  
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The password entered is invalid
`
  
  

## R2.7 - Password and Password2 have to be exactly the same

### R2.7.1 Purpose: Checks if the passwords entered are the same (Positive Case)

Program Inputs:

`Password
`
`password2
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The passwords entered are valid and are the same
`
  

### R2.7.2 Purpose: Checks if the passwords entered are the same (Negative Case)

Program Inputs:

`Password
`
`password2
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The passwords entered not the same please try again
`
  
  

## R2.8 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.

### R2.8.1 Purpose: Checks if the user name entered is valid (Positive Case)

Program Inputs:

`User Name
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The user name entered are valid
`
  

### R2.8.2 Purpose: Checks if the user name entered is valid (Negative Case)

Program Inputs:

`User Name
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The user name entered is not valid try again
`
## R2.9 - User name has to be longer than 2 characters and less than 20 characters.

### R2.9.1 Purpose: Checks if the user name entered the correct length (Positive Case)

Program Inputs:

`User Name
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The user name entered are valid
`
  

### R2.9.2 Purpose: Checks if the user name entered is correct length (Negative Case)

Program Inputs:

`User Name
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The user name entered is not valid try again
`
## R2.10 - Email does not exist in the known accounts.

### R2.10.1 Purpose: Checks if the email exists in the database (Positive Case)

Program Inputs:

`email
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The email was found linked to an account
`
  

### R2.10.2 Purpose: Checks if the email exists in the database(Negative Case)

Program Inputs:

`email
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`The email is not linked to an account
`
  

## R2.11 - **For any formatting errors, show message '{} format is incorrect.'.format(the_corresponding_attribute), end the registration session, and print the landing screen**

  

### R2.11.1 Purpose: Prints an error if the format is wrong (positive case)

  

Program Inputs:

`none
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`‘{} format is incorrect.’
`
`‘Session terminated.’
`
`/landing
`
  

### R2.11.2 Purpose: Prints an error if the format is wrong (negative case)

  

Program Inputs:

`none
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`none
`
  
  

## R2.12 - Otherwise, show message 'account registered', end the registration session/process, print the landing screen according to R1
  

### R2.12.1 Purpose: Prints if the account is registered properly (positive case)

  

Program Inputs:

`none
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`‘Account Registered.’
`
`‘Session terminated.’
`
`/landing
`
  

### R2.12.2  Purpose: Prints if the account is registered properly (negative case)

  

Program Inputs:

`none
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`none
`
  

## R2.13 - New account will get a balance of 3000

  

### R2.13.1 Purpose: adds 3000 to the balance of a new account

  

Program Inputs:

`none
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`Balance = 3000
`
`‘New account balance: 3000’
`
  

## R2.14 - Append a new registration transaction if successfully registered.

  

### R2.14.1 Purpose: Creates a registration transaction (positive case)

  

Program Inputs:

`none
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`‘Registration Transaction successfully created.’
`
  

Expected Output File Content:

-   `transaction_name, user_name, user_email, user_password, balance
    `

### R2.14.2 Purpose: Creates a registration transaction (negative case)

  

Program Inputs:

`none
`
  

Expected Tails of stdout Program Output (match the last several lines of program output):

`none`

