#!/usr/bin/python
# -*- coding: utf-8 -*

import random
import string

import numpy as np
from captcha.image import ImageCaptcha


class generateCaptcha():
    def __init__(self,
                 width=160,  # 验证码图片的宽
                 height=60,  # 验证码图片的高
                 char_num=4,  # 验证码字符个数
                 characters=string.digits + string.ascii_uppercase + string.ascii_lowercase):  # 验证码组成，数字+大写字母+小写字母
        self.width = width
        self.height = height
        self.char_num = char_num
        self.characters = characters
        self.classes = len(characters)

    def gen_captcha(self, batch_size=50):
        X = np.zeros([batch_size, self.height, self.width, 1])
        img = np.zeros((self.height, self.width), dtype=np.uint8)
        Y = np.zeros([batch_size, self.char_num, self.classes])
        image = ImageCaptcha(width=self.width, height=self.height)

        while True:
            for i in range(batch_size):
                captcha_str = ''.join(random.sample(self.characters, self.char_num))
                img = image.generate_image(captcha_str).convert('L')
                img = np.array(img.getdata())
                X[i] = np.reshape(img, [self.height, self.width, 1]) / 255.0
                for j, ch in enumerate(captcha_str):
                    Y[i, j, self.characters.find(ch)] = 1
            Y = np.reshape(Y, (batch_size, self.char_num * self.classes))
            yield X, Y

    def decode_captcha(self, y):
        y = np.reshape(y, (len(y), self.char_num, self.classes))
        return ''.join(self.characters[x] for x in np.argmax(y, axis=2)[0, :])

    def get_parameter(self):
        return self.width, self.height, self.char_num, self.characters, self.classes

    def gen_test_captcha(self):
        image = ImageCaptcha(width=self.width, height=self.height)
        captcha_str = ''.join(random.sample(self.characters, self.char_num))
        img = image.generate_image(captcha_str)
        img.save('demo/'+captcha_str + '.jpg')


if __name__ == '__main__':
    a = generateCaptcha()
    for key in range(10000):
        print(key)
        a.gen_test_captcha()
