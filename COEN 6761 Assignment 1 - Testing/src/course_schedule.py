# src/course_schedule.py

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
