class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefixes = [1] * length
        suffixes = [1] * length


        for i in range(len(nums)-1):
            prefixes[i+1] = nums[i] * prefixes[i]
            suffixes[length -2 - i] = suffixes[length - 1 - i] * nums[length - 1 - i]
        
        return [prefixes[i] * suffixes[i] for i in range(len(nums))]
        