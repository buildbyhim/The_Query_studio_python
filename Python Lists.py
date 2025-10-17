# A list can store multiple values in one variable
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Access items using index (starts at 0)
print(fruits[0])  # first item
print(fruits[2])  # third item

# Update an item by index
fruits[1] = "mango"
print(fruits)

# Add one item
fruits.append("orange")

# Add multiple items
fruits.extend(["grape", "pineapple"])
print(fruits)

# Insert at a specific position
fruits.insert(1, "kiwi")
print(fruits)

# Remove by value
fruits.remove("apple")

# Remove by index
del fruits[0]

# Remove last item
fruits.pop()
print(fruits)

# Use a for loop
for fruit in fruits:
    print(fruit)

# Check with 'in'
if "mango" in fruits:
    print("Mango is here!")

# Sort in ascending order
fruits.sort()

# Sort in descending order
fruits.sort(reverse=True)
print(fruits)

# Count how many items
print(len(fruits))
