import json

# Path to the JSON file
file_path = 'radio_map.json'

# Reading the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Define the rectangle bounds
x_min, y_min = 50, 50
x_max, y_max = 100, 60

# Filter points within the rectangle
filtered_data = []
for item in data:
    x = item["INSTANCE"]["mCenter"]["x"]
    y = item["INSTANCE"]["mCenter"]["y"]
    if x_min <= x <= x_max and y_min <= y <= y_max:
        filtered_data.append(item)

# Path to save the new JSON file
output_file_path = 'filtered_radio_map.json'

# Saving the filtered data to a JSON file
with open(output_file_path, 'w') as file:
    json.dump(filtered_data, file, indent=4)

print(f"Filtered data saved to {output_file_path}. It contains {len(filtered_data)} points.")
