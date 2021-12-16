# 图表算法主要分为无向图和有向图
# 无向图
# 程序存储方式:
# 1.邻接矩阵:大量的点互相连接的情况下，使用邻接矩阵更直观，否则浪费空间
# 2.邻接列表:反之，小量的点连接使用邻接列表，节省空间
# 涉及的算法应用：深度优先搜索和广度优先搜索

# 深度优先搜索适合解决的问题（depth-first search）
# a.给定一个点，求所有它能抵达的所有点。
# b.给定两个点，它们是否能抵达彼此，如果能，求路线。

class DepthFirstPaths:

    def __init__(self, graph: list):
        self.graph = graph  # 图表
        self.depth = len(graph)  # 深度
        self.marked = [0] * self.depth  # 标记列表（用于标记哪个点已遍历）
        self.last = [-1] * self.depth  # 记录每个点的上一个点
        self.group = {}  # 相连点分组

    # 用邻接矩阵存储
    def dfs_matrix(self):
        for i in range(self.depth):
            for j in range(self.depth):
                pass
