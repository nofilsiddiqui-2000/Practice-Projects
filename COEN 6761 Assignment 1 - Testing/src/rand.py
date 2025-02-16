# Import the function
from collections import deque
from typing import List

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """Finds the order of courses to be taken using topological sorting."""
    graph = {i: [] for i in range(numCourses)}
    in_degree = {i: 0 for i in range(numCourses)}
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
    course_order = []
    
    while queue:
        course = queue.popleft()
        course_order.append(course)
        
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return course_order if len(course_order) == numCourses else []

# Test cases
test_cases = [
    (2, [[1, 0]]),  # Expected output: [0, 1]
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),  # Expected output: [0, 1, 2, 3] or [0, 2, 1, 3]
    (3, [[0, 1], [1, 2], [2, 0]]),  # Expected output: [] (cycle detected)
    (1, []),  # Expected output: [0]
]

# Running the tests
for i, (numCourses, prerequisites) in enumerate(test_cases):
    print(f"Test {i+1}: numCourses={numCourses}, prerequisites={prerequisites}")
    print("Output:", findOrder(numCourses, prerequisites))
    print("-" * 50)
