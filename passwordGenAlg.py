import random


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


def wtf():
    uppercaseLetter = chr(random.randint(65, 90))
    uppercaseLetter2 = chr(random.randint(65, 90))
    lowercaseLetter = chr(random.randint(97, 122))
    lowercaseLetter2 = chr(random.randint(97, 122))
    num = str(random.randint(0, 9))
    num2 = str(random.randint(0, 9))
    special = chr(random.randint(35, 36))
    special2 = chr(random.randint(35, 36))

    temp = uppercaseLetter + uppercaseLetter2 + lowercaseLetter + lowercaseLetter2 + num + num2 + special + special2

    og = shuffle(temp)
    return str(og)


def tenLetter():
    uppercaseLetter = chr(random.randint(65, 90))
    uppercaseLetter2 = chr(random.randint(65, 90))
    uppercaseLetter3 = chr(random.randint(65, 90))
    uppercaseLetter4 = chr(random.randint(65, 90))
    lowercaseLetter = chr(random.randint(97, 122))
    lowercaseLetter2 = chr(random.randint(97, 122))
    lowercaseLetter3 = chr(random.randint(97, 122))
    lowercaseLetter4 = chr(random.randint(97, 122))
    num = str(random.randint(0, 9))
    num2 = str(random.randint(0, 9))
    special = chr(random.randint(35, 36))
    special2 = chr(random.randint(35, 36))

    temp = uppercaseLetter + uppercaseLetter2 + lowercaseLetter + lowercaseLetter2 + num + num2 + special + special2 + lowercaseLetter3 + lowercaseLetter4 + uppercaseLetter3 + uppercaseLetter4
    og = shuffle(temp)
    return str(og)


def twentyLetter():
    uppercaseLetter = chr(random.randint(65, 90))
    uppercaseLetter2 = chr(random.randint(65, 90))
    uppercaseLetter3 = chr(random.randint(65, 90))
    uppercaseLetter4 = chr(random.randint(65, 90))
    uppercaseLetter5 = chr(random.randint(65, 90))
    uppercaseLetter6 = chr(random.randint(65, 90))
    lowercaseLetter = chr(random.randint(97, 122))
    lowercaseLetter2 = chr(random.randint(97, 122))
    lowercaseLetter3 = chr(random.randint(97, 122))
    lowercaseLetter4 = chr(random.randint(97, 122))
    lowercaseLetter5 = chr(random.randint(97, 122))
    lowercaseLetter6 = chr(random.randint(97, 122))
    num = str(random.randint(0, 9))
    num2 = str(random.randint(0, 9))
    num3 = str(random.randint(0, 9))
    num4 = str(random.randint(0, 9))
    special = chr(random.randint(35, 36))
    special3 = chr(random.randint(35, 36))
    special2 = chr(random.randint(35, 36))
    special4 = chr(random.randint(35, 36))

    temp = uppercaseLetter + uppercaseLetter2 + lowercaseLetter + lowercaseLetter2 + num + num2 + special + special2 + lowercaseLetter3 + lowercaseLetter4 + \
           uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + lowercaseLetter5 + lowercaseLetter6 + num3 + num4 + special3 + special4
    og = shuffle(temp)
    return str(og)
