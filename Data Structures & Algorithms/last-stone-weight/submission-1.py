class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_negated = [-n for n in stones]
        heapq.heapify(stones_negated)

        while len(stones_negated) > 1:
            top_stones = (-heapq.heappop(stones_negated), -heapq.heappop(stones_negated))
            if top_stones[0] == top_stones[1]:
                continue
            else:
                new_stone = top_stones[0] - top_stones[1]
                heapq.heappush(stones_negated, -new_stone)
        
        if not stones_negated:
            return 0
        else:
            return -stones_negated[0]