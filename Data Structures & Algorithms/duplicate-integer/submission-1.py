class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        appear = False
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
               appear = True
               break
        return appear         



class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False