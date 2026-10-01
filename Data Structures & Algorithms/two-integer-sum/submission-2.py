class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dit = {}
        for i in range(0,len(nums)):
            diff = target-nums[i]
            if diff in dit.keys():
                return [dit[diff],i]
            else:
                dit[nums[i]] = i