class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            chars_counter = [0] * 26
            for c in s:
                chars_counter[ord(c) - ord('a')] += 1
            res[tuple(chars_counter)].append(s)
        return list(res.values())