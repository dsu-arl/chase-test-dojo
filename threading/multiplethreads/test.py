import threading
from time import sleep

def thread_func():
    print(1)
    sleep(15)

t1 = threading.Thread(target=thread_func())
t2 = threading.Thread(target=thread_func())
t3 = threading.Thread(target=thread_func())

t1.start()
t2.start()
t3.start()

print("waiting..")


t1.join()
t2.join()
