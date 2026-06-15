class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        TeamS = {}
        TeamT = {}    
        for i in range(len(s)):
            TeamS[s[i]] = TeamS.get(s[i], 0) + 1
            TeamT[t[i]] = TeamT.get(t[i], 0) + 1

        
        return TeamS == TeamT    

         

      
         
            




        