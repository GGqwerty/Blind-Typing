lengthall=20
from random import randint


print('Please enter the language that you want to test blind testing in:')
print('English: 1')
print('Russian: 0')
print('')
print('Пожалуйста, введите язык, на котором вы хотите опробовать печать вслепую: ')
print('Английский: 1')
print('Русский: 0')
print('')

valid=False
while not valid:
    try:
        language = int(input())
        if (language!=1) and (language!=0):
            raise ZeroDivisionError
        else:
            valid = True
    except:
        print('Invalid input: try again!')
        print('Неверный ввод: попробуйте снова!')


# 1 - это англ, 0 - это русский
language = 1
if language:
    f = open('Dictionary.txt')
    dict = f.readline()
    dict = dict.split(' ')
    LEFT_BORDERS = [0, 52, 104, 304, 504, 704, 904, 1104, 1304, 1504]
    RIGHT_BORDERS = [51, 103, 303, 503, 703, 903, 1103, 1303, 1503, 1703]
    bool = [0] * 1704
    f.close()
else:
    #   f = open('      Dictionary FOR RUSSIAN   .txt')
    # dict = f.readline()
    # dict = dict.split(' ')
    LEFT_BORDERS = [0,    66,     132,332,532,732,932,1132,1332,1532]
    RIGHT_BORDERS = [65,    131,    331,531,731,931,1131,1331,1531,1731]
    bool = [0] * 1732
    # f.close()


currWord = []
def find_word(currLength):
    currWord=[]
    while currLength!=0:
        if currLength >= 10:
            i = randint(1,10)-1
        else:
            i = randint(1,currLength)-1
        indexForDict = randint(LEFT_BORDERS[i],RIGHT_BORDERS[i])
        if bool[indexForDict]:
            pass
        else:
            currWord.append(dict[indexForDict])
            currLength-=i+1
            bool[indexForDict] = 1
    return currWord

def word_for_length(theLength):
    theLength-=1
    indexForDict = randint(LEFT_BORDERS[theLength],RIGHT_BORDERS[theLength])
    while bool[indexForDict]:
        indexForDict = randint(LEFT_BORDERS[theLength], RIGHT_BORDERS[theLength])
    oneWord = dict[indexForDict]
    bool[indexForDict] = 1
    return oneWord
""""""
Flag=False

while lengthall>0:

    if not (Flag):
        str1=find_word(lengthall)
    else:
        str1=strarray
    for i in str1:
        print(i,end=' ')
    print()
        

    strarray=[]
    str2=input().split(' ')
    flagYbav=True
    Flag=False
    if len(str1)>len(str2):
        Flag=True
        flagYbav=False

    for i in range(len(str1)):    
        buf=[]
        for j in range(len(str1[i])):
            buf.append(1)
        if i>len(str2)-1:
            for j in range(len(str1[i])):
                buf[j]+=1
                lengthall+=1


        else:
            for j in range(len(str1[i])):
                if j>len(str2[i])-1:
                    Flag=True
                    buf[j]+=1
                    lengthall+=1
                    flagYbav=False
                else:
                    if str1[i][j]!=str2[i][j]:
                        Flag=True
                        buf[j]+=1
                        lengthall+=1
                        flagYbav=False
        s=''
        k=[]
        if Flag:
            for j in range(len(str1[i])):
                
                for g in range(buf[j]):
                    s=s+str1[i][j]
        else:
            s=str1[i]
        if len(s)==len(str1[i]):
            k=find_word(len(str1[i]))
            strarray=strarray+k
        else:
            strarray.append(s)
    print()
    if flagYbav:
        lengthall-=2
print('You are winner sun')        
    









































"""
from random import randint


print('Please enter the language that you want to test blind testing in:')
print('English: 1')
print('Russian: 0')
print('')
print('Пожалуйста, введите язык, на котором вы хотите опробовать печать вслепую: ')
print('Английский: 1')
print('Русский: 0')
print('')

valid=False
while not valid:
    try:
        language = int(input())
        if (language!=1) and (language!=0):
            raise ZeroDivisionError
        else:
            valid = True
    except:
        print('Invalid input: try again!')
        print('Неверный ввод: попробуйте снова!')


if language:
    f = open('Dictionary.txt')
    dict = f.readline()
    dict = dict.split(' ')
    LEFT_BORDERS = [0, 52, 104, 304, 504, 704, 904, 1104, 1304, 1504]
    RIGHT_BORDERS = [51, 103, 303, 503, 703, 903, 1103, 1303, 1503, 1703]
    bool = [0] * 1704
    f.close()
else:
    #   f = open('      Dictionary FOR RUSSIAN   .txt')
    # dict = f.readline()
    # dict = dict.split(' ')
    LEFT_BORDERS = [0,    66,     132,332,532,732,932,1132,1332,1532]
    RIGHT_BORDERS = [65,    131,    331,531,731,931,1131,1331,1531,1731]
    bool = [0] * 1732
    # f.close()


currWord = []
def find_word(currLength):
    while currLength!=0:
        if currLength >= 10:
            i = randint(1,10)-1
        else:
            i = randint(1,currLength)-1
        indexForDict = randint(LEFT_BORDERS[i],RIGHT_BORDERS[i])
        if bool[indexForDict]:
            pass
        else:
            currWord.append(dict[indexForDict])
            currLength-=i+1
            bool[indexForDict] = 1
    return currWord

def word_for_length(theLength):
    indexForDict = randint(LEFT_BORDERS[theLength],RIGHT_BORDERS[theLength])
    while bool[indexForDict]:
        indexForDict = randint(LEFT_BORDERS[theLength], RIGHT_BORDERS[theLength])
    oneWord = dict[indexForDict]
    bool[indexForDict] = 1
    return oneWord


# INSERT THE LENGTH HERE
find_word(20)
print(currWord)"""



