#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 19:54
# @Author  : AsiHacker
# @File    : aes.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt(key, data):
    '''
    AES的ECB模式加密方法
    :param key: 密钥
    :param data:被加密字符串（明文）
    :return:密文
    '''
    key = key.encode('utf8')
    # 字符串补位
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    result = cipher.encrypt(data.encode())
    encodestrs = base64.b64encode(result)
    enctext = encodestrs.decode('utf8')
    print(enctext)
    return enctext


def decrypt(key, data):
    '''

    :param key: 密钥
    :param data: 加密后的数据（密文）
    :return:明文
    '''
    key = key.encode('utf8')
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)
    # 去补位
    text_decrypted = unpad(cipher.decrypt(data))
    text_decrypted = text_decrypted.decode('utf8')
    print(text_decrypted)
    return text_decrypted


if __name__ == '__main__':
    key = '2RAjqiBvIh0OuwbN'

    data = '{"venueEnName":"XJTY","gameCode":"","clientType":"H5","isManualLaunch":false,"isUseCache":false,"isApp":false,"https":true,"rollbackAddress":"https://www.yabo858.com/app/venue-back?token=HY_IFrReNZbnnMJEx8PILhDpmKA6K09k4TE8FP1HusFYAeFijsAvcl3mlRQIsC2tIF4"}'

    ecdata = encrypt(key, data)
    decrypt(key, ecdata)
