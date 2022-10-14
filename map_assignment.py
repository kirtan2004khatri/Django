import os
import math
os.system('cls')

# 1
l1=[4,5,6,7,8]
def tripler(item):
    return math.floor(math.pow(item,3))

result=list(map(tripler,l1))
# print("The triped values are  : {0}".format(result))

# 2 
l2=[1,2,3,4,5,6,7,8,9,10,11] 
def even_filter(item):
    if(item%2==0):
        return item
def odd_filter(item):
    if(item%2!=0):
        return item
result1=list(filter(lambda x:x,map(even_filter,l2)))
result2=list(filter(lambda x:x,map(odd_filter,l2)))
# print("Odd numbers : {0}".format(result1))
# print("Even numbers : {0}".format(result2))

# 3
string=("ABC","DEF","GHI","JKL")

def to_lower(item):
    return item.lower()

result=tuple(map(to_lower,string))
# print(result)

# 4
l3=[1,2,3,4,5]
def doubler(item):
    return math.sqrt(item)

result=list(map(doubler,l3))
# print("The sqrt values are  : {0}".format(result))

# 5
string="this is a small string and is a string of good things"
t_list=[]
def el_dup(item):
    if(item not in t_list):
        t_list.append(item)
        return item
result=list(filter(lambda x:x,(map(el_dup,string.split(" ")))))
# print("String without duplicate words : {0}".format(result))

# 6
# num=int(input("Enter a number to print the table : "))
# limit=int(input("Enter the limit of the table : "))
# for i in range(1,limit+1):
#     print("{0} x {1} = {2}".format(num,i,num*i))

# 7
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]

l3=l1+l3
# print(l3)

# 8
l4=[1.2,2,3,3.5,6.5,7]
def float_int_convert(item):
    if(type(item)==float):
        # 1
        return int(item)
        
        # 2
        # return math.floor(item)
        
        # 3
        # return math.ceil(item)

        # 4
        # return math.trunc(item)
    else:
        return item
result=list(map(float_int_convert,l4))
# print(result)

# 9
given_set={1,2,3,4,5,6,78,98,56}

li=list(given_set)
li.reverse()

# print(li)
# print(set(li))

# 10
emails={1:"kiRtan",2:"THOMAS",3:"KING"}

def email_maker(item):
    item[1]+"@gmail.com"
    return item[1]

result = dict(map(email_maker,list(emails.items())))

print(result)
