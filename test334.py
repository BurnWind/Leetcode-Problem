# 递增的三元子序列：https://leetcode-cn.com/problems/increasing-triplet-subsequence/
# **

class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = nums[0], float("inf")
        for i in range(1, n):
            num = nums[i]
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
        return False


if __name__ == '__main__':
    nums = [4, 10, 3, 4, 2, 10]
    s = Solution()
    print(s.increasingTriplet(nums))


# 总结
# 贪心算法
