class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for i in range(len(prices)): 
          for j in range( i+1, len(prices)):
            if prices[j] - prices[i] > diff:
                diff = prices[j] - prices[i]
        return diff   


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      l = 0
      r = 1
      maxi = 0
      while r < len(prices):
          if prices[l] < prices[r]:
              maxi = max(prices[r] - prices[l], maxi)
          else:
            l = r
             
          r += 1

      return maxi



      
