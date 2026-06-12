class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        for p in points:
            distance = math.sqrt((0 - p[0]) ** 2 + (0 - p[1]) ** 2)
            heapq.heappush(min_heap, (distance, [p[0], p[1]]))

        closest_points = []
        for i in range(k):
            closest_points.append(heapq.heappop(min_heap)[1])
        
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



        