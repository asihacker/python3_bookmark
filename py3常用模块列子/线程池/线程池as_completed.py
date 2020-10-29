import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests


# 参数times用来模拟网络请求的时间
def get_page():
    time.sleep(10)
    code = requests.get('http://www.baidu.com/').status_code
    return code


if __name__ == '__main__':
    t1 = time.time()
    obj_list = list()
    executor = ThreadPoolExecutor(max_workers=100)
    for key in range(100):
        obj = executor.submit(get_page)
        obj_list.append(obj)
    for data in as_completed(obj_list):
        print('data')
    print('www')





