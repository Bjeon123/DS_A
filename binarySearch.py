import math
sortedArr = [1,4,5,12,15,20,23,26]


def binarySearch(arr, target):
    if len(arr) == 0:
        return -1
    mid = math.floor(len(arr) / 2)
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return mid + binarySearch(arr[mid:],target)
    else:
        return binarySearch(arr[0:mid],target)

print(binarySearch(sortedArr,3))