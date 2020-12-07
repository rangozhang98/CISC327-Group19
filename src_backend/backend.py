import sys
import csv
accountsPath = 'accounts.csv'
ticketsPath = 'tickets.csv'
filled = False

# ---- will not work with nonexistent file names as arguments because process() tries to open them -----------
def main():
    try:
        transactionFiles = []
        for i in range(1, len(sys.argv)):
            transactionFiles.append(sys.argv[i])
        transactionFiles.sort()
        # array ready to process
        process(transactionFiles)
    except:
        # instruct user how to run the program if arguments are wrong
        print("Program needs arguments: {transaction_file_1.csv}, {transaction_file_2.csv}, etc...")

#checks if buy is valid and changes ticket amount and buyer balance
def checkBuy(transaction, tickets, accounts):
    for ticket in tickets:
         if ticket[0] == transaction[1]:
             if int(ticket[2]) >= int(transaction[-1]):
                 ticket[2] = int(ticket[2]) - int(transaction[-1])
                 global filled
                 filled = True
                 break

    if filled == True:
        for account in accounts:
            if account[1] == transaction[1]:
                account[3] = int(account[3]) - (int(transaction[3])*int(transaction[4]) + int(transaction[3])*0.35 + int(transaction[3])*0.05)
                break
    else:
        errorMessage = "The buy transaction was not filled"

    return(tickets, accounts, errorMessage)

# checks if sell is valid
def checkSell(transaction, tickets, accounts):
     
    for ticket in tickets:
         if ticket[0] == transaction[1]:
             if int(ticket[2]) >= int(transaction[-1]):
                 ticket[2] = int(ticket[2]) - int(transaction[-1])
                 global filled
                 filled = True
                 break

    if filled == True:
        for account in accounts:
            if account[1] == transaction[1]:
                account[3] = int(account[3]) + (int(transaction[3])*int(transaction[4]) + int(transaction[3])*0.35 + int(transaction[3])*0.05)
                break
    else:
        errorMessage = "The sell transaction was not filled"


    return(tickets, accounts, errorMessage)

#updates stuff if its the correct person trying to update the ticket        
def checkUpdate(transaction, tickets, accounts):
     
    for ticket in tickets:
         if ticket[0] == transaction[1]:
             for account in accounts:
                if transaction[1] == account[1] and ticket[3] == account[0]:
                    ticket[1] = transaction[3]
                    ticket[2] = transaction[4]
                    break
    
    return(tickets, accounts)

#updates accounts file to include newly registered accounts
def checkRegistration(transaction, accounts):
    newEmail = True
    for account in accounts:
        if transaction[2] == account[0]:
            newEmail = False
            errorMessage = "This email already exists"
    
    if newEmail == True:
        accounts.append([transaction[2], transaction[1], transaction[3], transaction[4]])
    
    return(accounts, errorMessage)


# Each transaction has to satisfy the constraints specificed in the frontend requirement. 
# For example, a ticket purchase transaction has to make sure that there are enough tickets in order to proceeed.
def process(transactionFiles):

    updatedTickets = []
    updatedAccounts = []
    errorMessage = ""

    #read in the data from the accounts and tickets files
    ticketFile = open(ticketsPath, "r")
    for line in ticketFile:
        tickets = line.split(',')
        updatedTickets.append(tickets)

    accountsFile = open(accountsPath, "r")
    for line in accountsFile:
        accounts = line.split(',')
        updatedAccounts.append(accounts)

    # for each file
    for transactionFile in transactionFiles:
        file = open(transactionFile, "r")
        # for each transaction
        for line in file:
            transaction = line.split(',')
            # if somehow invalid then log error in console

            if transaction[0].lower() == "buy":
                updatedTickets, updatedAccounts, errorMessage = checkBuy(transaction, updatedTickets, updatedAccounts)
            elif transaction[0].lower() == "sell":
                updatedTickets, updatedAccounts, errorMessage = checkSell(transaction, updatedTickets, updatedAccounts)
            elif transaction[0].lower() == "update":
                updatedTickets, updatedAccounts = checkUpdate(transaction, updatedTickets, updatedAccounts)
            elif transaction[0].lower() == "registration":
                updatedAccounts, errorMessage = checkRegistration(transaction, updatedAccounts)


        file.close()
    update(updatedAccounts, updatedTickets)


# create updated_accounts and updated_tickets csvs with processed info
def update(accounts, tickets):

    with open('updated_accounts.csv', 'w', newline='') as file:
        accountsWriter = csv.writer(file)
        for account in accounts:
            accountsWriter.writerow(account)

    with open('updated_tickets.csv', 'w', newline='') as file2:
        ticketsWriter = csv.writer(file2)
        for ticket in tickets:
            ticketsWriter.writerow(ticket)

    return

main()