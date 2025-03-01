class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        count=0
        nums.sort() 
        while i<j:
            if nums[i] + nums[j] == k:
                count = count+1
                i=i+1
                j=j-1
            elif nums[i] + nums[j] < k:
                i=i+1
            else:
                j=j-1
        return count