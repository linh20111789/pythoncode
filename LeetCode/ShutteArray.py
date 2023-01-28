class Solution:
    def shuffle(self, nums, n):
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res


obj = Solution()
print(obj.shuffle([2,5,1,3,4,7],3))        