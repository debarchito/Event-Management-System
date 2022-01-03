from string import ascii_uppercase, ascii_lowercase, digits
from random import choice


class AskException(Exception):
    pass


def generate_unique_id():
    chars = ascii_uppercase + ascii_lowercase + digits
    return "".join(choice(chars) for _ in range(10))


def get_month(i):
    return [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Nov",
        "Dec",
    ][int(i) - 1]


def ask(context, invoker, store, entity):
    while True:
        inp = input(context).strip()
        if inp == "":
            continue
        elif inp[0] == ".":
            if inp[1:].lower() in ("s", "stop"):
                raise AskException
            else:
                invoker(inp)
        else:
            store[entity] = inp
            break
