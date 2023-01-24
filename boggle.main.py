# class TreeNode:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
# def level_i_nodes(root,i):
#     return level_i_help(root,i,0,[])
# def level_i_help(root,i,index,nodes):
#     if index == i:
#         try:
#             nodes.append(root.data)
#         except:
#             pass
#     else:
#         level_i_help(root.left,i,index+1,nodes)
#         level_i_help(root.right,i,index+1,nodes)
#     return nodes
#
# def diff_order(l1,l2):
#     for item in l1:
#         if item not in l2:
#             return False
#     return True
#
# def equal_trees(x,y):
#     if not x or not y:
#         return None
#     i = 0
#     state = True
#     while i <10:
#         try:
#             cur1 = level_i_nodes(x,i)
#             cur2 = level_i_nodes(y,i)
#             print(cur1,cur2)
#             if not diff_order(cur1,cur2) or len(l1)!=len(l2):
#                 state= False
#                 return state
#         except:
#             return state
#         i+=1
#     return state
#
#
# def agregate(f):
#     sols = []
#     def wrapper(x):
#         sols.append(f(x))
#         return sols
#     return wrapper
#
# @agregate
# def f(x):
#     return 2*x
#
# h = agregate(f)
# print(h(4))
#
# class Car:
#     all_cars = []
#     def __init__(self,id_num):
#         self.id_num = id_num
#         if self.id_num in Car.all_cars:
#             raise ValueError
#         self.all_ids = [self.id_num]
#         self.all_cars.append(id_num)
#
#     def change(self,new_num):
#         if new_num not in Car.all_cars:
#             Car.all_cars.remove(self.id_num)
#             self.id_num = new_num
#             self.all_ids.append(new_num)
#             Car.all_cars.append(new_num)
#         else:
#             raise ValueError("fuck you")
#
#     def revert(self):
#         if self.all_ids[0] not in Car.all_cars:
#             self.id_num = self.all_ids[0]
#         else:
#             raise ValueError("EGJR{LHWE")
#
# car = Car("123")
# print(car.change("134"))
# print(car.id_num)
# print(car.change("123"))
# print(car.id_num)
# print(car.change("12344"))
# print(car.id_num)
# print(car.revert())
# print(car.id_num)
# car1 = Car("123")
# print(Car.all_cars)
#
#
#
#
#
#
#
#
#
#
#
#
# root1 = TreeNode(1)
# root1.left = TreeNode(2)
# root1.right = TreeNode(3)
# root1.left.left = TreeNode(4)
# root1.left.right = TreeNode(5)
# root1.right.right = TreeNode(6)
#
# root2 = TreeNode(1)
# root2.left = TreeNode(3)
# root2.right = TreeNode(2)
# root2.left.left = TreeNode(6)
# root2.right.left = TreeNode(5)
# root2.right.right = TreeNode(4)
# print(equal_trees(root1,root2))
# root3 = TreeNode(4)
# root3.left = TreeNode(3)
# root3.right = TreeNode(2)
# root3.left.left = TreeNode(6)
# root3.right.left = TreeNode(5)
# root3.right.right = TreeNode(4)
# root4 = TreeNode(1)
# root4.left = TreeNode(3)
# root4.right = TreeNode(2)
# root4.left.left = TreeNode(6)
# root4.right.left = TreeNode(9)
# root4.right.right = TreeNode(4)
# print(equal_trees(root4,root3))
#
#
#
# # def find_closest(lst,target):
# #     best = None
# #     low = 0
# #     high = len(lst)-1
# #
# #     while low <high:
# #         cur = lst[low] +lst[high]
# #         print(cur)
# #         if cur <target:
# #             low+=1
# #         if cur > target:
# #             high -=1
# #         if cur == target:
# #             return (lst[low],lst[high])
# #         diff = abs(target-cur[low]-cur[high])
# #         if not best or diff < abs(target-best[0]-best[1]):
# #             best = (lst[low],lst[high])
# #
# #     return best
# #
# # print(find_closest([10, 20,30,40,50,60,70], 54))
#
# def fuck_you(n):
#     return fuck_you_h(n,"")
# def fuck_you_h(n,cur_str):
#     if len(cur_str) == n:
#         print(cur_str)
#         return
#     for num in [0,1]:
#         if num ==1 and len(cur_str)>0 and cur_str[-1] ==str(1):
#             cur_str+=str(0)
#
#
#         else:
#             fuck_you_h(n,cur_str+str(num))
#     cur_str=""
# fuck_you(1)
#
# def fuck_hell(prog,vals):
#     for step in prog:
#         all_args = [vals[key] for key in step[2:]]
#         var = step[0]
#         command = step[1](*all_args)
#
#
# def f(x, n):
#     alist = [x] * n
#     for i in range(len(alist)):
#         alist[i][1] -= i
#     for j in range(0, alist[0][1]):
#         for k in range(3, n):
#             print("here")
#             x[0] *= k
#     return x
# print(f([3,4],5))
# def f(s, k):
#     g(s, "", len(s), k)
# def g(s, p, n, k):
#     if (k == 0):
#         print(p)
#         return
#     for i in range(n):
#         np = p + s[i]
#         g(s, np, n, k - 1)
# f(['a', 'b'], 2)
#
# def got_em(l1,l2):
#     return got_em_HELP(l1,l2,0,0)
#
#
# def one_in(num,l2,index):
#     if index==len(l2):
#         return
#     if num == l2[index]:
#         return True
#     if one_in(num,l2,index+1):
#         return True
#
# def all_in(l1,l2):
#     return all_in_help(l1,l2,0)
#
# def all_in_help(l1,l2,index):
#     if index+1 == len(l1):
#         if one_in(l1[index],l2,0):
#             return True
#
#         return False
#
#     if one_in(l1[index],l2,0):
#         if all_in_help(l1,l2,index+1):
#             return True
#     return False
#
# def reverse(head):
# #     le = get_len(head)
# #     now = head
# #     for i in range(le-1):
# #         for i in range(le-1):
# #             node = cur.next
# #             cur.next = node
# #         cur.next = node
# #
# #
# #
# #
# #
# # def get_len(head):
# #     cur = head
# #     le = 0
# #     while True:
# #         cur = cur.next
# #         if cur.next is head:
# #             return le
# #         cur.next = cur
# #     le+=1
# #
#
# def posi(lis,i):
#     return list(map(lambda x: x[i],lis))
#
# def make_closed(dict):
#     i_need = list(dict.items())
#
#     pos_zero = posi(i_need,0)
#     pos_one = posi(i_need,1)
#     sol = []
#     for num in pos_one:
#         if num not in pos_zero:
#             for pos,item in enumerate(i_need):
#                 if i_need[pos][1] == num:
#                     i_need.remove(item)
#     return {i_need[i][0]:i_need[i][1] for i in range(len(i_need))}
#
# print(make_closed({1:2,2:3,3:1,7:8}))
# print(make_closed({1:2,2:3,3:1,7:7}))
# print(make_closed({1:2,2:3,3:1,7:7,"a":7}))
# print(make_closed({1:2,2:3,3:1,7:8,6:5}))
#
#
# def unite(a,b):
#     sol = []
#     for i in range(len(a)):
#         sol.append(a[i])
#         sol.append(b[i])
#     return sol
#
#
# class Node:
#     def __init__(self,data,next=None,prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
#
#
# def weave(a,b):
#     united = unite(a,b)
#     cur = Node(a[0])
#     head = cur
#     for i in range(1, len(united)+1):
#         if i <len(united):
#             cur.next = Node(united[i])
#         if i >1:
#             cur.prev = Node(united[i-1])
#         cur = cur.next
#     return head
#
# def while_weave(head):
#     cur= head
#     while cur:
#         print(cur.data)
#         cur = cur.next
# k  = weave([1,2,3],[4,5,6])
# while_weave(k)
#
#
# def okay(lis,num_peek):
#     count = 0
#     for pos,num in enumerate(lis):
#         if pos == 0:
#             if lis[pos] >= lis[pos+1]:
#                 count+=1
#         elif pos == len(lis)-1:
#             if lis[pos] >= lis[pos-1]:
#                 count+=1
#         else:
#             if lis[pos] >= lis[pos-1] and lis[pos] >= lis[pos+1]:
#                 count +=1
#         if count > num_peek:
#             return False
#     if count == num_peek:
#         return True
#     return False
# print(okay([1, 3, 4, 4, 8, 8, 4, 2],4))
#
#
# def find_vall(lis):
#     return find_vall_h(lis,0)
#
# def find_vall_h(lis,index):
#     print(index)
#     if index == len(lis) - 1:
#         if lis[index] <= lis[index-1]:
#             return index
#         return
#     elif index == 0:
#         if lis[index] <= lis[index+1]:
#             return index
#
#
#     else:
#         if lis[index-1] >= lis[index] and lis[index+1] >=lis[index]:
#             return index
#
#     k = find_vall_h(lis,index+1)
#     if k:
#         return k
#
#
# print(find_vall([1,5,4,3,2,1]))
#
# def make_stack():
#     stack = []
#     def wrapper(*args):
#         if len(args) >0:
#             for arg in args:
#                 stack.append(arg)
#         else:
#             return stack.pop()
#     return wrapper
#
# s = make_stack()
# s(1)
# s(2)
# s(3)
# print(s(),s(),s())
#
#
# def MyDict:
#     def __init__(self):
#         self.dict = []
#
#     def set(self,key,value):
#         if key not in self.keys():
#             self.dict.append((key,value))
#         else:
#             pos = self.dict.index(key)
#             self.dict[pos] = (key,value)
#     def get(self,key):
#         try:
#             pos = self.dict.index(key)
#         except:
#             raise(KeyError):
#                 "reported"
#
#     def keys(self):
#         return [self.dict[i][0] for i in self.dict]
#
#









class Dog:
    def __init__(self,name):
        self.name = name
        Dog.bark = True

    def f(self):
        Dog.bark = False


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
