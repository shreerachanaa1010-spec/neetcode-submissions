class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addsum = {}
        for i,num in enumerate(nums):
               diff = target - num
               if diff in addsum:
                   return[addsum[diff], i]
               addsum[num] = i  

        