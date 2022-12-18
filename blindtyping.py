chancesOfRandom = [3, 9, 17, 25, 33, 41, 49, 57, 65, 73]  # шансы: 3,6,8,8,8,8,8,8,8,8
from random import randint
from time import sleep

UserInGame=True
while UserInGame:
    lengthall = 20
    print('-------------------------------------------------------------------------')
    print('Please enter the language that you want to test blind testing in:')
    print('English: 1')
    print('Russian: 0')
    print('-------------------------------------------------------------------------')
    print('Пожалуйста, введите язык, на котором вы хотите опробовать печать вслепую: ')
    print('Английский: 1')
    print('Русский: 0')
    print('-------------------------------------------------------------------------')

    valid = False                   # try except для ввода
    while not valid:
        try:
            language = int(input())                 # ввод в переменную language языка
            if (language != 1) and (language != 0):
                raise ZeroDivisionError
            else:
                valid = True
        except:
            print('Invalid input: try again!')
            print('Неверный ввод: попробуйте снова!')

    if language:                        # обработка введенного языка: language = 1 - это англ
        f = open('Dictionary.txt')      # открывается словарь для английских слов
        dict = f.readline()             # строка записывается в переменную dict
        dict = dict.split(' ')          # dict отныне массив, где каждый элемент - это слово
        LEFT_BORDERS = [0, 52, 104, 304, 504, 704, 904, 1104, 1304, 1504]       # левые и правые границы
        RIGHT_BORDERS = [51, 103, 303, 503, 703, 903, 1103, 1303, 1503, 1703]
        howMuchElements = 1704              # кол-во элементов в массиве
        TheBool = [0] * howMuchElements     # булевый массив; в нем изначально все 0
        f.close()

    else:                   # по аналогии обрабатывается русский язык
        f = open('DictionaryRUS.txt')
        dict = f.readline()
        dict = dict.split(' ')
        LEFT_BORDERS = [0, 66, 116, 316, 516, 716, 916, 1116, 1316, 1516]
        RIGHT_BORDERS = [65, 115, 315, 515, 715, 915, 1115, 1315, 1515, 1715]
        howMuchElements = 1716
        TheBool = [0] * howMuchElements
        f.close()

    if language:  # вывод условия выхода из тренажера
        print()
        print('--------------------------------')
        print('In order to exit please type: 13')
        print('--------------------------------')
        print()
    else:
        print()
        print('------------------------------------')
        print('Для выхода из программы напишите: 13')
        print('------------------------------------')
        print()


    def clearing(index):    # функция очистки диапазона элементов длины index+1
        # проверка диапазона для данного индекса на наличие нулей
        if TheBool[LEFT_BORDERS[index]:RIGHT_BORDERS[index] + 1].count(0) == 0:
            for j in range(LEFT_BORDERS[index], RIGHT_BORDERS[index] + 1):  # range(0,4) = (0,1,2,3)
                TheBool[j] = 0


    def find_word(currLength):      # функция подбора массива длиной currLength
        currWord = []               # инициализация пустого массива
        while currLength != 0:      # подбор слов до тех пор, пока не будет достигнута длниа
            if currLength >= 10:    # подбор слов длиной до 10
                bufferIndex = randint(1, 73)  # подбор индекса с фиксированными шансами
                i = 0               # i = это длина - 1
                if bufferIndex in range(1, 4):  # обработка длины 1
                    pass
                else:
                    while i < 9 and bufferIndex > chancesOfRandom[i]:
                        i += 1
                clearing(i)         # очистка диапазона булевского массива

            else:                   # подбор слов длиной до текущей длины
                bufferIndex = randint(1, chancesOfRandom[currLength - 1])  # аналогия с предыдущим
                i = 0
                if bufferIndex in range(1, 4):  # range (1,4) = (1,2,3)
                    pass
                else:
                    while i < 9 and bufferIndex > chancesOfRandom[i]:
                        i += 1
                clearing(i)

            indexForDict = randint(LEFT_BORDERS[i], RIGHT_BORDERS[i])  # поиск слова определенной длины

            while TheBool[indexForDict] == 1:  # ищем другое, если попалась 1
                indexForDict = randint(LEFT_BORDERS[i], RIGHT_BORDERS[i])

            currWord.append(dict[indexForDict])     # добавление в массив слова
            currLength -= i + 1                     # currLength:= currLenght - (i+1)
            # if indexForDict != 0:          // это старое правило для единиц; отныне единицы чищатся, как и другие
            TheBool[indexForDict] = 1               # говорим, что это слово больше брать нельзя
        return currWord  # возвращаем длину слова


    def word_for_length(theLength):     # функция подбора слова определенной длины (до 10)
        theLength -= 1                  # так как нумерация с 0
        clearing(theLength)             # очистка длины
        indexForDict = randint(LEFT_BORDERS[theLength], RIGHT_BORDERS[theLength])  # аналогия с предыдущей функцией
        while TheBool[indexForDict]:
            indexForDict = randint(LEFT_BORDERS[theLength], RIGHT_BORDERS[theLength])
        oneWord = dict[indexForDict]    # oneWord - полученное слово, его мы и возвращаем в функции
        TheBool[indexForDict] = 1
        return oneWord


    """
    Виталя, сделай подбор разбиения слов длиной больше 10 через find_word,
    а те, что меньше 10, через функцию word_for_length
    """

    Flag = False
    mnoj = 2
    str1 = []
    while lengthall + len(str1) - 1 < 211:

        if not (Flag):
            str1 = find_word(lengthall)
        else:
            str1 = strarray
        for i in str1:
            print(i, end=' ')
        print()

        strarray = []  
        str2 = input().split(' ')
        if len(str2) == 1 and str2[0] == '13':
            break
        Flag = False

        if len(str1) > len(str2):
            Flag = True

        for i in range(len(str1)):
            buf = []
            for j in range(len(str1[i])):
                buf.append(1)
            if i > len(str2) - 1:
                for j in range(len(str1[i])):
                    buf[j] += mnoj - 1
                    lengthall += mnoj - 1


            else:
                for j in range(len(str1[i])):
                    if (j > len(str2[i]) - 1) or (str1[i][j] != str2[i][j]):
                        try:
                            TheBool[dict.index(str1[i])] = 0
                        except:
                            pass
                        Flag = True
                        buf[j] += mnoj - 1
                        lengthall += mnoj - 1

                if len(str1[i]) < len(str2[i]):
                    try:
                        TheBool[dict.index(str1[i])] = 0
                    except:
                        pass
                    Flag = True

            s = ''
            if Flag:
                for j in range(len(str1[i])):

                    for g in range(buf[j]):
                        s = s + str1[i][j]
            else:
                s = str1[i]
            if (len(s) == len(str1[i])) and (Flag):
                if len(s) <= 10:
                    strarray.append(word_for_length(len(s)))
                else:
                    strarray = strarray + find_word(len(str1[i]))
            else:
                strarray.append(s)
        print()
        if not (Flag):
            lengthall -= 2

        if lengthall < 1:
            mnoj = mnoj * 2
            lengthall = 20
            if language:
                print()
                print('-----------------------------')
                print('You have reached a new level!')
                print('-----------------------------')
                print()
            else:
                print()
                print('----------------------------')
                print('Вы перешли на новый уровень!')
                print('----------------------------')
                print()

    if language:
        if lengthall + len(str1) - 1 > 211:
            print('Unfortunately, you have lost.')
            print()
        else:
            print('Thank you for playing!')
            UserInGame=False
    else:
        if lengthall + len(str1) - 1 > 211:
            print('К сожалению, вы проиграли.')
            print()
        else:
            print('Спасибо за игру!')
            UserInGame=False
    sleep(2)
