#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 15:29
# @Author  : AsiHacker
# @File    : 两数之和.py
# @Software: PyCharm
# @notice  : True masters always have the heart of an apprentice.
# 给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 的那两个整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
# 你可以按任意顺序返回答案。
#
# 示例 1：
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []


if __name__ == '__main__':
    example = Solution()
    # print(example.twoSum(nums=[2, 7, 11, 15], target=9))
    # print(example.twoSum(nums=[3, 3], target=6))
    print(example.twoSum(nums=[3, 2, 4], target=6))
