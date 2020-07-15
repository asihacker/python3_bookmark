import hashlib

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad


class AESCipher(object):
    def __init__(self, key):
        self.key = key
        self.d_iv = hashlib.new('md5', key).digest()
        self.e_iv = hashlib.new('md5', key).digest()

    def decrypt(self, enc: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_CBC, self.d_iv)
        result = unpad(cipher.decrypt(enc), AES.block_size)
        self.d_iv = enc[len(enc) - 16:]
        return result

    def encrpyt(self, clear: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_CBC, self.e_iv)
        result = cipher.encrypt(pad(clear, AES.block_size))
        self.e_iv = result[len(result) - 16:]
        return result


if __name__ == '__main__':
    cipher = AESCipher('0123456789abcdef0123456789abcdef'.encode())

    encrypt1 = cipher.encrpyt('123'.encode())
    print(encrypt1)

    encrypt2 = cipher.encrpyt('45617'.encode())
    print(encrypt2)

    print(cipher.decrypt(encrypt1))
    print(cipher.decrypt(encrypt2))
