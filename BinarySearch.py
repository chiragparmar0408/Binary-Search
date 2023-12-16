def binarySearch(arr,key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if (key == arr[mid]):
            return mid
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

list1 = []
print("Enter size of list : ")
size = int(input())
print("Enter list elements")
for i in range(0, size):
    ele = int(input())
    list1.append(ele)
print(list1)
key = int(input("Enter search element : "))
print("index of ",key," is ",binarySearch(list1,key))

