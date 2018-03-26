# Problem:
# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.
# Difficulty: Medium
# Runtime: 289ms (beating 90% of submissions)
# I solved this as a part of contest 25 in 18 minutes.

class Solution(object):
    def allPathsSourceTarget(self, graph):
        return Solution.r_findAllPaths(self, graph[0], graph, 0, [])
        
    def r_findAllPaths(self, node, graph, idx, path_so_far):
        psf = path_so_far + [idx]
        if idx == len(graph) - 1:
            return [psf]
        else:
            if len(node) == 0:
                return False
            
            ret = []
            for i in node:
                ans = Solution.r_findAllPaths(self, graph[i], graph, i, psf)
                if ans:
                    ret = ret + ans
            return ret