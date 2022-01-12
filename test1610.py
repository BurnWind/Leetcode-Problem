# 可见点的最大数目：https://leetcode-cn.com/problems/maximum-number-of-visible-points/
import math
from bisect import bisect_right


class Solution:
    def visiblePoints(self, points: list, angle: int, location: list) -> int:
        angle_list = []
        same_num = 0
        for p in points:
            if p[0] == location[0] and p[1] == location[1]:
                same_num += 1
            else:
                angle_list.append(math.atan2((p[1]-location[1]), (p[0]-location[0])))
        angle_list.sort()
        n = len(angle_list)
        angle_list += [angle + 2 * math.pi for angle in angle_list]
        angle = math.pi * angle/180
        max_num = max((bisect_right(angle_list, angle_list[i] + angle) - i for i in range(n)), default=0)
        return max_num + same_num


if __name__ == '__main__':
    points = [[0, 0], [0, 2]]
    angle = 90
    location = [1, 1]
    s = Solution()
    print(s.visiblePoints(points, angle, location))


# 总结点：
# 官方两种解法：二分查找，滑动窗口
# 数据结构：二分查找
