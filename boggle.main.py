
def binary_search_recursive(arr, low, high, x):
    if low <= high:
        mid = (high + low) // 2
        # If x is greater than mid, ignore left half
        if arr[mid] < x:
            return binary_search_recursive(arr, mid + 1, high, x)
        # If x is smaller than mid, ignore right half
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        # x is present at mid
        else:
            return mid
    else:
        # element is not present in array
        return -1
# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#
#         mid = (high + low) // 2
#
#         # If x is greater, ignore left half
#         if arr[mid] < x:
#             low = mid + 1
#
#         # If x is smaller, ignore right half
#         elif arr[mid] > x:
#             high = mid - 1
#
#         # x is present at mid
#         else:
#             return mid
#
#     # If we reach here, then the element was not present
#     return -1

print(binary_search_recursive([1,2,3,4,5,6,7],6,7,0))
# print(binary_search([1,2,3,4,5,6,7],10))
# print(binary_search([1,2,3,4,5,6,7],3))
# print(binary_search([1,2,3,4,5,6,7],2))

k = [[i]*i for i in range(1,3)]
for i in range(1,4):
    k =list((k*i,k+k))




def count(l,inst , s):
    if isinstance(l, inst):
        s.append(id(l))
        for sub in l:
            if id(sub) not in s: # כדי שלא ייכנס ללופ איינסופי עם עצמו
                count(sub, inst, s)
    return s



print(count(k,list,[]))
