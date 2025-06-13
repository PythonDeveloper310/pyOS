import System.Filesystem.filesystem as fs
from System.variables import *
from System.constants import *
from System.Commands import *

def init():
    global sys_homedir
    fs.create_filesystem()
    sys_homedir = FS_PATH + 'home'

def system():
    clear(0)
    print("\nInitializing pyOS...")
    init()
    print("\npyOS initialized.")
    clear(1.5)

    print("Welcome to pyOS!")
    print("Logged in as: root")
    clear(2)
    print("Welcome to pyOS!")
    print("Type 'help' for a list of available commands.\n")

    while True:
        shell_input = input("$ ").strip().lower()

        if shell_input == 'help':
            help()
        elif shell_input == 'clear':
            clear(0)
        elif shell_input == 'ls':
            ls()
        elif shell_input.startswith('mkdir '):
            dir_name = shell_input.split(' ', 1)[1] if ' ' in shell_input else ''
            if dir_name:
                mkdir(dir_name)
            else:
                print("Usage: mkdir <directory_name>")
        elif shell_input == 'shutdown':
            shutdown()
        else:
            print(f"Unknown command: {shell_input}\nType 'help' for a list of available commands.")

def run():
    try:
        system()
    except KeyboardInterrupt:
        shutdown()
    except Exception as e:
        print(f"An error occurred: {e}")
        shutdown()