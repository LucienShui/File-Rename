import os
from config import *


def rename(path):
    for name in os.listdir(path):
        if name[0] == '.' or name in banList:
            continue
        nextpath = path + os.path.sep + name
        if recursive and os.path.isdir(nextpath):
            rename(nextpath)
        oldName = path + os.path.sep + name
        newName = path + os.path.sep + name.replace(old, new)
        os.rename(oldName, newName)


if __name__ == '__main__':
    rename('.')

