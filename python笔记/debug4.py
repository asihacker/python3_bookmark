class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = list()
        for ch in S:
            if stk and stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        return "".join(stk)


if __name__ == '__main__':
    e = Solution()
    print(e.removeDuplicates(S='abbaca'))
