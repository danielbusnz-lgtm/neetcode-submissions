class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        seen = {}
        for i , num in enumerate(nums):
            equivalent = target - num
            if equivalent in seen:
                return [seen[equivalent], i]
            seen[num] = i