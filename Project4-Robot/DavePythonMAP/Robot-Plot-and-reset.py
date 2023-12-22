import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

# Change the working directory to the directory where the script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to calculate distance
def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Load an image
img = mpimg.imread('Husk-ROBOT_Map.png')  # Make sure to provide the correct path to your image

# Plot the image
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, img.shape[1], img.shape[0], 0])
points = []

# Event handler for mouse clicks
def onclick(event):
    if event.inaxes == ax:
        x, y = event.xdata, event.ydata
        points.append((x, y))
        ax.plot(x, y, 'ro')

        if len(points) > 1:
            x_values, y_values = zip(*points)
            ax.plot(x_values, y_values, 'r-')

            # Calculate the total distance
            total_distance = sum(calculate_distance(x_values[i], y_values[i], x_values[i+1], y_values[i+1])
                                 for i in range(len(points) - 1))
            print(f"Total Distance: {total_distance:.2f}")

        plt.draw()

# Reset the plot to its initial state
def reset(event):
    global points
    points = []
    ax.clear()
    ax.imshow(img, extent=[0, img.shape[1], img.shape[0], 0])
    plt.draw()

# Connect the onclick event
fig.canvas.mpl_connect('button_press_event', onclick)

# Add a button to reset the plot
button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])
button = plt.Button(button_ax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')

# Connect the reset event
button.on_clicked(reset)

plt.show()
