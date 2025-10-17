# Create a deep nested list
data = [
    ["Kenya", ["Nairobi", ["Westlands", "Kilimani"]]],
    ["USA", ["New York", ["Brooklyn", "Manhattan"]]],
    ["Japan", ["Tokyo", ["Shinjuku", "Shibuya"]]]
]

# Access level 1 (country)
print(data[0][0])  # Kenya

# Access level 2 (city)S
print(data[1][1][0])  # New York

# Access level 3 (area)
print(data[2][1][1][1])  # Shibuya

# Loop through nested items
for country, info in data:
    city = info[0]
    area_list = info[1]
    print(country, "->", city, "->", area_list)

# Use list comprehension to get all areas
areas = [area for _, info in data for area in info[1]]
print(areas)
# [['Westlands', 'Kilimani'], ['Brooklyn', 'Manhattan'], ['Shinjuku', 'Shibuya']]

# Access last city of each country
last_city = [info[0] for _, info in data]
print(last_city)  # ['Nairobi', 'New York', 'Tokyo']

# Access second area of each country
second_areas = [info[1][1] for _, info in data]
print(second_areas)  # ['Kilimani', 'Manhattan', 'Shibuya']

# Change a nested value
data[0][1][1][0] = "Parklands"
print(data[0])  
# ['Kenya', ['Nairobi', ['Parklands', 'Kilimani']]]
