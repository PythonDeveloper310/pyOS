from System.Commands.clear import clear

def shutdown():
    import sys
    
    print("Shutting down the system...")
    global sys_homedir
    sys_homedir = ''
    clear(1.5)
    sys.exit(0)