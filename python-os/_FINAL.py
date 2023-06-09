from fileCheck import *
from fileCompare import *
from listConvert import *


# PATH
myPath1 = input("First  Path:   ")
myPath2 = input("Second Path:   ")

# DATABASE
dataBase1 = []
dataBase2 = []

# BASIC LIST
basicList1 = []
basicList2 = []

# ---------------------------------------------------------------

# FILECHECK
FileCheck(myPath1, dataBase1)
FileCheck(myPath2, dataBase2)

# LISTCONVERTER
ListConvert(dataBase1, basicList1)
ListConvert(dataBase2, basicList2)

# FILECOMPARE
FileCompare(basicList1, basicList2)
