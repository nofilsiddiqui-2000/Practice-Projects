# import unittest
# import csv
# from src.course_schedule import findOrder

# class TestCourseSchedule(unittest.TestCase):
#     """Unit test class for Course Schedule II problem."""
    
#     def test_cases_from_csv(self):              # Test 01
#         """Reads test cases from CSV and runs parameterized tests."""
#         with open('data/test_cases.csv', newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             next(reader)  # Skip header row
#             for row in reader:
#                 numCourses = int(row[0])
#                 prerequisites = eval(row[1])  # Convert string to list
#                 expected_output = eval(row[2])  # Convert string to list
#                 self.assertEqual(findOrder(numCourses, prerequisites), expected_output)
    
#     def test_cycle(self):           # Test 02
#         """Test case with a cycle - should return an empty list."""
#         self.assertEqual(findOrder(2, [[0, 1], [1, 0]]), [])  # Cyclic dependency

#     def test_single_course(self):           # Test 03
#         """Test case with only one course and no prerequisites."""
#         self.assertEqual(findOrder(1, []), [0])  # Only one course

#     def test_no_prerequisites(self):            # Test 04
#         """Test case where there are multiple courses but no prerequisites."""
#         numCourses = 3
#         result = findOrder(numCourses, [])
#         self.assertEqual(sorted(result), [0, 1, 2])  # Any order is valid

#     def test_multiple_valid_paths(self):            # Test 05
#         """Test case with multiple valid outputs."""
#         result = findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
#         valid_outputs = [[0, 1, 2, 3], [0, 2, 1, 3]]  # Both are valid
#         self.assertIn(result, valid_outputs)  # Check if the output is one of the valid ones

# if __name__ == '__main__':
#     unittest.main()  # pragma: no cover


## After cyclomatic complexity:

import unittest
import csv
from src.course_schedule import findOrder

class TestCourseSchedule(unittest.TestCase):
    """Unit test class for Course Schedule II problem."""
    
    def test_cases_from_csv(self):              # Test 01
        """Reads test cases from CSV and runs parameterized tests."""
        with open('data/test_cases.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                numCourses = int(row[0])
                prerequisites = eval(row[1])  # Convert string to list
                expected_output = eval(row[2])  # Convert string to list
                self.assertEqual(findOrder(numCourses, prerequisites), expected_output)

    def test_cycle(self):           # Test 02
        """Test case with a cycle - should return an empty list."""
        self.assertEqual(findOrder(2, [[0, 1], [1, 0]]), [])  # Cyclic dependency

    def test_single_course(self):           # Test 03
        """Test case with only one course and no prerequisites."""
        self.assertEqual(findOrder(1, []), [0])  # Only one course

    def test_no_prerequisites(self):            # Test 04
        """Test case where there are multiple courses but no prerequisites."""
        numCourses = 3
        result = findOrder(numCourses, [])
        self.assertEqual(sorted(result), [0, 1, 2])  # Any order is valid

    def test_multiple_valid_paths(self):            # Test 05
        """Test case with multiple valid outputs."""
        result = findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        valid_outputs = [[0, 1, 2, 3], [0, 2, 1, 3]]  # Both are valid
        self.assertIn(result, valid_outputs)  # Check if the output is one of the valid ones

    def test_single_dependency_chain(self):  # Test 06
        """Test case where each course depends on the previous one (linear chain)."""
        result = findOrder(3, [[1, 0], [2, 1]])
        self.assertEqual(result, [0, 1, 2])  # Single valid path

    def test_large_input(self):  # Test 07
        """Performance test with a large number of courses."""
        numCourses = 1000
        prerequisites = [[i, i - 1] for i in range(1, numCourses)]
        expected_output = list(range(numCourses))
        self.assertEqual(findOrder(numCourses, prerequisites), expected_output)

    def test_random_order_prerequisites(self):  # Test 08
        """Test case where prerequisites are given in random order."""
        result = findOrder(4, [[3, 1], [1, 0], [3, 2], [2, 0]])
        valid_outputs = [[0, 1, 2, 3], [0, 2, 1, 3]]  # Both are valid
        self.assertIn(result, valid_outputs)

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
