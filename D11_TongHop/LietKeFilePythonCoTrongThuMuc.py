import os

def search_py_thon_file(directory, pyfiles):
    """Liet ke cac file py trong thu muc

    :param directory: thu muc
    :return:
    """
    items = os.listdir(directory)
    print(items)
    for item in items:
        full_path = os.path.join(directory, item)
        print(item, full_path)
        if os.path.isfile(item):
            pyfiles.append(full_path)
            print("Added ", full_path)
        elif os.path.isdir(item):
            # Goi de quy
            search_py_thon_file(full_path, pyfiles)

from pathlib import Path
currDir = Path(os.getcwd())
print("TM: ", currDir)
print("TM: ", currDir.parent)
pyfiles = []
search_py_thon_file(currDir.parent, pyfiles)
# search_py_thon_file(currDir, pyfiles)
print(pyfiles)