class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = collections.defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            hm[key].append(s)

        return list(hm.values())
        