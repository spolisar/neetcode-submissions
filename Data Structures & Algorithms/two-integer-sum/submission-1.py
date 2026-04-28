class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevs:
                return [prevs[diff], i]
            prevs[nums[i]] = i
        return [-1, -1]