def clear(sleep_time):
    import os
    import time

    time.sleep(sleep_time)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')