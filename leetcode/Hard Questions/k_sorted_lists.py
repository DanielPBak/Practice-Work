# Problem:
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# Difficulty: Hard
# Runtime: 201ms, 130/130 test cases passing

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import bisect

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ret = []
        lists = [x for x in lists if x]
        if len(lists) == 0:
            return []
        lists.sort(key=lambda node:node.val)
        keys = [node.val for node in lists]
        ret = []
        while(len(keys) > 0):
            smallest = keys[0]
            ret.append(smallest)
            node = lists.pop(0)
            del(keys[0])
            node = node.next
            if node is not None:
                val = node.val
                bisect.insort_left(keys, val)
                new_idx = bisect.bisect_left(keys, val)
                lists.insert(new_idx, node)
            
                
        return ret