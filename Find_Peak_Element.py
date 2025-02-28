class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = []
        postfix = []

        for i in range(0, len(nums)):
            prefix.append("F")
            postfix.append("F")
        prefix[0] = "T"
        postfix[len(nums)-1] = "T"
        for i in range(1, len(nums)):
            prefix[i] = "F"
            if nums[i] > nums[i-1]:
                prefix[i] = "T"
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = "F"
            if nums[i] > nums[i+1]:
                postfix[i] = "T"
        key = -1
        for i in range(0, len(nums)):
            if prefix[i] == postfix[i]:
                key = i
        
        return key