import matplotlib.pyplot as plt
from scipy.stats import linregress
from .measure import Measure


def plot_threshold_estimation(data1: dict[int, int], data2: dict[int, int], label1: str, label2: str, ylabel: str):
    """Plots threshold estimation for two data sets."""
    plt.plot(list(data1.keys()), list(data1.values()), label=label1)
    plt.plot(list(data2.keys()), list(data2.values()), label=label2)
    plt.xlabel("Threshold")
    plt.ylabel(ylabel)
    plt.title("Threshold Estimation")
    plt.legend()
    plt.show()


def plot_threshold_measures(data: dict[int, int]):
    """Plots the time taken for various thresholds."""
    x = list(data.keys())
    y = list(data.values())
    plt.plot(x, y, label="Measurements")
    plt.scatter(x, y, label="Measurements")
    plt.xlabel("Threshold")
    plt.ylabel("Time (ms)")
    plt.title("Threshold Selection")
    plt.legend()
    plt.show()


def display_table(measures: list[Measure]):
    """Displays a table of measurements."""
    print("{: <12} {: <12} {: <12}".format("Size", "Max Number", "Mean Time (ms)"))
    for measure in measures:
        print("{: <12} {: <12} {: <12}".format(measure.size, measure.max_number, measure.mean))


def plot_power_test(data: dict[int, int], xlabel: str, ylabel: str, title: str = "Power Test"):
    """Takes the data and displays it into the corresponding test graph.
    It applies no transformations to the data.

    Args:
        data (dict[int,int]): A dictionnary mapping the x variable to the y variable
    """
    # Log both sets of values
    x = list(data.keys())
    y = list(data.values())

    # Perform the lin regression
    m, b, rvalue, _, _ = linregress(x, y)

    # Estimate the values of y based on the lin regression results
    predicted = [m * iter + b for iter in x]

    # Create the line equation
    line_eq = f"y = {m:.2f}x + {b:.2f}"

    # Plot the points
    plt.scatter(x, y, label='Mesures')

    # Plot the regression line
    plt.plot(x, predicted, color="red", label=f'Regression linéaire R²={round(rvalue**2,6)}')

    # Add labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # Add legend
    plt.legend(bbox_to_anchor=(0.60, 0), loc='lower left')

    # Display the line equation
    plt.text(min(x), max(y), line_eq)

    # Show the plot
    plt.show()


def plot_ratio_test(data: dict[int, int], xlabel: str, ylabel: str, title: str = "Ratio Test"):
    """Takes the data and displays it into the corresponding test graph.
    It applies no transformations to the data.

    Args:
        data (dict[int,int]): A dictionnary mapping the x variable to the y variable
    """
    x = list(data.keys())
    y = list(data.values())

    plt.plot(x, y, label='Mesures')
    plt.scatter(x, y, label='Mesures')

    # Add labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def plot_constant_test(data: dict[int, int], xlabel: str, ylabel: str = "Time (ms)", title: str = "Constant Test"):
    """Takes the data and displays it into the corresponding test graph.
    It applies no transformations to the data.

    Args:
        data (dict[int,int]): A dictionnary mapping the x variable to the y variable
    """
    x = list(data.keys())
    y = list(data.values())

    # Perform linear regression
    m, b, rvalue, _, _ = linregress(x, y)

    predicted = [m * iter + b for iter in x]

    # Create the line equation
    line_eq = f"y = {m:.2E}x + {b:.2E}"

    # Plot the points
    plt.scatter(x, y, label='Mesures')

    # Plot the regression line
    plt.plot(x, predicted, color="red", label=f'Regression linéaire R²={round(rvalue**2,6)}')

    # Add labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # Add legend
    plt.legend(bbox_to_anchor=(0.60, 0), loc='lower left')

    # Display the line equation
    plt.text(min(x), max(y), line_eq)

    # Show the plot
    plt.show()
