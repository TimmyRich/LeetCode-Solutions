class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = 0
        notactuallythemedian = 0
        m, n = len(nums1), len(nums2)
        length = m + n
        if length % 2:
            k = length // 2 + 1 # kth smallest element is median
        else:
            k = length // 2 # mean of kth and kth + 1 element is "median"
            notactuallythemedian = 1

        # Merge the arrays up to k + 1 elements
        merged = []
        i, j = 0, 0
        for _ in range(k + 1):
            if i < m and (j >= n or nums1[i] < nums2[j]):
                merged.append(nums1[i])
                i += 1
            elif j < n:
                merged.append(nums2[j])
                j += 1

        if len(merged) == 1:
            return merged[0]
        if notactuallythemedian:
            return (merged[-1] + merged[-2])/2
        else:
            return merged[-2]
        





sol = Solution()
a1 = [1,2]
a2 = [3,4]
print(sol.findMedianSortedArrays(a1, a2))