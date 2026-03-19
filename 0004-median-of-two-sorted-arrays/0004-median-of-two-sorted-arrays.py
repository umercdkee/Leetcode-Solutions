class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        new_arr = []
        while i < len (nums1) and j < len (nums2):
            if nums1[i]<=nums2[j]:
                new_arr.append(nums1[i])
                i+=1
            else:
                new_arr.append(nums2[j])
                j+=1
        if i == len (nums1):
            new_arr += nums2[j:len(nums2)]
        else:
            new_arr += nums1[i:len(nums1)]
        new_len = len(nums1)+len(nums2)
        if new_len%2==1:
            return new_arr[new_len//2]
        else:
            return (new_arr[int(new_len/2)]+new_arr[int((new_len/2)-1)])/2