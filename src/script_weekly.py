import script_daily as daily

def main():
    for i in range(5):
        daily.main()

        accounts = open("accounts.csv", 'r')
        oldAccounts = open("account_updates/accounts_day_" + str(i+1) + ".csv", 'a')
        
        for line in accounts:
            oldAccounts.write(line)

        accounts.close()
        oldAccounts.close()

        tickets = open("tickets.csv", 'r')
        oldTickets = open("ticket_updates/tickets_day_" + str(i+1) + ".csv", 'a')
        
        for line in tickets:
            oldTickets.write(line)

        tickets.close()
        oldTickets.close()

        newAccounts = open("updated_accounts.csv", 'r')
        accounts = open("accounts.csv", 'w')
        
        for line in newAccounts:
            accounts.write(line)

        accounts.close()
        newAccounts.close()

        newTickets = open("updated_tickets.csv", 'r')
        tickets = open("tickets.csv", 'w')
        
        for line in newTickets:
            tickets.write(line)

        tickets.close()
        newTickets.close()

##### call main method #####
if __name__ == "__main__":
    main()