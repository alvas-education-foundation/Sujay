"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            
            if target == nums[i]:
                return i
            
            if target < nums[i]:
                nums.insert(i,target)
                return i
        
        return i+1