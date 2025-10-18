# Create a nested dictionary
students = {
    "Ali": {"age": 20, "scores": {"Math": 90, "Science": 88}},
    "Sara": {"age": 22, "scores": {"Math": 95, "Science": 91}},
    "John": {"age": 21, "scores": {"Math": 84, "Science": 76}}
}

# Access nested values
print(students["Sara"]["scores"]["Math"])  # 95

# Add new key-value
students["Ali"]["scores"]["English"] = 89
print(students["Ali"])

# Loop keys and values
for name, info in students.items():
    print(name, "->", info["age"], "yrs")

# Get all math scores
math_scores = [info["scores"]["Math"] for info in students.values()]
print("Math scores:", math_scores)

# Find top math scorer
top = max(students, key=lambda n: students[n]["scores"]["Math"])
print("Top Math Student:", top)

# Merge two dicts
extra = {"Mike": {"age": 23, "scores": {"Math": 80, "Science": 85}}}
students.update(extra)
print(students.keys())

# Count how many subjects per student
subject_count = {n: len(info["scores"]) for n, info in students.items()}
print(subject_count)

# Sort by Science score (descending)
sorted_sci = dict(sorted(students.items(), key=lambda x: x[1]["scores"]["Science"], reverse=True))
print(sorted_sci)

# Safe access using get()
print(students.get("Ali").get("age"))  # 20

# Delete a key safely
students["John"]["scores"].pop("Science", None)
print(students["John"])

# Combine lists into dict
names = ["Tom", "Lina", "Musa"]
marks = [77, 83, 69]
combined = dict(zip(names, marks))
print(combined)

# Dictionary comprehension filter
passed = {k: v for k, v in combined.items() if v >= 75}
print("Passed:", passed)
