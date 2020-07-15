import asyncio
import threading


async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)


if __name__ == '__main__':
    # print(asyncio.iscoroutinefunction(do_some_work))  # True
    threading.Thread(target=do_some_work,args=[3]).start()