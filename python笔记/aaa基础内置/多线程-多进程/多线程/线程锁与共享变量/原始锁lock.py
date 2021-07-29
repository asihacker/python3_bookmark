import threading

lock = threading.Lock()
lock.acquire()


def func():
    lock.release()
    print("lock is released")


t = threading.Thread(target=func)
t.start()
