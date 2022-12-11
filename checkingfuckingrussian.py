f = open('dictionaryRUS.txt')
dict = f.read().split()
f.close()
LEFT_BORDERS = [0, 66, 116, 316, 516, 716, 916, 1116, 1316, 1516]
RIGHT_BORDERS = [65, 115, 315, 515, 715, 915, 1115, 1315, 1515, 1715]