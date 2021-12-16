# 可见点的最大数目：https://leetcode-cn.com/problems/maximum-number-of-visible-points/
import math


class Solution:
    def visiblePoints(self, points: list, angle: int, location: list) -> int:
        angle_list = []
        for p in points:
            if p[0] == location[0] and p[1] == location[1]:
                continue
            elif p[0] == location[0]:
                angle_list.append(0)
            elif p[1] == location[1]:
                angle_list.append(math.pi / 2)
            else:
                angle_list.append(math.atan2((p[1]-location[1])/(p[0]-location[0])))
        angle_list.sort()
        angle = math.atan2(angle)
        big_other = 0
        small_other = 0
        print(angle_list[1] - angle_list[2])
        for i in angle_list[::-1]:
            if i > angle_list[0] + angle:
                big_other += 1
            else:
                break
        for i in angle_list:
            if i < angle_list[-1] - angle:
                small_other += 1
            else:
                break
        return len(points) - big_other if big_other < small_other else len(points) - small_other


if __name__ == '__main__':
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]]
    angle = 0
    location = [1, 1]
    s = Solution()
    s.visiblePoints(points, angle, location)
