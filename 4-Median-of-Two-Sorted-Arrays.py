class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i = 0
        j = 0
        while True:
            if i == len(nums1):
                nums3 += nums2[j:]
                break
            if j == len(nums2):
                nums3 += nums1[i:]
                break
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        ret = 0
        if len(nums3) % 2 == 0:
            ret = (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2
        else:
            ret =  nums3[len(nums3) // 2]
        return ret