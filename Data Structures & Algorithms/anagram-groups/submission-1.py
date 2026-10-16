class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        isanagram = defaultdict(list)
        for i in strs:
            isanagram[''.join(sorted(i))].append(i)
        return list(isanagram.values())    
           