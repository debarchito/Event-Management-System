from os import system, name
from json import load
from mysql.connector import connect, Error, errorcode
from sys import exit
from modules.events import *
from modules.highlight import highlight_mode_init


options = """
 Select your option (a-e, A-E, 1-5):

    (a) Create a new event
    (b) List event(s)
    (c) View event contents
    (d) Edit event(s)
    (e) Delete event(s)"""

help_message = """
 Type "!" to enter highlight mode

 Type ".options" or ".o" to view the options again
 Type ".exit" or ".e" to exit the app
 Type ".help" or ".h" to print this help message again"""


def initials():
    system("cls" if name == "nt" else "clear")
    print(
        f"""
 --- Event Management System ---
 *** by Debarchito, Surachandra, Ruhit, and Saurav ***
{options}
{help_message}"""
    )


def init():
    try:
        with open("database/config.json", "r") as config_file:
            config = load(config_file)
            try:
                con = connect(
                    host=config["host"],
                    user=config["user"],
                    password=config["password"],
                    database=config["database"],
                )
                initials()
                while True:
                    inp = input("\n Enter your choice: ").lower().strip()
                    if inp != "":
                        if inp[0] == ".":
                            invoker(inp[1:])
                        else:
                            if inp == "!":
                                highlight_mode_init(con, invoker)
                            elif inp in ("a", "1"):
                                create_new_event(con, invoker)
                            elif inp in ("b", "2"):
                                list_events(con)
                            elif inp in ("c", "3"):
                                view_event_contents(con, invoker)
                            elif inp in ("d", "4"):
                                edit_events(con, invoker)
                            elif inp in ("e", "5"):
                                delete_events(con, invoker)
                            else:
                                print(
                                    f'\n [!] ChoiceError: "{inp}" is an invalid choice. Choose from: a-e, A-E, 1-5 or >'
                                )
                    else:
                        pass
            except Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print(
                        "\n [!] AccessDenied: The username or password passed is probably wrong"
                    )
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("\n [!] BadDatabaseError: The database passed does not exist")
                else:
                    print(err)
    except KeyboardInterrupt:
        print("\n [!] KeyboardInterrupt")


def invoker(inp):
    if inp in ("exit", "e"):
        exit()
    elif inp in ("options", "o"):
        print(options)
    elif inp in ("help", "h"):
        print(help_message)
    else:
        print(f'\n [!] InvokerError: ".{inp}" is an invalid invoker')
