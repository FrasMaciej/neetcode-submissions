class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = defaultdict(int)
        for n in nums:
            dct[n] += 1
        # return list(dict(sorted(dct.items(), key = lambda x: x[1], reverse = True)).keys())[:k]
        return sorted(dct, key=dct.get, reverse=True)[:k]

        