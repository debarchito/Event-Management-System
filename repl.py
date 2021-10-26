from os import system, name
from json import load
from mysql.connector import connect, Error, errorcode
from sys import exit
from events import create_new_event, list_events

options = '''
 Select your option (a-g, A-G, 1-7):

    (a) Create a new event
    (b) List event(s)
    (c) View event contents
    (d) Edit event(s)
    (e) Remove event(s) [temporary; stays in recycle bin]
    (f) Restore event(s)
    (g) Delete event(s) [permanent]'''

help_ = '''
 Type ".options" or ".o" to view the options again
 Type ".exit" or ".e" to exit the app
 Type ".help" or ".h" to print this help message again'''

def initials():
    system('cls' if name == 'nt' else 'clear')
    print(f'''
 --- Event Management System ---
 *** by Debarchito, Surachandra, Ruhit, and Saurav ***
{options}
{help_}''')

def init():
    try:
        with open('database/config.json', 'r') as config_file:
            config = load(config_file)
            config_file.close()
            try:
                con = connect(
                    host = config['host'],
                    user = config['user'],
                    password = config['password'],
                    database = config['database']
                )
                initials()
                while True:
                    inp = input('\n Enter your choice: ').lower().strip()
                    if inp != '':
                        if inp[0] == '.':
                            invoker(inp[1:])
                        else:
                            if inp in ('a', '1'):
                                create_new_event(con = con, invoker = invoker)
                            elif inp in ('b', '2'):
                               list_events(con = con)
                            elif inp in ('c', '3'):
                                pass
                            elif inp in ('d', '4'):
                                pass
                            elif inp in ('e', '5'):
                                pass
                            elif inp in ('f', '6'):
                                pass
                            elif inp in ('g', '7'):
                                pass
                            else:
                                print(f'\n [!] ChoiceError: "{inp}" is an invalid choice. Choose from: a-f, A-F, 1-6')
                    else:
                        pass
            except Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print('\n [!] AccessDenied: The username or password passed is probably wrong')
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print('\n [!] BadDatabaseError: The database passed does not exist')
                else:
                    print(err)
    except KeyboardInterrupt:
        print('\n [!] KeyboardInterrupt')

def invoker(inp):
    if inp in ('exit', 'e'):
        exit()
    elif inp in ('options', 'o'):
        print(options)
    elif inp in ('help', 'h'):
        print(help_)
    else:
        print(f'\n [!] InvokerError: ".{inp}" is an invalid invoker')
