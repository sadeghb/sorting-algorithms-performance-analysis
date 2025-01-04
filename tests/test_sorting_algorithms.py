from src.algorithms import bubble_sort, cocktail_shaker_sort, merge_sort, radix_sort, merge_sort_threshold
from .sorting_test_utils import run_sorting_algorithm_tests

def test_bubble_sort():
    """
    Tests the Bubble Sort algorithm using shared test cases.
    """
    run_sorting_algorithm_tests(bubble_sort, "Bubble Sort")

def test_cocktail_shaker_sort():
    """
    Tests the Cocktail Shaker Sort algorithm using shared test cases.
    """
    run_sorting_algorithm_tests(cocktail_shaker_sort, "Cocktail Sort")

def test_merge_sort():
    """
    Tests the Merge Sort algorithm using shared test cases.
    """
    run_sorting_algorithm_tests(merge_sort, "Merge Sort")

# def test_merge_sort_threshold():
#     """
#     Tests the Merge Sort Threshold algorithm using shared test cases.
#     """
#     run_sorting_algorithm_tests(merge_sort_threshold, "Merge Sort Threshold")

def test_radix_sort():
    """
    Tests the Radix Sort algorithm using shared test cases.
    """
    run_sorting_algorithm_tests(radix_sort, "Radix Sort")
