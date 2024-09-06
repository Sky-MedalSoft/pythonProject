# 多线程
import time
import threading


def ring():
    while 1:
        print("ring...")
        time.sleep(1)

def dance():
    while 1:
        print("dance...")
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=ring)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()