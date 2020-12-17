import threading

rock = threading.Lock()
number = 0


def add():
    global number
    global rock
    for i in range(10000000):
        # rock.acquire()
        # print(threading.currentThread().getName())
        rock.acquire()
        number += 1
        rock.release()
        # rock.release()

if __name__ == '__main__':

    thread_1 = threading.Thread(target=add)
    thread_2 = threading.Thread(target=add)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print(number)
