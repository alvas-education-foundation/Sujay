"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsofar = nums[0]
        currentmax = nums[0]

        for i in range(1, len(nums)):
            currentmax = max(nums[i], currentmax + nums[i])
            maxsofar = max(maxsofar, currentmax)

        return maxsofar