import time
from .is_valid_solution import is_valid_solution
from .problems import Problem


class InvalidSolution(Exception):
    def __init__(self):
        super().__init__("Invalid solution, verify your code.")


class Measure:
    """A wrapper to contain information on taken measures."""
    def __init__(self, size: int, max_number: int, mean: int) -> None:
        self.size = size
        self.max_number = max_number
        self.mean = mean


def measure(procedure, sample: list[int], time_scale: int = 1000) -> int:
    """Returns the time in milliseconds taken to run the procedure."""
    start = time.time() * time_scale
    solution = procedure(sample)
    end = time.time() * time_scale
    if not is_valid_solution(sample, solution):
        raise InvalidSolution()
    return round(end - start)


def measure_mean(procedure, prob: Problem, time_scale: int = 1000) -> Measure:
    """Generates multiple samples and returns the mean time in milliseconds."""
    mean_time = sum(
        [measure(procedure, sample, time_scale) for sample in prob.generate_dataset()]
    ) / prob.num_samples
    return Measure(prob.size, prob.max_number, mean_time)


def measure_range(procedure, problems: list[Problem], time_scale: int = 1000) -> list[Measure]:
    """Measures the mean time taken for a range of problems."""
    return [measure_mean(procedure, prob, time_scale) for prob in problems]
