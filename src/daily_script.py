import random
from importlib import reload
import os
import io
import sys
import frontend
import backend
from time import sleep
from os import system
from os import name
clear = lambda: system('cls' if name=='nt' else 'clear')

accountsPath = 'accounts.csv'
ticketsPath = 'tickets.csv'
login_inputs = [['login','aaa@gmail.com','Aa.45'],
            ['login','www@gmail.com','Ww.45'],
            ['login','zzz@gmail.com','Zz.45'],
            ['login','ddd@gmail.com','Dd.45'],
            ['register','bbb@gmail.com','bbb', 'Bb.45', 'Bb.45'],
            ['register','ccc@gmail.com','ccc', 'Cc.45', 'Cc.45'],
            ['login','bbb@gmail.com','Bb.45'],
            ['login','ccc@gmail.com','Cc.45']]
                
action_inputs = [['buy','ticket1','5','15.00','20200202'],
                ['buy','ticket1','7','15.00','20200202'],
                ['buy','ticket2','3','20.00','20200202'],
                ['buy','ticket2','8','20.00','20200202'],
                ['sell','ticket3','25.00','100','20200202'],
                ['sell','ticket4','30.00','100','20200202'],
                ['buy','ticket3','2','25.00','20200202'],
                ['buy','ticket3','10','25.00','20200202'],
                ['buy','ticket4','4','30.00','20200202'],
                ['buy','ticket4','10','30.00','20200202'],
                ['update','ticket1','10.00','100','20200202'],
                ['update','ticket2','15.00','70','20200202']]

def main():
    input_cities, terminal_input = define_input()
    run_frontend(input_cities, terminal_input)
    run_backend(input_cities)

def run_backend(input_cities):
    # cleanup package
    reload(backend) 
    # prepare program parameters
    sys.argv = ['backend.py']
    for city in input_cities:
        sys.argv.append(city + "_transactions.csv")

    # run the program
    backend.main()

def run_frontend(input_cities, terminal_input):
    # run frontend for multiple cities for the day
    for i in range(len(terminal_input)): 
        # cleanup package
        reload(frontend) 
        # prepare program parameters
        sys.argv = [
            'frontend.py',
            input_cities[i],
            accountsPath,
            ticketsPath
        ]
                
        # set terminal input
        sys.stdin = io.StringIO(
            '\n'.join(terminal_input[i]))

        # run the program
        frontend.main()

def define_input():
    input_cities = []
    terminal_input = []
    # if accounts file empty (monday)
    if os.stat(accountsPath).st_size == 0:
        input_cities = ['a', 'b']
        terminal_input = [['register',
                        'aaa@gmail.com',
                        'aaa',
                        'Aa.45',
                        'Aa.45',
                        'register',
                        'www@gmail.com',
                        'www',
                        'Ww.45',
                        'Ww.45',
                        'exit'],
                        ['register',
                        'zzz@gmail.com',
                        'zzz',
                        'Zz.45',
                        'Zz.45',
                        'register',
                        'ddd@gmail.com',
                        'ddd',
                        'Dd.45',
                        'Dd.45',
                        'exit']]
    # if tickets file empty (tuesday)
    elif os.stat(ticketsPath).st_size == 0:
        input_cities = ['a', 'b']
        terminal_input = [['login',
                        'aaa@gmail.com',
                        'Aa.45',
                        'sell',
                        'ticket1',
                        '15.00',
                        '30',
                        '20200202',
                        'logout',
                        'exit'],
                        ['login',
                        'ddd@gmail.com',
                        'Dd.45',
                        'sell',
                        'ticket2',
                        '20.00',
                        '50',
                        '20200202',
                        'logout',
                        'exit']]
    # if both files are populated (wednesday-friday)
    else:
        input_cities = ['a', 'b', 'c']
        for i in range(0,3):
            temp = []
            for j in range(0,3):
                rand = random.randint(0,len(login_inputs)-1)
                temp += login_inputs[rand]        
                rand = random.randint(0,len(action_inputs)-1)
                temp += action_inputs[rand]
                temp.append('logout')
            temp.append('exit')
            terminal_input.append(temp)  
    return(input_cities, terminal_input)

##### call main method #####
if __name__ == "__main__":
    main()