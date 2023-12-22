# Interactive Image Measurement Tool

This tool allows users to interactively measure distances within an image using a Python script that utilizes the Matplotlib library. The script provides a visual interface for selecting points on the image, and it calculates and displays the total distance between the selected points.

## Features

- **Image Display**: The script loads and displays an image within a Matplotlib plot.
- **Point Selection**: Users can click on the image to select points. Each point is marked with a red dot.
- **Distance Calculation**: The script calculates the Euclidean distance between consecutive points and displays the total distance.
- **Interactive Cursor**: A red cursor follows the mouse position for precise point selection.

## Usage

1. **Load Image**: Replace `'image.png'` with the path to your image file.
2. **Run Script**: Execute the script to open the interactive Matplotlib window.
3. **Select Points**: Click on the image to select points. The script will automatically calculate and print the total distance.
4. **Close Window**: Close the Matplotlib window to end the session.

## Requirements

- Python 3.x
- Matplotlib (`pip install matplotlib`)
- NumPy (`pip install numpy`)

## Example Code

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Cursor
import numpy as np

# Function to calculate distance
def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Load your image
img = mpimg.imread('image.png')  # Replace with your image path

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

# Connect the event to the onclick function
fig.canvas.mpl_connect('button_press_event', onclick)

# Add a cursor
cursor = Cursor(ax, useblit=True, color='red', linewidth=1)

plt.show()
```

## Notes

- Ensure the image file path is correct before running the script.
- The script prints the total distance in the console. Keep the console open to view the output.
- The distance is calculated in the image's pixel space, not in real-world units.

___

> Created by Dave Husk <dave.husk@keyin.com>