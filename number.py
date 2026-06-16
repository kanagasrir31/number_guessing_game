import random
sc=random.randint(0,100)

while True:
    gu=int(input("Enter a number"))
    if sc==gu:
        print("gueseeed number is correct")
        break
    elif sc < gu:
        print("Too high")
    else:
        print("Too low")    
