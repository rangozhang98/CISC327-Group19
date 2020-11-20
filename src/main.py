# to get command line arguments
import sys
# sleep function to pause before changing the console text
from time import sleep
# function clears the console using the appropriate OS's keywords
from os import system
from os import name
clear = lambda: system('cls' if name=='nt' else 'clear')

# boolean to track if user is logged in
loggedIn = False
# user's account details
userInfo = {"username": "", "balance": -1, "email": ""}
# office location, used in transaction file's name
location = "kingston"
# string that collects transactions to write to file when user exits
runningTransactions = ""
# paths of account and ticket list files used for this program
accountsPath = "src/accounts.csv"
ticketsPath = "src/tickets.csv"


# main method, program must be run with args (location, accountsPath, ticketsPath) in command line
def main():
    try:
        # set up global vars for office location and file paths
        global location, accountsPath, ticketsPath
        location = sys.argv[1]
        accountsPath = sys.argv[2]
        ticketsPath = sys.argv[3]
        # go to landing page
        landing()
    except:
        # instruct user how to run the program if arguments are wrong
        print("Program needs arguments: {location} {accountsPath} {ticketsPath}")


# method controls the landing page
def landing():
    #sleep(1.5)
    clear()
    if loggedIn:
        global userInfo
        # print menu screen
        print("---Your balance: $%.2f---\nbuy\nsell\nupdate\nlogout" % userInfo["balance"])
        # call methods according to user's input command
        menuSelection = input()
        if menuSelection == "buy":
            buy()
        elif menuSelection == "sell":
            sell()
        elif menuSelection == "update":
            update()
        elif menuSelection == "logout":
            logout()
        else:
            print("Command invalid")
            landing()
    else:
        # print menu screen
        print("login\nregister\nexit")
        menuSelection = input()
        if menuSelection == "login":
            login()
        elif menuSelection == "register":
            register()
        elif menuSelection == "exit":
            exit()
        else:
            print("Command invalid")
            landing()

# method registers new account info into account file
def register():
    if loggedIn: 
        print("Command invalid")
        landing()
        return
    clear()

    print("---REGISTER---")
    email = input("Enter an email: ")
    validEmail = True
    try:
        # email must have 2 parts
        localpart, domain = email.split('@')

        # email local part can't be blank or start/end with a period
        if len(localpart) > 0 and localpart[0] != '.' and localpart[-1] != '.':
            for i in range(len(localpart)):
                c = localpart[i]
                # invalid if char is a consecutive period, or isn't alpha-nummeric or !#%&'*+-/=?^_`{|}~
                if not c.isalnum() and not c in "!#%&'*+-/=?^_`{|}~" and not (c == '.' and localpart[i-1] != '.' and localpart[i+1] != '.'):
                    validEmail = False
                    break
        else:
            validEmail = False

        # domain can't be blank, or start/end with a period/hyphen
        if len(domain) > 0 and domain[0] != '.' and domain[0] != '-' and domain[-1] != '.' and domain[-1] != '-':
            for i in range(len(domain)):
                c = domain[i]
                # invalid if char is a consecutive period or isn't alpha-numeric
                if not c.isalnum() and not c == '.' and not c == '-':
                    validEmail = False
                    break
        else:
            validEmail = False
    except:
        # format is wrong if email couldn't be parsed
        validEmail = False

    if not validEmail:
        print("Email format is incorrect")
        landing()
        return

    # check that this email isn't already registered
    emailExists = False
    file = open(accountsPath, "r")
    for line in file:
        values = line.split(',')
        if values[0] == email:
            emailExists = True
            break
    if emailExists:
        print("Email already exists")
        landing()
        return
        
    username = input("Enter a username: ")
    # username is limited to 2-20 chars, alphanumeric, and doesn't start/end with a space
    if len(username) <= 2 or len(username) >= 20 or not username.isalnum() or username[0] == ' ' or username[-1] == ' ':
        print("Username format is incorrect")
        landing()
        return

    validPass = False
    password = input("Enter a password: ")
    # password minimum length is 5
    if len(password) >= 5:
        # scan for at least one uppercase, lowercase, and special character
        upper = False
        lower = False
        special = False
        for c in password:
            if c.isupper(): upper = True
            elif c.islower(): lower = True
            elif c in ".!#%&'*+-/=?^_`{|}~": special = True
        if upper == True and lower == True and special == True:
            validPass = True
    if not validPass:
        print("Password format is incorrect")
        landing()
        return
            
    pass2 = input("Confirm your password: ")
    if password != pass2:
        print("Passwords do not match")
        landing()
        return
    
    balance = 3000

    # add account to file
    accounts = open(accountsPath, "a")
    accounts.write("%s,%s,%s,%.2f\n" % (email, username, password, balance))
    accounts.close()
    # add transaction to running total
    global runningTransactions
    runningTransactions += "registration,%s,%s,%s,%.2f\n" % (username, email, password, balance)

    print("Account registered")
    landing()

