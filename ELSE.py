a = float (input("a="))
b = float (input("b="))
c = float (input("c="))
if  a > b:
    print("Свершилось!")
elif int (b) > int (a):
    print("Да ну!")
else:
    print("А если так?")
    print("a+c=",int (a+c))
    print("b-c=",int (b-c))
    if int (a+c)> int (b-c):
        print("Свершилось!")
    elif int (a+c)< int (b-c):
        print("Да ну!")
