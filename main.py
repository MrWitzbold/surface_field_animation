import random
import shutil
import numpy as np
import matplotlib.cm as cm
import pystencils.plot as plt
from pystencils.session import *
import math

decreasing = False

def example_scalar_field(t=0):
    x, y = np.meshgrid(np.linspace(0, 2 * np.pi, 100), np.linspace(0, 2 * np.pi, 100))
    z = np.sin(x*t/50) + np.sin(y*t/50)
    print(t)
    return z

t = 0
def run_func():
    global decreasing
    global t
    if decreasing == False:
        t += 1
    else:
        t -= 1
    if t == 40:
        decreasing = True
    if t == 0 and decreasing == True:
        decreasing = False
    return example_scalar_field(t)

animation = plt.surface_plot_animation(run_func, frames=60, cm="plasma")
plt.show()