# method logs user in with credentials from accounts list
def login():
    # can't be logged in already
    global loggedIn
    if not loggedIn:
        clear()
        print("---LOG IN---")
        email = input("Enter your email: ")
        # for every account in the file, check for matching email
        file = open(accountsPath, "r")
        for line in file:
            values = line.split(',')
            # when match is found for email, as for password
            if email == values[0]:
                # get password as input
                password = input("Enter your password: ")
                # if password is correct, set user to logged in
                if password == values[2]:
                    print("Account logged in")
                    global userInfo
                    loggedIn = True
                    # set user's info 
                    userInfo["username"] = values[1]
                    userInfo["balance"] = float(values[3])
                    userInfo["email"] = email
                    break
        if not loggedIn:
            print("Login failed")
    else:
        print("Command invalid")
    landing()

# method lets user sell tickets
def sell():
    if loggedIn:
        clear()
        print("---SELL---")
        ticketName = input("Enter the ticket name: ")
        validName = False
        # name must be alpha-numeric, not over 60 chars, and can't start/end with a space
        if len(ticketName) <= 60 and ticketName.isalnum() and ticketName[0] != ' ' and ticketName[-1] != ' ':
            validName = True
            #for c in ticketName:
                #if c != ' ':
                    #validName = False
        elif len(ticketName) <= 60 and not ticketName.isalnum() and ticketName[0] != ' ' and ticketName[-1] != ' ':
            tempTicket = ""
            for c in ticketName:
                if c != ' ':
                    tempTicket += c
            if tempTicket.isalnum():
                validName = True
        else:
            validName = False
        if not validName:
            print("Ticket name is invalid")
            landing()
            return

        # price must be in range [10:100]
        ticketPrice = float(input("Enter the ticket price: "))
        if ticketPrice < 10 or ticketPrice > 100:
            print("Ticket price is invalid")
            landing()
            return
        # quantity must be in range [0:100]
        ticketQuantity = int(input("Enter the ticket quantity: "))
        if ticketQuantity < 0 or ticketQuantity > 100:
            print("Ticket quantity is invalid")
            landing()
            return
        # date must be in format YYYYMMDD
        ticketDate = input("Enter the ticket date: ")
        monthsA = [1, 3, 5, 7, 8, 10, 12]
        monthsB = [4, 6, 9, 11]
        if ticketDate.isnumeric():
            if len(ticketDate) != 8 or int(ticketDate[:4]) > 2020 or int(ticketDate[4:6]) > 12 or int(ticketDate[4:6]) < 0:
                    print("Ticket date is invalid")
                    landing()
                    return
            else:
                if  int(ticketDate[4:6]) in monthsA and int(ticketDate[6:]) > 31 or int(ticketDate[4:6]) in monthsB and int(ticketDate[6:]) > 30 or int(ticketDate[4:6]) == 2 and int(ticketDate[:4])%4 != 0 and int(ticketDate[6:]) > 28 or int(ticketDate[4:6]) == 2 and int(ticketDate[:4])%4 == 0 and int(ticketDate[6:]) > 29:
                    print("Ticket date is invalid")
                    landing()
                    return
        else:
            print("Ticket date is invalid")
            landing()
            return
        
        global runningTransactions
        global userInfo
        # append a sell transaction to running total
        runningTransactions += "sell,%s,%s,%.2f,%d\n" % (userInfo["username"], ticketName, ticketPrice, ticketQuantity)
    else:
        print("Command invalid")
    landing()

# method lets user buy tickets from ticket list file
def buy():
    if loggedIn:
        clear()
        print("---BUY---")
        availableQuantity = -1
        ticketPrice = -1
        ticketName = input("Enter the ticket name: ")
        # validate name format
        validTicket = False
        if (ticketName[0] != " " and not ticketName.endswith(" ") and len(ticketName) <= 60):
            if not ticketName.isalnum():
                tempTicket = ""
                for c in ticketName:
                    if c != ' ':
                        tempTicket += c
            if ticketName.isalnum() or tempTicket.isalnum():
                # match name to ticket in file
                tickets = open(ticketsPath, "r")
                for line in tickets:
                    values = line.split(',')
                    if values[0] == ticketName:
                        # get ticket values
                        validTicket = True
                        ticketPrice = float(values[1])
                        availableQuantity = int(values[2])
                        break
            else:
                print("Ticket name is invalid")
                landing()
                return
            tickets.close()
        if not validTicket:
            print("Ticket name is invalid")
            landing()
            return

        global userInfo
        ticketQuantity = int(input("Enter the ticket quantity: "))
        # buy quantity can't be greater than what's available and user needs to be able to afford it
        if (ticketQuantity < 0 or ticketQuantity > availableQuantity):
            print("Ticket quantity is invalid")
        elif (ticketPrice * ticketQuantity * 1.40 >= userInfo["balance"]):
            print("Balance is too low")
        else:
            # update user balance
            userInfo["balance"] -= ticketPrice * ticketQuantity * 1.40
            newfile = ""
            email = userInfo["email"]
            # update user balance in the file
            accounts = open(accountsPath, "r")
            for line in accounts:
                values = line[:-1].split(',')
                if values[0] == email:
                    newfile += "%s,%s,%s,%.2f\n" % (email, values[1], values[2], userInfo["balance"])
                else:
                    newfile += line
            accounts = open(accountsPath, "w")
            accounts.write(newfile)
            accounts.close()

            # update ticket quantity in the file
            newfile = ""
            tickets = open(ticketsPath, "r")
            for line in tickets:
                values = line[:-1].split(',')
                if values[0] == ticketName:
                    newfile += "%s,%.2f,%d,%s\n" % (ticketName, ticketPrice, availableQuantity - ticketQuantity, values[3])
                else:
                    newfile += line
            tickets = open(ticketsPath, "w")
            tickets.write(newfile)
            tickets.close()
            
            # append a buy transaction
            global runningTransactions
            runningTransactions += "buy,%s,%s,%.2f,%d\n" % (userInfo["username"], ticketName, ticketPrice, ticketQuantity)
    else:
        print("Command invalid")
    landing()

