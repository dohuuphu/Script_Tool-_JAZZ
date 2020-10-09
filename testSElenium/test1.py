#from Add_lib import *
import threading
import time
import sys
count = 0
def daemon():
    global count
    while(count<10):
        print (threading.currentThread().getName(),"daemon:" ,count)
        time.sleep(1)
        count +=1

 
def non_daemon():
    global count
    while(count<10):
            print (threading.currentThread().getName(),"Non_daemon:" ,count)
            time.sleep(1)
            count +=1
 

def check():
    global count
    while(count<15):
        print (threading.currentThread().getName(),"check:" ,count)
        time.sleep(1)
        count +=1
        if(count > 5):
            print("ok let's go")
            #d.setDaemon(True)
            time.sleep(2)
            #d.setDaemon(False)
            print("ok END")
        else:
            print("count <5")

#def main():
    

		
if __name__ == "__main__":
        d = threading.Thread(name='daemon', target=daemon)
        #t = threading.Thread(name='non_daemon', target=non_daemon)
        #c = threading.Thread(name='check', target=check)
        d.setDaemon(True)
        d.start()
        #c.start()
        #c.join()
        time.sleep(2)
        print("end")
