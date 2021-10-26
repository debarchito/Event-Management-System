from utils import generate_unique_id

def create_new_event(*, con, invoker):
    i = 1
    while True:
        print('''
 -*-*- Create a new event -*-*-
 *-*-* Type ".stop" or ".s" to stop *-*-*''')
        if i == 0:
            ask = input('\n Do you want to continue? (y/n): ').lower().strip()
            if ask in ('yes', 'y'):
                pass
            else:
                break
        name = input('\n Enter a name for the event: ').strip()
        if name[0] == '.':
            if name[1:].lower() in ('stop', 's'):
                break
            else:
                invoker(name)
        desp = input('\n Enter a description for the event: ').strip()
        if desp[0] == '.':
            if desp[1:].lower() in ('stop', 's'):
                break
            else:
                invoker(desp)
        date = input('\n Enter the date of commencement (yyyy-mm-dd): ').strip()
        if date[0] == '.':
            if date[1:].lower() in ('stop', 's'):
                break
            else:
                invoker(date)
        cursor = con.cursor()
        cursor.execute(
            'INSERT INTO events (id, name, description, `date`) VALUES (%s, %s, %s, %s);',
            (generate_unique_id(), name, desp, date)
        )
        con.commit()
        print(f'\n [+] New event "{name}" has been added to the database')
        if i == 1:
            i = 0

def list_events(*, con):
    print('''
 -*-*- Registered events -*-*-
 *-*-* Choose [2 or b or B] to edit events *-*-*
 ''')
    cursor = con.cursor()
    cursor.execute('SELECT name FROM events;')
    records = cursor.fetchall()
    for i, record in enumerate(records):
        print(f' {i + 1}. {record[0]}')
