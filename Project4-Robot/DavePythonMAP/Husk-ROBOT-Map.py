import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button
import numpy as np
import os

# Change the working directory to the directory where the script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to calculate distance
def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Load your image
img = mpimg.imread('Husk-ROBOT_Map.png')  # Replace with your image path

# Plot the image
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, img.shape[1], img.shape[0], 0])

# This list will hold the points
points = []

def onclick(event):
    # If the click is outside the axes, ignore it
    if event.inaxes != ax:
        return

    # Add the point to the list
    points.append((event.xdata, event.ydata))

    # Plot the point
    ax.plot(event.xdata, event.ydata, 'ro')

    # Draw lines between the points
    if len(points) > 1:
        x_values, y_values = zip(*points)
        ax.plot(x_values, y_values, 'r-')

    # Calculate the total distance
    if len(points) > 1:
        total_distance = sum(calculate_distance(x_values[i], y_values[i], x_values[i+1], y_values[i+1])
                             for i in range(len(points) - 1))
        print(f"Total Distance: {total_distance:.2f}")

    plt.draw()

def reset(event):
    global points
    points = []
    ax.clear()
    ax.imshow(img, extent=[0, img.shape[1], img.shape[0], 0])
    plt.draw()

def save(event):
    fig.savefig('plotted_image.png')  # Replace with your desired path

# Connect the event to the onclick function
fig.canvas.mpl_connect('button_press_event', onclick)

# Create a button for resetting the plot
ax_reset = plt.axes([0.7, 0.05, 0.1, 0.075])
btn_reset = Button(ax_reset, 'Reset')
btn_reset.on_clicked(reset)

# Create a button for saving the plot
ax_save = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_save = Button(ax_save, 'Save')
btn_save.on_clicked(save)

plt.show()
