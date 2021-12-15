# 喧闹和富有:https://leetcode-cn.com/problems/loud-and-rich/


class Solution:
    def loudAndRich(self, richer: list, quiet: list) -> list:
        length = len(quiet)
        richer_list = [[] for _ in range(length)]
        for r in richer:
            richer_list[r[1]].append(r[0])
        answer = [-1] * length

        def dfs(x: int):
            if answer[x] != -1:
                return
            answer[x] = x
            for y in richer_list[x]:
                dfs(y)
                if quiet[answer[y]] < quiet[answer[x]]:
                    answer[x] = answer[y]
        for i in range(length):
            dfs(i)
        return answer


if __name__ == '__main__':
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    s = Solution()
    s.loudAndRich(richer, quiet)


# 总结点：
# 官方两种解法：深度优先搜索，拓扑排序
# 数据结构：有向图

