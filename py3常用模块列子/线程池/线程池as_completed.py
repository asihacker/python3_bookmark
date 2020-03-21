import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


# 参数times用来模拟网络请求的时间
def get_page():
    code = requests.get('http://www.17golink.xyz/').status_code
    return code


if __name__ == '__main__':
    t1 = time.time()
    obj_list = list()
    executor = ThreadPoolExecutor(max_workers=100)
    for key in range(100):
        obj = executor.submit(get_page)
        obj_list.append(obj)
    for future in as_completed(obj_list):
        data = future.result()
        print(f"main: {data}",future)
    print(123)
    # t2 = time.time() - t1
    # print(t2)
    # t1 = time.time()
    # for key in range(50):
    #     get_page()
    # # print(456)
    # t2 = time.time() - t1
    # print(t2)
