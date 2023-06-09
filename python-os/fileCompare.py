def FileCompare(liste1, liste2):
    for i in liste1:
        if liste2.count(i) == 0:
            print(f"\ndifferent in path1: {i}", end="")

    print("\n", end="")

    for l in liste2:
        if liste1.count(l) == 0:
            print(f"\ndifferent in path2: {l}", end="")

    print("\n\n", end="")
