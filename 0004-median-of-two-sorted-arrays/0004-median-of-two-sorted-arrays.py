class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        
        nums1=sorted(nums1)
        if len(nums1)%2==0:
            midIndx=int(len(nums1)/2)
            return (nums1[midIndx]+nums1[midIndx-1])/2
        else:
            midIndx=int(len(nums1)//2)
            return nums1[midIndx]