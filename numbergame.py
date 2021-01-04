import random
while True:
    num=int(input("enter any number: "))
    a=random.randint(1,9)
    print("random number is: ",a)
    if num==a:
        print("your guess is right..")
        exit()
    elif num<a :
        print("your guess is low ")
    else:
        print("your guess is high ")