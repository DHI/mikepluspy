import os
from mikeplus import DataTableAccess
from os import listdir
from os.path import isfile, join


def update_sqlite_dbs(directory: str):
    myDir = os.path.abspath(directory)

    subdirs = listdir(myDir)
    i = 0
    count = len(subdirs)
    while i < count:
        subdirs[i] = join(myDir, subdirs[i])
        i = i + 1

    while len(subdirs) != 0:
        file_path = subdirs[0]
        subdirs.remove(file_path)
        if isfile(file_path):
            filename, file_extension = os.path.splitext(file_path)
            if file_extension == ".sqlite":
                print("Do database upgrading for " + file_path)
                data_access = DataTableAccess(file_path)
                data_access.open_database()
                data_access.close_database()
        else:
            sec_sub_dirs = listdir(file_path)
            if sec_sub_dirs is not None:
                for item in sec_sub_dirs:
                    f = join(file_path, item)
                    subdirs.append(f)
