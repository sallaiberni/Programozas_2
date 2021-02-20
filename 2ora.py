#ex1
#
# while True:
#     try:
#         a=int(input("Giva a number: "))
#         print(a)
#         break
#     except ValueError:
#         print("That was not a valid integer")
#
#ex2

# try:
#     myFile=open("E:\\EGYETEM\\GAZDINFÓ\\2. félév\\Programozás 1\\labor\\2. labor input.txt")
#     for str in myFile:
#         print(str)
#     myFile.close()
# except FileNotFoundError:
#     print("The given file is not found.")

#ex3

#első verzió rossz megoldással, a probléma,
# hogy a szövegben pont, vagy vessző is van utána,
#ezért nem számolja azokat

# def numberOfLannister(myFile):
#     num = 0
#     for str in myFile:
#         for word in str.split(" "):
#             if word == "Lannister":
#                 num+=1
#     return num
#
# myFile=open("E:\\EGYETEM\\GAZDINFÓ\\2. félév\\Programozás 1\\labor\\2. labor input.txt")
# print(numberOfLannister(myFile))
#
#
# #második megoldás, amely még mindig nem jó
# # a probléma, hogy itt azt nézi, hogy egy sorban benne van-e,
# # de van olyan sor, ahol 2szer is van
#
# def numberOfLannister(myFile):
#     num = 0
#     for str in myFile:
#         if "Lannister" in str:
#                 num+=1
#     return num
#
# myFile=open("E:\\EGYETEM\\GAZDINFÓ\\2. félév\\Programozás 1\\labor\\2. labor input.txt")
# print(numberOfLannister(myFile))
#
# #harmadik megoldás, amely megfelelő
# #levágjuk a string azon részét, amelyben van a szó
#
# def numberOfLannister(myFile):
#     num = 0
#     for str in myFile:
#         while str.find("Lannister") !=-1:
#             str=str[str.find("Lannister") +1:]
#             num+=1
#     return num
#
# myFile=open("E:\\EGYETEM\\GAZDINFÓ\\2. félév\\Programozás 1\\labor\\2. labor input.txt")
# print(numberOfLannister(myFile))

# ex5 - leghosszabb szó

import string
def longestWord(inputName, outputName):
    try:
        maxLength = 0
        words = []
        inFile = open(inputName, 'r')
        outFile= open(outputName, 'w')
        newStr = ""
        for str in inFile:
            for ch in str:
                if ch not in string.punctuation:
                    newStr+=ch
            listOfWords = newStr.split()
            for word in listOfWords:
                if len(words) > maxLength:
                    words = []
                    words.append(word)
                    maxLength=len(word)
                elif len(word) == maxLength:
                    words.append(word)
        print("The length of the longest word is ", maxLength, "\n The list of them: ", file=outFile)
        for str in words:
            print(str, file=outFile) #nem írja felül az első 2 sort, a 3ikba ír majd
        inFile.close()
        outFile.close()

    except FileNotFoundError:
        print("The given file is not found.")

longestWord('E:\\EGYETEM\\GAZDINFÓ\\2. félév\\Programozás 1\\labor\\2. labor input.txt', 'output.txt')

