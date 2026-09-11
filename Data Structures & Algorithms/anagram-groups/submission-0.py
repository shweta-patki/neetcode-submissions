class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = dict()
        for i in strs:
            x = ''.join(sorted(list(i)))
            if x in grps:
                grps[x].append(i)
            else:
                grps[x] = [i]
            
        r = list(grps.values())
        return r