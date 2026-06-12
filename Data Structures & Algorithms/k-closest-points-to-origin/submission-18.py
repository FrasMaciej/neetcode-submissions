class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            distance = (0 - x) ** 2 + (0 - y) ** 2
            if len(max_heap) == k and distance < -max_heap[0][0]:
                heapq.heapreplace(max_heap, (-distance, [x, y]))
            elif len(max_heap) < k:
                heapq.heappush(max_heap, (-distance, [x, y]))

        closest_points = []
        for p in max_heap:
            closest_points.append(p[1])
        
        return closest_points

        # Notes:

        # points[n][0] -- x
        # points[n][1] -- y

        # for two points Euclidean distance is defined as:
        # sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        # brute force: 1. calculate all distances and add to list, 2. sort distances, 3. return k points
        
        # better: store k of the closest points in max heap
        # when smaller than the max of the heap found then use replace it on heap

        # method should return points coords, but heap is storing distances. 
        # Need to use tuple to handle that



        