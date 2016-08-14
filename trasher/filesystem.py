import os
import shutil

def listdir_with_prefix(start):
    if not os.path.isdir(start):
        raise ValueError("Must be a directory")
    if not start.endswith('/'):
        start += '/'
    for subentry in os.listdir(start):
        with_prefix = start + subentry
        if os.path.isdir(with_prefix):
            with_prefix += '/'
        yield with_prefix

def remove(entry):
    if os.path.isdir(entry):
        shutil.rmtree(entry)
    else:
        os.remove(entry)

def move(entry, destination):
    shutil.move(entry, destination)

def traversal(directory):
    for entry in listdir_with_prefix(directory):
        enter = yield entry
        if enter and os.path.isdir(entry):
            yield from traversal(entry)
