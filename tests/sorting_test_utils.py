import random
from src.utils.is_valid_solution import is_valid_solution

def get_shared_test_cases():
    """
    Returns a list of shared test cases for sorting algorithms.

    Each test case is a tuple of the form:
    (input_list, expected_output_list, description)
    """
    # Static test cases
    static_cases = [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "Already sorted"),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], "Reversed order"),
        ([2, 2, 2, 2], [2, 2, 2, 2], "All identical elements"),
        ([], [], "Empty list"),
        ([5], [5], "Single element"),
        ([3, 1, 2, 3, 1], [1, 1, 2, 3, 3], "Unsorted with duplicates"),
        ([-1, 2, 0, -2, 1], [-2, -1, 0, 1, 2], "Negative numbers"),
        ([30000000, 200, 10000000], [200, 10000000, 30000000], "Large numbers"),
        (list(range(5000, 0, -1)), list(range(1, 5001)), "Long reversed list"),
    ]

    # Randomized test cases
    random_cases = [
        (lst := random.sample(range(1, 2**31), 10), sorted(lst), "Random list of 10 elements"),
        (lst := random.sample(range(1, 2**31), 100), sorted(lst), "Random list of 100 elements"),
        (lst := random.sample(range(1, 2**31), 1000), sorted(lst), "Random list of 1000 elements"),
    ]

    return static_cases + random_cases


def run_sorting_algorithm_tests(algorithm, algorithm_name=None, test_cases=None):
    """
    Runs unit tests for a given sorting algorithm.

    Args:
        algorithm (function): The sorting function to test.
        algorithm_name (str): The name of the sorting algorithm (for reporting).
        test_cases (list): A list of test cases (optional, defaults to shared test cases).

    Raises:
        AssertionError: If a test case fails.
    """
    if not test_cases:
        test_cases = get_shared_test_cases()

    if not algorithm_name:
        algorithm_name = algorithm.__name__

    print(f"\nRunning tests for {algorithm_name}...")

    for i, (original, expected, description) in enumerate(test_cases):
        sorted_result = algorithm(original)
        assert is_valid_solution(original, sorted_result), f"Test {i+1} ({description}): Invalid solution"
        assert sorted_result == expected, f"Test {i+1} ({description}): Expected {expected}, got {sorted_result}"

    print(f"All tests passed for {algorithm_name}!")
