class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        
        pre = 1
        for i in range(length):
            result[i] *= pre
            pre *= nums[i]
        suff = 1
        for i in range(length-1, 0, -1):
            suff *= nums[i]
            result[i-1] *= suff
        return result
        