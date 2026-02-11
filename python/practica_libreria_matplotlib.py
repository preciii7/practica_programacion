# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "matplotlib>=3.10.8",
# ]
# ///

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()  