# method lets user update ticket info in the file
def update():
    if loggedIn:
        clear()
        print("---UPDATE---")
        ticketName = input("Enter the ticket name: ")

        # check if name matches a ticket in file
        tickets = open(ticketsPath, "r")
        validName = False
        if ticketName[0] != ' ' and not ticketName.endswith(' ') and not len(ticketName) > 60:
            tempTicket = ""
            if not ticketName.isalnum():
                for c in ticketName:
                    if c != ' ':
                        tempTicket += c
            if ticketName.isalnum() or tempTicket.isalnum():
                tickets = open(ticketsPath, "r")
                for line in tickets:
                    values = line.split(',')
                    if values[0] == ticketName:
                        validName = True
                        break
        if not validName:
            print("Name is invalid")
            landing()
            return
        
        # new price must be in range [10:100]
        ticketPrice = float(input("Enter the ticket price: "))
        if ticketPrice < 10 or ticketPrice > 100:
            print("Price is invalid")
            landing()
            return
        # new quantity must be in range [0:100]
        ticketQuantity = int(input("Enter the ticket quantity: "))
        if ticketQuantity < 0 or ticketQuantity > 100:
            print("Quantity is invalid")
            landing()
            return
        # date must be in format YYYYMMDD
        ticketDate = input("Enter the ticket date: ")
        monthsA = [1, 3, 5, 7, 8, 10, 12]
        monthsB = [4, 6, 9, 11]
        if ticketDate.isnumeric():
            if len(ticketDate) != 8 or int(ticketDate[:4]) > 2020 or int(ticketDate[4:6]) > 12 or int(ticketDate[4:6]) < 0:
                    print("Date is invalid")
                    landing()
                    return
            else:
                if  int(ticketDate[4:6]) in monthsA and int(ticketDate[6:]) > 31 or int(ticketDate[4:6]) in monthsB and int(ticketDate[6:]) > 30 or int(ticketDate[4:6]) == 2 and int(ticketDate[:4])%4 != 0 and int(ticketDate[6:]) > 28 or int(ticketDate[4:6]) == 2 and int(ticketDate[:4])%4 == 0 and int(ticketDate[6:]) > 29:
                    print("Date is invalid")
                    landing()
                    return
        else:
            print("Date is invalid")
            landing()
            return
        
        # change ticket info in file
        newfile = ""
        tickets = open(ticketsPath, "r")
        for line in tickets:
            values = line[:-1].split(',')
            if values[0] == ticketName:
                newfile += "%s,%.2f,%d,%s\n" % (ticketName, ticketPrice, ticketQuantity, values[3])
            else:
                newfile += line
        tickets = open(ticketsPath, "w")
        tickets.write(newfile)
        tickets.close()

        # append an update transaction
        global runningTransactions
        runningTransactions += "update,%s,%s,%.2f,%d\n" % (userInfo["username"], ticketName, ticketPrice, ticketQuantity)
    else:
        print("Command invalid")
    landing()

# method logs user out and resets user variables
def logout():
    # must be logged in
    global loggedIn
    if loggedIn:
        clear()
        # signal that user logged out
        global userInfo
        loggedIn = False
        # reset user variables
        userInfo["username"] = ""
        userInfo["balance"] = -1
        userInfo["email"] = ""
        print("Logout successful")
    else:
        print("Command invalid")
    landing()

# method ends the program and adds all transactions to file
def exit():
    if not loggedIn:
        clear()
        # append all performed transactions to office location's file
        global runningTransactions
        transactions = open(location + "_transactions.csv", "a")
        transactions.write(runningTransactions)
        transactions.close()
        print("Exiting program")
        #sleep(1.5)
        clear()
    else:
        print("Command invalid")
        landing()


##### call main method #####
if __name__ == "__main__":
    main()