# Sorting Algorithms Performance Analysis

This project implements and analyzes the performance of four popular sorting algorithms: **Bubble Sort**, **Cocktail Shaker Sort**, **Merge Sort**, and **Radix Sort**. The algorithms are evaluated using various performance tests, including **power tests**, **ratio tests**, and **constant tests**, to assess their efficiency with different input sizes and characteristics.

## Algorithms Implemented
- **Bubble Sort**: A simple comparison-based algorithm with time complexity of \( \Theta(n^2) \).
- **Cocktail Shaker Sort**: A bidirectional variation of bubble sort, also with \( \Theta(n^2) \) time complexity.
- **Merge Sort**: A divide-and-conquer algorithm with a more efficient \( \Theta(n \log n) \) time complexity.
- **Radix Sort**: A non-comparative algorithm with linear time complexity, \( \Theta(nk) \), where \( k \) is the number of digits.

## Features
- **Empirical Analysis**: Includes performance tests for different sorting algorithms.
  - **Power Test**: Assesses the relationship between the size of the input and the time taken to sort.
  - **Ratio Test**: Evaluates how the execution time compares to theoretical models.
  - **Constant Test**: Examines the constant factors in sorting time complexity.
- Visualizations of the results to analyze and compare the algorithms’ performances.

## Installation

To install the necessary dependencies, use:

```bash
pip install -r requirements.txt
