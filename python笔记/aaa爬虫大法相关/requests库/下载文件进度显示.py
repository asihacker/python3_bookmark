# -*- coding: utf-8 -*-
import os
import time
import requests
from tqdm import tqdm


# 请求下载地址，以流式的。打开要下载的文件位置。
def download(path, download_url, filename):
    source_path = path
    path = f'{path}{os.sep}{filename}'
    with requests.get(download_url, stream=True) as r, open(path, 'wb') as file:
        # 请求文件的大小单位字节B
        total_size = int(r.headers['content-length'])
        # 以下载的字节大小
        content_size = 0
        # 进度下载完成的百分比
        plan = 0
        # 请求开始的时间
        start_time = time.time()
        # 上秒的下载大小
        temp_size = 0
        # 开始下载每次请求1024字节
        jdt = tqdm(r.iter_content(chunk_size=1024))
        for content in jdt:
            file.write(content)
            # 统计以下载大小
            content_size += len(content)
            # 计算下载进度
            plan = (content_size / total_size) * 100
            # 每一秒统计一次下载量
            if time.time() - start_time > 1:
                # 重置开始时间
                start_time = time.time()
                # 每秒的下载量
                speed = content_size - temp_size
                # KB级下载速度处理
                if 0 <= speed < (1024 ** 2):
                    # jdt.set_description(f"正在更新：{source_path}{os.sep}{file}")
                    print('正在下载更新文件', round(plan, 2), '%', round(speed / 1024, 2), 'KB/s')
                # MB级下载速度处理
                elif (1024 ** 2) <= speed < (1024 ** 3):
                    print('正在下载更新文件', round(plan, 2), '%', round(speed / (1024 ** 2), 2), 'MB/s')
                # GB级下载速度处理
                elif (1024 ** 3) <= speed < (1024 ** 4):
                    print('正在下载更新文件', round(plan, 2), '%', round(speed / (1024 ** 3), 2), 'GB/s')
                # TB级下载速度处理
                else:
                    print('正在下载更新文件', round(plan, 2), '%', round(speed / (1024 ** 4), 2), 'TB/s')
                # 重置以下载大小
                temp_size = content_size
    return path, source_path
