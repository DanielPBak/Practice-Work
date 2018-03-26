# Problem:
# Given a string, find the length of the longest substring without repeating characters.
# Difficulty: Medium
# Runtime: 154ms


from collections import defaultdict
import math
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        indices_dict = defaultdict(list)
        
        for idx, c in enumerate(s):
            indices_dict[c].append(idx)
            
        
        lengths = []
        
        for idx, c in enumerate(s):
            del indices_dict[c][0]
            if (len(indices_dict[c]) == 0):
                lengths.append(len(s) - idx)
            else:
                lengths.append(indices_dict[c][0] - idx)        
        
        maximum = 1
        
        prev = float('inf')
        for i in range(len(lengths)-1, -1, -1):
            prev = min(lengths[i], prev+1)
            maximum = max(prev, maximum)
            
        return maximum