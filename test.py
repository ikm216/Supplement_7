import numpy as np
import matplotlib.pyplot as plt

def plot_200():
    """
    Plots 200 points from a standard normal distribution.

    This function generates 200 random points from a standard normal distribution
    (mean = 0, standard deviation = 1) and plots them as a scatter plot. The x-axis
    represents the index of the points (from 0 to 199), and the y-axis represents
    the values of the sampled points.

    Returns:
        Display the plots on a grid
    """
    points = np.random.normal(0, 1, 200) #np.random.normal: generates random numbers from a normal distrubution
    plt.scatter(range(200), points)
    plt.title("Plots")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

def plot_line(y_intercept, slope, low_x, up_x):
    x = np.linspace(low_x, up_x, 500)
    y = slope * x + y_intercept

    plt.plot(x, y)
    plt.xlim(low_x, up_x)
    plt.title("Plot Line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

def test_should_return_200_plots():
    points = np.random.normal(0, 1, 200)
    assert len(points) == 200
    # np.isclose: checks if the numbers are equal
    assert np.isclose(np.mean(points), 0, atol = 0.5)
    assert np.isclose(np.std(points), 1, atol = 0.5)

    plot_200()

def test_should_return_plot_line():
    y_intercept = 5
    slope = 2
    low_x = -7
    up_x = 7

    x = np.linspace(low_x, up_x, 5)
    y = slope * x + y_intercept

    plot_graph = [slope * xi + y_intercept for xi in x]
    assert np.allclose(y, plot_graph)

    plot_line(y_intercept, slope, low_x, up_x)

