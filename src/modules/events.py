from sys import exit
from modules.utils import ask, AskException, generate_unique_id, get_month


def create_new_event(con, invoker):
    new_instance = True
    try:
        while True:
            print(
                """
 -*-*- Create a new event -*-*-
 *-*-* Type ".stop" or ".s" to stop *-*-*"""
            )
            if not new_instance:
                inp = input("\n Do you want to continue? (y/n): ").lower().strip()
                if inp in ("yes", "y"):
                    pass
                else:
                    break
            data = {}
            ask("\n Enter a name for the event: ", invoker, data, "name")
            ask("\n Enter a description for the event: ", invoker, data, "description")
            ask("\n Enter the name of event manager: ", invoker, data, "event_manager")
            ask(
                "\n Enter the date of commencement (yyyy-mm-dd): ",
                invoker,
                data,
                "start_date",
            )
            ask(
                "\n Enter the date of termination (yyyy-mm-dd): ",
                invoker,
                data,
                "end_date",
            )
            ask("\n Enter budget (in Rs): ", invoker, data, "budget")
            ask("\n Enter the location of event: ", invoker, data, "location")
            cursor = con.cursor()
            cursor.execute(
                "INSERT INTO events (id, name, description, event_manager, start_date, end_date, budget, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                (
                    generate_unique_id(),
                    data["name"],
                    data["description"],
                    data["event_manager"],
                    data["start_date"],
                    data["end_date"],
                    data["budget"],
                    data["location"],
                ),
            )
            con.commit()
            print(f'\n [+] New event "{data["name"]}" has been added to the database')
            if new_instance:
                new_instance = False
    except AskException:
        return


def list_events(con, inline=False):
    if not inline:
        print(
            """
 -*-*- Registered events -*-*-
 *-*-* Choose [4 or d or D] to edit events *-*-*
 """
        )
    cursor = con.cursor()
    cursor.execute(
        "SELECT name, event_manager, start_date, end_date, id FROM events ORDER BY start_date;"
    )
    records = cursor.fetchall()
    if len(records) == 0:
        print(" No events to show")
        return []
    for i, record in enumerate(records):
        [yyyy, mm, dd] = str(record[2]).split("-")
        [yyyy2, mm2, dd2] = str(record[3]).split("-")
        print(
            f" {i + 1}. {record[0]}\n Event Manager: {record[1]}\n Commencement: {get_month(mm)} {int(dd)}, {yyyy}\n Termination: {get_month(mm2)} {int(dd2)}, {yyyy2}\n"
        )
    return records


def view_event_contents(con, invoker):
    print(
        """
 -*-*- View event contents -*-*-
 *-*-* Type ".stop" or ".s" to exit
 """
    )
    records = list_events(con, True)
    if len(records) == 0:
        return
    while True:
        inp = input("\n Enter the serial number of the event: ").lower().strip()
        if inp == "":
            continue
        elif inp[0] == ".":
            if inp[1:] in ("stop", "s"):
                break
            else:
                invoker(inp[1:])
        else:
            inp = int(inp)
            if inp < 1:
                print("\n [!] ChoiceError: Serial number can't be smaller than 1")
                return
            elif inp > len(records):
                print(
                    f'\n [!] ChoiceError: Entered serial number "{inp}" is larger than the number of events registered'
                )
                return
            cursor = con.cursor()
            cursor.execute(
                "SELECT * FROM events WHERE id = %s;", (records[inp - 1][4],)
            )
            [records2] = cursor.fetchall()
            print(
                f"""\n Name of the event: {records2[1]}
 Description of the event: {records2[2]}
 Name of the event manager: {records2[3]}
 Date of commencement: {records2[4]}
 Date of termination: {records2[5]}
 Budget for the event: {records2[6]}
 Location for the event: {records2[7]}"""
            )


def edit_events(con, invoker):
    print(
        """
 -*-*- Edit events -*-*-
 -*-*- Type ".stop" or ".s" to exit
 """
    )
    new_instance = True
    records = list_events(con, True)
    if len(records) == 0:
        return
    while True:
        inp = input("\n Enter the serial number of the event: ").lower().strip()
        if inp == "":
            continue
        if inp[0] == ".":
            if inp[1:] in ("stop", "s"):
                break
            else:
                invoker(inp[1:])
        else:
            try:
                if not new_instance:
                    inp2 = input("\n Do you want to continue? (y/n): ").lower().strip()
                    if inp2 in ("yes", "y"):
                        pass
                    else:
                        break
                data = {}
                ask("\n Enter a name for the event: ", invoker, data, "name")
                ask(
                    "\n Enter a description for the event: ",
                    invoker,
                    data,
                    "description",
                )
                ask(
                    "\n Enter the name of event manager: ",
                    invoker,
                    data,
                    "event_manager",
                )
                ask(
                    "\n Enter the date of commencement (yyyy-mm-dd): ",
                    invoker,
                    data,
                    "start_date",
                )
                ask(
                    "\n Enter the date of termination (yyyy-mm-dd): ",
                    invoker,
                    data,
                    "end_date",
                )
                ask("\n Enter budget (in Rs): ", invoker, data, "budget")
                ask("\n Enter the location of event: ", invoker, data, "location")
                cursor = con.cursor()
                for item in data.keys():
                    cursor.execute(
                        "UPDATE events SET " + item + " = %s WHERE id = %s;",
                        (data[item], records[int(inp) - 1][4]),
                    )
                con.commit()
                print(f'\n [+] Event "{data["name"]}" has been updated')
                if new_instance:
                    new_instance = False
            except AskException:
                break


def delete_events(con, invoker):
    print(
        """
 -*-*- Delete events -*-*-
 """
    )
    records = list_events(con, True)
    if len(records) == 0:
        return
    while True:
        inp = input(
            "\n Enter serial numbers of events to delete (seperated by comma): "
        ).strip()
        if inp == "":
            continue
        elif inp[0] == ".":
            invoker(inp[1:])
        else:
            event_names = []
            event_ids = []
            for serial_number in inp.split(","):
                temp = int(serial_number)
                if temp < 1:
                    print("\n [!] ChoiceError: Serial number can't be smaller than 1")
                    return
                elif temp > len(records):
                    print(
                        f'\n [!] ChoiceError: Entered serial number "{temp}" is larger than the number of events registered'
                    )
                    return
                event_names.append(records[temp - 1][0])
                event_ids.append(records[temp - 1][4])
            cursor = con.cursor()
            for id in event_ids:
                cursor.execute("DELETE FROM events WHERE id = %s;", (id,))
            con.commit()
            print(
                f'\n [-] Event(s) "{", ".join(event_names)}" were deleted from the database'
            )
            break
