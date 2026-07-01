class Solution:
    def findOrder(self, numCourse: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourse 
        adjacency_list = [[] for _ in range(numCourse)]
    
        for course, prereq in prerequisites:
            in_degree[course] += 1
            adjacency_list[prereq].append(course)
    
        q = deque()
    
        for i in range(numCourse):
            if in_degree[i] == 0:
                q.append(i)
    
        courses_order = []

        while q:
            course = q.popleft()
            courses_order.append(course)

            for node in adjacency_list[course]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)

    
        if len(courses_order) != numCourse:
            return []
    
        return courses_order