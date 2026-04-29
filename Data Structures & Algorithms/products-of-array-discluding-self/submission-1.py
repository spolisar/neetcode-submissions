class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefixes = [1] * length
        suffixes = [1] * length

        # switch to more readable version
        # for i in range(len(nums)-1):
        #     prefixes[i+1] = nums[i] * prefixes[i]
        #     suffixes[length -2 - i] = suffixes[length - 1 - i] * nums[length - 1 - i]
        for i in range(1, length):
            prefixes[i] = nums[i-1] * prefixes[i-1]
        for i in range(length-2, -1, -1):
            suffixes[i] = nums[i+1] * suffixes[i+1]
        return [prefixes[i] * suffixes[i] for i in range(len(nums))]
        