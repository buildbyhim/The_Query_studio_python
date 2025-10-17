# Create nested tuples
student = ("Ali", (90, 85, 92), ("Math", "Science", "English"))
print(student[0])     # Name
print(student[1][2])  # Score 92
print(student[2][1])  # Subject Science

# Tuple unpacking
name, scores, subjects = student
print(name)
print(scores)
print(subjects)

# Combine tuples
t1 = (10, 20, 30)
t2 = (40, 50)
merged = t1 + t2
print(merged)  # (10, 20, 30, 40, 50)

# Repeat tuple values
repeat = t1 * 2
print(repeat)  # (10, 20, 30, 10, 20, 30)

# Find index and count
nums = (5, 8, 5, 9, 5, 7)
print(nums.index(9))  # index of 9
print(nums.count(5))  # count 3

# Loop through tuple with index
for i, v in enumerate(nums):
    print(i, v)

# Convert list → tuple and tuple → list
lst = [1, 2, 3, 4]
tpl = tuple(lst)
print(tpl)
print(list(tpl))

# Tuple inside list
data = [("Kenya", "Nairobi"), ("USA", "New York")]
for country, city in data:
    print(country, "->", city)

# Tuple sorting by element
people = [("Ali", 25), ("Sara", 19), ("John", 30)]
sorted_people = sorted(people, key=lambda x: x[1])  # sort by age
print(sorted_people)  # [('Sara', 19), ('Ali', 25), ('John', 30)]

# Immutable test (will raise error)
try:
    t1[0] = 99
except TypeError:
    print("Tuples can't change values")
