# Problem:
# https://leetcode.com/problems/champagne-tower/description/
# Difficulty: Medium
# Runtime: 241ms
# I solved this as a part of contest 75 in 34 minutes.
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        already_determined = {}
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        
        return Solution.r_champagne(self, poured, query_row, query_glass, already_determined)[0]
    
    def r_champagne(self, poured, query_row, query_glass, already_determined):
        if (query_row, query_glass) in already_determined:
            return already_determined[(query_row, query_glass)]
        if query_row == 0:
            
            if poured > 1:
                liquid_in_cup = 1.0
                liquid_overflow = poured - 1
            else:
                liquid_in_cup = poured
                liquid_overflow = 0.0
            already_determined[(query_row, query_glass)] = (liquid_in_cup, liquid_overflow / 2.0)
            return (liquid_in_cup, liquid_overflow / 2.0)
            
            
        left_parent = None
        right_parent = None
        liquid = 0.0
        if query_glass < query_row:
            right_parent = (query_row-1, query_glass)
            extra_liquid = Solution.r_champagne(self, poured, right_parent[0], right_parent[1], already_determined)[1]
            liquid = liquid + extra_liquid
        if query_glass > 0:
            left_parent = (query_row-1, query_glass-1)
            extra_liquid = Solution.r_champagne(self, poured, left_parent[0], left_parent[1], already_determined)[1]
            liquid = liquid + extra_liquid

        if liquid > 1.0:
            liquid_in_cup = 1.0
            liquid_overflow = liquid - 1
        else:
            liquid_in_cup = liquid
            liquid_overflow = 0.0

            
        already_determined[(query_row, query_glass)] = (liquid_in_cup, liquid_overflow / 2.0)
        return (liquid_in_cup, liquid_overflow / 2.0)