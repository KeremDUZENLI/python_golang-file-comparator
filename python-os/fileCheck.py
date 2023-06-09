from os import listdir
from os.path import isfile, join


def FileCheck(filePath, dataBase):
    liste = []

    for i in listdir(filePath):
        if isfile(join(filePath, i)):
            liste.append(i)
        else:
            newPath = filePath + "/" + i
            FileCheck(newPath, dataBase)

    dataBase.append(liste)
