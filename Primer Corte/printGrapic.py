import numpy as np
from matplotlib import pyplot as plt

class PrintGrapic:
    # Constructor Application
    def __init__(self) -> None:
        pass
    # Method Print Grapics
    def printGrapic(self):
        ys = 200 + np.random.randn(100)
        x = [x for x in range(len(ys))]

        plt.plot(x, ys, '-')
        plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

        plt.title("Sample Visualization")
        plt.show()
        pass

