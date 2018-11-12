from random import*
from os import*
from time import*
def terminal():
    command=input("[terminal] $ ")
    if command== ("terminal help"):
        helpmod()
    elif command== ("terminal help.commands"):
        commandhelp()
    elif command== ("terminal apps"):
        terminalapps()
    elif command==("dev"):
        devinterpreter()
    elif command==("net"):
        netinterpreter()
    elif command==("cmd"):
        cmdinterpreter()
    else:
        print()
        print("This is not a valid command.")
        terminal()
def terminalapps():
    print()
    print("---Terminal Apps------------------------------------------------")
    print()
    print("terminal enable 'net'        -Enables the NET commands")
    print("terminal switch 'net'        -Switches to the NET interpreter")
    print("terminal enable 'cmd'        -Enables the CMD commands")
    print("terminal switch 'cmd'        -Switches to the CMD interpreter")
    print("terminal enable 'dev'        -Enables the DEV commands")
    print("terminal switch 'dev'        -Switches to the DEV interpreter")
    print()
    print()
    print("---net Apps----------------------------------------------------")
    print()
    print("net processes            -Displays the NET processes active")
    print("net leave                -Returns to the 'terminal' interpreter")
    print("net join                 -Joins a 'net' connection")
    print()
    terminal()
def helpmod():
    print(" _  _ ___ _    ___   ___")
    print("| || | __| |  | _ \ |__ \ ")
    print("| __ | _|| |__|  _/   /_/")
    print("|_||_|___|____|_|    (_)")
    print()
    print("---terminal Commands---------------------------------------------")
    print("terminal random      -Dispalys a random  number")
    print("terminal exit        -Exits the terminal")
    print("terminal help        -Displays the Help Section")
    print("terminal help pro    -Displays a full list of commands")
    print("terminal apps        -Displays a list of apps")
    print("terminal random      -Displays a random number")
    print()
    print()
    print("---cmd Commands--------------------------------------------------")
    print("cmd help            -Displays the Help Section")
    print("cmd leave           -Quits the CMD app")
    print("cmd quit            -Quits the Emulator")
    print("cmd help pro        -Dispalys a full list of commands")
    print("cmd apps            -Displays a list of apps")
    print("cmd create          -Creates a file containing a random number")
    print("cmd random          -Displays a random number")
    print()
    print()
    print("---net Commands--------------------------------------------------")
    print("net info            -Displays the current session info")
    print("net help            -Displays a list of 'net' commands")
    print("net leave           -Returns to the 'terminal' interpreter")
    print("net quit            -Quits the terminal")
    print()
    print()
    print("--dev Commands--------------------------------------------------")
    print("dev help            -Displays a list of Developer Commands")
    print("dev leave           -Returns to the 'terminal' interpreter")
    print("dev debug           -Starts the Debugger")
    print("dev quit            -Quits the Emulator")
    print("dev errors          -Displays a list of error codes")
    print("dev lock            -Locks the 'dev' interpreter")
    print()
    print()
    terminal()
def devinterpreter():
    devcommand=input("[Developer] $ ")
    if devcommand==("dev help"):
        devhelp()
    elif devcommand==("dev leave"):
        print("Leaving the 'dev' interpreter...")
        sleep(5)
        terminal()
    elif devcommand==("dev debug"):
        devdebug()
    elif devcommand==("dev quit"):
        print("Leaving the 'dev' interpreter...")
        sleep(5)
        print("Leaving the Emulator...")
        sleep(5)
        exit()
    elif devcommand==("dev errors"):
        deverrors()
    elif devcommand==("dev lock"):
        lock()
    else:
        print("ERROR CODE: 000x02")
        devinterpreter()
def devhelp():
    print("See DEVREADME.md")
    devinterpreter()
terminal()
