import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import TextBox
import numpy as np
import os

# Change the working directory to the directory where the script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to calculate distance
def calculate_distance(points):
    distances = [np.sqrt((x2 - x1)**2 + (y2 - y1)**2) for (x1, y1), (x2, y2) in zip(points[:-1], points[1:])]
    return distances

# Initialize the plot
img_path = 'Husk-ROBOT_Map.png'  # For example: '/mnt/data/Husk-ROBOT_Map.png'
img = mpimg.imread(img_path)
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, img.shape[1], img.shape[0], 0])
plt.subplots_adjust(bottom=0.2)

# This list will hold the points and measurements
points = []

# Event handler for clicks
def onclick(event):
    # If the click is outside the axes, ignore it
    if event.inaxes != ax:
        return

    # Add the point to the list
    points.append((event.xdata, event.ydata))

    # Plot the point
    ax.plot(event.xdata, event.ydata, 'ro')

    # Draw lines between the points and display the manually inputted measurement
    if len(points) > 1:
        ax.plot(*zip(*points[-2:]), 'r-')
        dist = calculate_distance(points[-2:])
        ax.annotate(f"{dist[0]:.2f}", ((points[-1][0] + points[-2][0]) / 2, (points[-1][1] + points[-2][1]) / 2),
                    textcoords="offset points", xytext=(0,10), ha='center')

    plt.draw()

# TextBox for inputting measurements
def submit(text):
    print(f"Measurement entered: {text}")

axbox = plt.axes([0.1, 0.05, 0.2, 0.075])
text_box = TextBox(axbox, 'Enter measurement: ')
text_box.on_submit(submit)

# Connect the onclick event
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
