class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l={}
        for i in nums:
            if i not in l.keys():
                l[i] = 1
            else:
                return True
        return False