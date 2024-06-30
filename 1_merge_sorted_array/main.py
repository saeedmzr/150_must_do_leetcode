class Solution(object):
    def merge(self, nums1: list, m: int, nums2: list, n: int):
        output1 = []
        output2 = []
        for i in range(min(len(nums1), m)):
            output1.append(nums1[i])

        for i in range(min(len(nums2), n)):
            output2.append(nums2[i])

        final = output1 + output2
        final.sort()
        return final


a = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
out = a.merge(nums1, m, nums2, n)
print(out)
