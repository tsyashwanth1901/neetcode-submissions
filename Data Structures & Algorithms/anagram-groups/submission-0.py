class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            j = ''.join(sorted(i))
            if j in anagrams.keys():
                anagrams[j].append(i)
            else:
                anagrams[j] = [i]
        return list(anagrams.values())