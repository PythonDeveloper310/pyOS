def listfile():
    import os
    from System.variables import sys_homedir

    try:
        files = os.listdir(sys_homedir)
        if not files:
            print("No files found.")
        else:
            print("Files:")
            for file in files:
                print(file)
    except Exception as e:
        print(f"An error occurred while listing files: {e}")