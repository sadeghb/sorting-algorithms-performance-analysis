def is_valid_solution(original: list[int], solution: list[int]) -> bool:
    """
    Validates if the solution is sorted and has the same elements as the original list.

    Args:
        original (list[int]): The original list before sorting.
        solution (list[int]): The list after applying the sorting algorithm.

    Returns:
        bool: True if the solution is valid, False otherwise.
    """
    # Check if the solution is sorted
    if solution != sorted(solution):
        return False

    # Check if the solution contains the same elements as the original list
    if sorted(original) != sorted(solution):
        return False

    return True
