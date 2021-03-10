#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 15:25
# @Author  : AsiHacker
# @File    : 删除字符串中的所有相邻重复项.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.

# 输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，
# 其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。


class Solution:
    def removeDuplicates(self, S: str) -> str:
        skt = list()
        _ = [skt.pop() if skt and k == skt[-1] else skt.append(k) for k in S]
        print(skt, _)
        return ''.join(skt)
        # skt = list()
        #
        # for k in S:
        #     if skt and k == skt[-1]:
        #         skt.pop()
        #     else:
        #         skt.append(k)
        # return ''.join(skt)


if __name__ == '__main__':
    example = Solution()
    print(example.removeDuplicates(S='abbaca'))
