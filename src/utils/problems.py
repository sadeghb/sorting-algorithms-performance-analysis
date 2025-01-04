import random
from collections.abc import Iterable

class Problem:
    def __init__(self, size: int, max_number: int, num_samples: int = 5) -> None:
        self.size = size
        self.max_number = max_number
        self.num_samples = num_samples

    def generate_sample(self) -> list[int]:
        """Returns a list of the given size containing numbers between 1 and the max_number."""
        return [random.randint(1, self.max_number) for _ in range(self.size)]

    def generate_dataset(self) -> Iterable[list[int]]:
        """Returns an iterator over as many samples as are described."""
        return (self.generate_sample() for _ in range(self.num_samples))


def create_problems(sizes: list[int], max_numbers: list[int], num_samples: int = 5) -> list[Problem]:
    """Creates problem instances using given sizes and max_numbers."""
    problems = []
    for size in sizes:
        for max_number in max_numbers:
            problems.append(Problem(size, max_number, num_samples))
    return problems
