import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import threading


# 参数times用来模拟网络请求的时间
def get_page(a):
    time.sleep(a)
    code = requests.get('http://www.17golink.xyz/').status_code
    return f'{code},{a},{threading.current_thread().getName()}'


if __name__ == '__main__':
    t1 = time.time()
    executor = ThreadPoolExecutor(max_workers=50, thread_name_prefix='asi')
    c_list = [1, 2, 3, 3, 2, 1, 2, 3, 1]
    for data in executor.map(get_page, c_list):
        print(f"main: {data}")
    # t1 = time.time()
    # for key in range(50):
    #     get_page()
    # t2 = time.time() - t1
    # print(t2)
