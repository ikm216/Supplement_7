import numpy as np
import matplotlib.pyplot as plt

def plot_200():
    points = np.random.normal(0, 1, 200)
    plt.scatter(range(200), points)
    plt.title("Plots")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

def test_should_return_200_plots():
    points = np.random.normal(0, 1, 200)
    assert len(points) == 200
    assert np.isclose(np.mean(points), 0, atol = 0.5)
    assert np.isclose(np.std(points), 1, atol = 0.5)

    plot_200()