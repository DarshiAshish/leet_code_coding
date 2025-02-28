class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        min_index = min(len(nums1), len(nums2))
        res_array = []
        i=0
        j=0
        while i < len(nums1) and j < len(nums2): 
            if nums1[i] < nums2[j]:
                res_array.append(nums1[i])
                i=i+1
            else:
                res_array.append(nums2[j])
                j=j+1
        print(res_array)
        while i < len(nums1):
            res_array.append(nums1[i])
            i=i+1
        while j < len(nums2):
            res_array.append(nums2[j])
            j=j+1
        print(res_array)
        fin_len = len(res_array)
        if fin_len%2 == 0:
            mid = fin_len // 2
            print(mid)
            ans = (float(res_array[mid - 1]) + float(res_array[mid])) / 2
            print(ans)
            return ans
        else:
            mid = int(fin_len/2)
            return res_array[mid]