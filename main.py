import json
import matplotlib.pyplot as plt
import mplcursors

# Path to the JSON file
file_path = 'radio_map.json'
# file_path = 'filtered_radio_map.json'

# Reading the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extracting coordinates
x_coords = [item["INSTANCE"]["mCenter"]["x"] for item in data]
y_coords = [item["INSTANCE"]["mCenter"]["y"] for item in data]

# Creating a scatter plot
fig, ax = plt.subplots(figsize=(6, 3))
sc = ax.scatter(x_coords, y_coords, color='blue', marker='o')
ax.grid(True)
ax.set_title('Scatter Plot of Coordinates from JSON Data')
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')

# Adding interactive cursor
cursor = mplcursors.cursor(sc, hover=True)

@cursor.connect("add")
def on_add(sel):
    # `sel.target.index` gives us the index of the point in the scatter plot, corresponding to its index in the JSON array
    index = sel.target.index
    # Use the index to get the x, y coordinates of the selected point from the original data arrays
    x, y = x_coords[index], y_coords[index]
    # Set the annotation position directly to the point's coordinates
    # This will ensure the annotation appears above the point being hovered over
    sel.annotation.set(text=f'Object Index: {index}\nX: {x:.2f}\nY: {y:.2f}',
                       position=(x, y))
    sel.annotation.get_bbox_patch().set(fc="white", alpha=0.6)

plt.show()
