from config import *
#a=0
def plus():
    global a
    a +=1
    print("a= ", a)
    return  a

def sub():
    global a
    if(a ==1 ):
        print(" 1:correct")
    a = a-1
    print("a= ", a)
    return a