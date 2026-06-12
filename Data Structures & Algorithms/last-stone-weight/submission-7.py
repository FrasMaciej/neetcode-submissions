class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_negated = [-s for s in stones]
        heapq.heapify(stones_negated)

        while len(stones_negated) > 1:
            first_stone, second_stone = -heapq.heappop(stones_negated), -heapq.heappop(stones_negated)

            if first_stone > second_stone:
                new_stone = first_stone - second_stone
                heapq.heappush(stones_negated, -new_stone)
        
        return -stones_negated[0] if stones_negated else 0