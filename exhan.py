import os
os.system('cls')

# try:
#     x=int(input("Enter first number:"))
#     y=int(input("Enter second number:"))
#     z=x/y
#     print(z)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# else:
#     print("This is the else block")
#     print("res",z)
# finally:
#     x=0
#     y=0
#     print("This is the final block")

while(True):
    try:
        age=int(input("Enter your age :"))
        if age<18:
            raise ValueError(age)
    except ValueError:
        print(age,"is out of allowed range")
    else:
        print("It worked")
        break