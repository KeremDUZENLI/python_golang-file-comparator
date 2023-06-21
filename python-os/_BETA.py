import os
from os import listdir
from os.path import isfile, join


listeFolder1 = []
listeFolder2 = []


def FileCheckX(filePath1, filePath2):
    i = 0
    liste1 = []
    liste2 = []

    newPath1 = filePath1
    newPath2 = filePath2

    listeX = listdir(filePath1)

    for deneme1Member in listdir(filePath1):
        if isfile(join(filePath1, deneme1Member)):
            liste1.append(deneme1Member)
        elif newPath1 in listeFolder1:
            continue
        else:
            newPath1 = filePath1 + "/" + deneme1Member
            listeFolder1.append(newPath1)
            print("newPath1: ", newPath1)
            break

    for deneme2Member in listdir(filePath2):
        if isfile(join(filePath2, deneme2Member)):
            liste2.append(deneme2Member)
        elif newPath2 in listeFolder2:
            continue
        else:
            newPath2 = filePath2 + "/" + deneme2Member
            listeFolder2.append(newPath2)
            print("newPath2: ", newPath2)
            break

    for deneme1Member in liste1:
        if liste2.count(deneme1Member) == 0:
            print(
                f"\ndifferent in {filePath1}: {deneme1Member}")

    for deneme2Member in liste2:
        if liste1.count(deneme2Member) == 0:
            print(
                f"\ndifferent in {filePath2}: {deneme2Member}")

    if (newPath1 != filePath1) & (newPath2 != filePath2):
        print("\n\n")
        FileCheckX(newPath1, newPath2)

    if (newPath1 == filePath1) & (newPath2 != filePath2):
        newPath1 = os.path.dirname(os.path.dirname(newPath1))
        FileCheckX(newPath1, newPath2)
        print("ok")

    if (newPath1 != filePath1) & (newPath2 == filePath2):
        newPath2 = os.path.dirname(os.path.dirname(newPath2))
        FileCheckX(newPath1, newPath2)
        print("ok")

    # if (newPath1 == filePath1) & (newPath2 == filePath2):
    #     FileCheckX(filePath1, filePath2)
        #     newPath1 = os.path.dirname(os.path.dirname(newPath1))
        #     newPath2 = os.path.dirname(os.path.dirname(newPath2))
        #     if newPath1 not in listeFolder1:
        #         if newPath2 not in listeFolder2:
        #             FileCheckX(newPath1, newPath2)


mypath1 = r"C:\Users\Kerem\Desktop\deneme1"
mypath2 = r"C:\Users\Kerem\Desktop\deneme2"

FileCheckX(mypath1, mypath2)
print(listeFolder1)
print(listeFolder2)
