# This file will create the filesystem for the OS.
import os
from System.constants import FS_PATH

def create_filesystem():
    os.makedirs(FS_PATH, exist_ok=True)

    subdirs = ['home', 'etc', 'var']

    for subdir in subdirs:
        os.makedirs(os.path.join(FS_PATH, subdir), exist_ok=True)

    return

def delete_filesystem(FS_PATH):
    if os.path.exists(FS_PATH):
        for root, dirs, files in os.walk(FS_PATH, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(FS_PATH)
    return
