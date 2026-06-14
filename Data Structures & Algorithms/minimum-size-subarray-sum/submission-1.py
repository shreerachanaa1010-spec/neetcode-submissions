class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        min_leng = float("inf")
        current_sum = 0
        for j in range(len(nums)):
            current_sum += nums[j]
            while current_sum >= target:
                min_leng = min(min_leng, j-i+1)
                current_sum -= nums[i]
                i += 1
            
        return 0 if min_leng == float("inf") else min_leng       
        