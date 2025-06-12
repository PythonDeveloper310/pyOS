def make_dir(dir_name):
    import os

    try:
        os.makedirs(dir_name, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating directory '{dir_name}': {e}")
        return False