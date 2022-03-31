# 自除数:https://leetcode-cn.com/problems/self-dividing-numbers/
# *

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list:
        res = []
        for i in range(left, right+1):
            if i < 10:
                res.append(i)
                continue
            if "0" in str(i):
                continue
            flag = True
            for c in set(str(i)):
                if i % int(c) != 0:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res


if __name__ == '__main__':
    left = 47
    right = 85
    s = Solution()
    res = s.selfDividingNumbers(left, right)
    print(res)


# 总结点：
# 1.就是一个简单的技巧解题
