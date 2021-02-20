import math

#Ex1

# a = float(input('Give a nunber: ')) #float
# while a != 0:
#     if a % 2 == 0:
#         print('{} is even'.format(a))
#     else:
#         print('{} is odd'.format(a))
#     a=float(input('Give a nunber: '))

#Ex2
def GCD(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    div=1
    for n in range(1,n1+1):  #range(1,5+1) 1,2,3,4,5
        if n1%n == 0 and n2%n == 0:
            div=n
    return div

# str = input("Give two number and separate with coma: ")
# a,b=str.split(',')
# print(a,b)
# print(GCD(int(a),int(b)))


#Ex3
def dist(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# s1 = input('Give the (x,y) coodinate of the fisrt piont:')
# s2 = input('Give the (x,y) coodinate of the second piont:')
#
# x1,y1 = s1.split(' ')
# x2,y2 = s2.split(' ')
#
# print('A ({},{}) és a ({},{}) pont távolasága: {:.3f}'.format(x1,y1,x2,y2,dist(int(x1),int(x2),int(y1),int(y2))))

#Ex4
def SumOfDigits(n):  #1234
    sum=0
    while n>0:
        sum += n%10
        n //= 10
    return sum

# n=int(input('Adjon meg egy számot: '))
# print('A számjegyek összege: {}'.format(SumOfDigits(n)))


#Ex5


def UniqueSortedWords(list): #['red','white'...]
    list.sort()
    newList=[]
    for str in list:
        if str not in newList:
            newList.append(str)
    return newList

ex5List=['red','white','black','red','green','black']
print(UniqueSortedWords(ex5List))

str='red,white,black,red,green,black'
str2=str.split(',')
print(UniqueSortedWords(str2))
