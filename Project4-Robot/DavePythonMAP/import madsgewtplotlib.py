import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import TextBox
import numpy as np
import os
from tkinter import Tk, filedialog

# Function to calculate distance
def calculate_distance(points):
    return np.sqrt(np.sum((np.array(points[-1]) - np.array(points[-2]))**2))

# Load the image provided by the user
def load_image():
    root = Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(title="Select Image File")
    img = mpimg.imread(filename)
    return img

# Initialize the plot
img = load_image()
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, img.shape[1], img.shape[0], 0])
plt.subplots_adjust(bottom=0.2)

# This list will hold the points and their measurements
points = []

# Event handler for clicks
def onclick(event):
    # If the click is outside the axes, ignore it
    if event.inaxes != ax:
        return

    # Add the point to the list with its measurement
    measurement = float(text_box.text)
    points.append(((event.xdata, event.ydata), measurement))

    # Plot the point
    ax.plot(event.xdata, event.ydata, 'ro')

    # Draw lines between the points and annotate with measurements
    if len(points) > 1:
        x_values, y_values = zip(*[p[0] for p in points])
        ax.plot(x_values, y_values, 'r-')

        # Annotate line with measurement
        mid_point = ((x_values[-2] + x_values[-1]) / 2, (y_values[-2] + y_values[-1]) / 2)
        ax.annotate(f"{measurement}", mid_point, textcoords="offset points", xytext=(0,10), ha='center')

    plt.draw()

# Event handler for submit
def submit(text):
    print(f"Current measurement: {text}")

# Create a TextBox for measurements input
ax_box = plt.axes([0.1, 0.05, 0.2, 0.075])
text_box = TextBox(ax_box, 'Measurement: ', initial="0.00")
text_box.on_submit(submit)

# Connect the event to the onclick function
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
