# Course Schedule II - Python Implementation

## Description
This project provides a solution to LeetCode's [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) problem using a **topological sort** approach. The algorithm determines a valid order to complete a set of courses given their prerequisite structure.

## Project Structure
```
.
├── .coverage                # Coverage report file (generated after tests)
├── data
│   └── test_cases.csv       # Contains test cases for the Course Schedule II problem in CSV format
├── main.py                  # Main entry point for the project (currently empty)
├── README.md                # Project documentation
├── requirements.txt         # Lists the dependencies required for the project
├── run_tests.sh             # Shell script to run unit tests and generate code coverage report
├── src
│   └── course_schedule.py   # Contains the implementation of the Course Schedule II solution
├── tests
│   └── test_course_schedule.py  # Unit tests for the Course Schedule II solution
└── __pycache__              # Compiled bytecode files (typically ignored in version control)
```

## Files
- **`main.py`**: Main entry point for the project (currently empty).
- **`requirements.txt`**: Lists the dependencies required for the project.
- **`run_tests.sh`**: Shell script to run unit tests and generate a code coverage report.
- **`data/test_cases.csv`**: Contains test cases for the Course Schedule II problem in CSV format.
- **`src/course_schedule.py`**: Contains the implementation of the Course Schedule II solution.
- **`tests/test_course_schedule.py`**: Unit tests for the Course Schedule II solution.

## How to Run
1. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Tests and Generate Coverage**  
   ```bash
   ./run_tests.sh
   ```
   - This script runs the unit tests with coverage reporting.

## Solution Explanation
The solution uses a **topological sort** (Kahn's algorithm) to determine a valid sequence in which courses can be taken. Key steps:
1. Build a directed graph where each node represents a course, and edges represent prerequisites.
2. Identify courses with no prerequisites (in-degree = 0).
3. Repeatedly add those courses to the result list and reduce the in-degree of their dependent courses.
4. If any courses remain with non-zero in-degree and cannot be processed, it means there is a cycle, and no valid ordering exists.

## Unit Tests
The unit tests are located in [`tests/test_course_schedule.py`](./tests/test_course_schedule.py) and include:
- **`test_cases_from_csv`**: Reads test cases from the CSV file and runs parameterized tests.
- **`test_cycle`**: Validates behavior when there is a cycle (expected to return an empty list).
- **`test_single_course`**: Tests the scenario with a single course and no prerequisites.
- **`test_no_prerequisites`**: Tests when multiple courses have no prerequisites.
- **`test_multiple_valid_paths`**: Tests scenarios where multiple valid topological sorts exist.

---

