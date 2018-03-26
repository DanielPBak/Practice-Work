# Problem:
# https://leetcode.com/contest/weekly-contest-77/problems/max-increase-to-keep-city-skyline/
# Difficulty: Medium
# Runtime: 57ms
# I solved this as a part of contest 27 in 9 minutes.

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_in_rows = []
        max_in_cols = []
        cols = []
        for i in range(0, len(grid[0])):
            cols.append([])
            
        for row in grid:
            m = max(row)
            max_in_rows.append(m)
            for idx, item in enumerate(row):
                cols[idx].append(item)
                
        for col in cols:
            max_in_cols.append(max(col))
            
        total_change = 0
        for idx_g, row in enumerate(grid):
            for idx_r, item in enumerate(row):
                max_val = min(max_in_rows[idx_g], max_in_cols[idx_r])
                change = max_val - item
                total_change += change
                
        return total_change
                