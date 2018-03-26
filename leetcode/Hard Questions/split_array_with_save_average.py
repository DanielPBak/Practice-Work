# Problem:
# In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)
# Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.# Difficulty: Hard
# Runtime: 646ms, 87/87 test cases passing

import math
class Solution(object):
    def splitArraySameAverage(self, A):
        memo = {}
        
        def recurse(l, sum_needed, length, so_far):
            if sum_needed == length == 0:
                return True
            elif length == 0:
                return False
            if (tuple(so_far), sum_needed, length) in memo:
                return False
            if sum(l) < sum_needed:
                return False

                return False
            else:
                for i in range(0, len(l)):
                    t = l[i]
                    rest = l[i+1:]
                    if recurse(rest, sum_needed-t, length-1, so_far + [t]):
                        return True
                    else:
                        memo[(tuple(so_far + [t]), sum_needed-t, length-1)] = True
                    
                return False
        """
        :type A: List[int]
        :rtype: bool
        """
        A = sorted(A)
        target_avg = sum(A) / float(len(A))
        for length in range(1, int(math.ceil(len(A) / 2) + 1)):

            sum_needed = length * target_avg

            if sum_needed % 1 > 0.000001:
                continue
            total_sum_needed = math.floor(sum_needed)
            for i in range(0, len(A)):
                t = A[i]
                rest = A[i+1:]
                if recurse(rest, total_sum_needed - t, length-1, [t]):
                    return True
                continue
            
        return False