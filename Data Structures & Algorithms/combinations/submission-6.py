class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i):
            
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(i, n+1):
              comb.append(i)
              backtrack(i + 1)
              comb.pop()
            

        backtrack(1)
        return res