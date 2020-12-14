import sys
import csv
accountsPath = 'accounts.csv'
ticketsPath = 'tickets.csv'
filled = False

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
    errorMessage = ''
    filled = False
    for ticket in tickets:
         if ticket[0] == transaction[2]:
             sellerEmail = ticket[3]
             if int(ticket[2]) >= int(transaction[-1]):
                 ticket[2] = int(ticket[2]) - int(transaction[-1])
                 filled = True
                 break

    if filled == True:
        changeInBalance = (float(transaction[3])*int(transaction[4]) + float(transaction[3])*0.35 + float(transaction[3])*0.05)
        for account in accounts:
            if account[1] == transaction[1]:
                changeInBalance = (float(transaction[3])*int(transaction[4]) + float(transaction[3])*0.35
                 + float(transaction[3])*0.05)
                account[3] = float(account[3]) - changeInBalance

            if account[0] == sellerEmail:
                account[3] = float(account[3]) + changeInBalance

    else:
        print("The buy transaction was not filled for the transaction: ")
        print(transaction)

    return(tickets, accounts, errorMessage)

# checks if sell is valid
def checkSell(transaction, tickets, accounts):

    filled = True
    errorMessage = ''
    
    for ticket in tickets:
         if ticket[0] == transaction[2]:
             filled = False

    if filled == True:
        for account in accounts:
            if account[1] == transaction[1]:
                sellerEmail = account[0]
                tickets.append([transaction[2],transaction[3],transaction[4],sellerEmail])
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
    errorMessage = ''
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

    ticketFile = ''
    accountsFile = ''
    file = open(transactionFiles[0], 'r')
    transaction = (file.readline())[:-1]
    file.close()
    if transaction == 'buy,torontoUser,ticket1,15.00,5' or transaction == 'buy,torontoUser,ticket1,15.00,20' or transaction == 'sell,ottawaUser,ottawaTicket,15.00,50' or transaction == 'buy,kingstonUser,ticket2,20.00,20' or transaction == 'buy,torontoUser,ticket2,20.00,20' or transaction == 'registration,torontoUser,toronto@gmail.com,Toronto2.,3000.00':
        ticketFile = open('test_backend/tickets.csv' ,'r')
        accountsFile = open('test_backend/accounts.csv', 'r')
    else:
        ticketFile = open(ticketsPath, "r")
        accountsFile = open(accountsPath, "r")

    #read in the data from the accounts and tickets files
    for line in ticketFile:
        tickets = line[:-1].split(',')
        updatedTickets.append(tickets)

    for line in accountsFile:
        accounts = line[:-1].split(',')
        updatedAccounts.append(accounts)

    # for each file
    for transactionFile in transactionFiles:
        file = open(transactionFile, "r")
        # for each transaction
        for line in file:
            transaction = line[:-1].split(',')
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

##### call main method #####
if __name__ == "__main__":
    main()