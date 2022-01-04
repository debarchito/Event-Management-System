from modules.submodules.dataframe import init as dataframe_init
from modules.submodules.visualisation import init as visualisation_init


def highlight_mode_init(con, invoker):
    options = """
 Select your option (a-b, A-B, 1-2):

    (a) DataFrame representation of highlights
    (b) Visual representation of highlights
    
 Type "?" to exit highlight mode
 Type ".!" to view the highlight options list"""

    print(
        f"""
 -*-*- Welcome to highlight mode -*-*-
 {options}"""
    )

    while True:
        inp = input("\n (hightlight mode) Enter your choice: ").lower().strip()
        if inp == "":
            pass
        elif inp[0] == "?":
            break
        elif inp[0] == ".":
            inp = inp[1:]
            if inp == "!":
                print(options)
            else:
                invoker(inp)
        else:
            if inp in ("a", "1"):
                dataframe_init(con, False)
            if inp in ("b", "2"):
                visualisation_init(con)
