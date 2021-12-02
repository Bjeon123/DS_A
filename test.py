# print(None is not None)\
# import math
# arr = list(range(1,10))
# min = min(arr)
# max = max(arr)
# numOccur = arr.count(3)
# str = "Hello World"
# upcase = str.upper();
# downcase = str.lower();

# print(math.ceil(45.3))
# print(5/2)
# print(numOccur)
# import sys

# hashtable = {}
# hashtable[0] = 1
# print( hashtable.get(0))

# num = None
# x = num or 0;
# y = not True
# # print(None < 10)

# arr = [1,2,3,4,5]
# arr2= [4,5]
# for num in range(len(arr)-1):
#     print(arr[num])

# print((True or False) and True )
# print(3*"A")

# arr.pop(2)
# print(arr)

# print([1,2]==[2,1])
# i=1
# if i==1:
#     print("hello")
# elif i < 2:
# print(arr[-2:])

class Car:
    def __init__(self, type, mileage):
        self.__type = type
        self.mileage = mileage

    def getName(self):
        return self.__type


obj1 = Car("honda", 10)
print(obj1.getName())
        