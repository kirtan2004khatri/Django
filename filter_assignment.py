
import os
from this import d
os.system('cls')

# 1
l1=[1,22,-1,-5,89,-90,-5,25,65,0]
def negative_filter(i):
    if(i<0):
        return i

result=list(filter(negative_filter,l1))
# print("Negative numbers in collections are : {0} ".format(result))

#2
l2=[1,2,3,4,5,6,7,8,9,10,11]

def even_filter(item):
    if(item%2!=0):
        return item

result=list(filter(even_filter,l2))
# print("Odd numbers in collections are : {0}".format(result))

#3
string="Hii hello little butterfly again"

def filter_vowel(item):
    item=item.lower()
    vowels=["a","e","i","o","u"]
    for i in item:
        if(i in vowels):
            return i

result=list(set(filter(filter_vowel,string)))
# print("The vowels in the list are : {0}".format(result))

# 4
l3=[1,22,-1,-5,89,-90,-5,25,65,0]
def positive_filter(i):
    if(i>=0):
        return i

# result=list(filter(positive_filter,l3))
# print(result)

# 5
l4=[1,22,-1,-5,89,-90,-5,25,65,0]
def positive_filter2(i):
    if(i<0):
        return True

result=list(map(lambda x:x*-1,filter(positive_filter2,l4)))
print(result)