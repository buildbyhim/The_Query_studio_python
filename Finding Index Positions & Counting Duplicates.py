# Create a list with duplicates
nums = [4, 7, 2, 7, 3, 4, 7, 9, 2, 4, 7]

# Find all indexes of a value
target = 7
indexes = [i for i, n in enumerate(nums) if n == target]
print("Indexes of", target, ":", indexes)  
# [1, 3, 6, 10]

# Count duplicates manually
counts = {}
for n in nums:
    counts[n] = counts.get(n, 0) + 1
print("Counts:", counts)
# {4: 3, 7: 4, 2: 2, 3: 1, 9: 1}

# Get the most repeated number
most_common = max(counts, key=counts.get)
print("Most repeated:", most_common)
# 7

# Sort items by count (highest first)
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print(sorted_counts)
# [(7, 4), (4, 3), (2, 2), (3, 1), (9, 1)]

# Create a new list with only unique values
unique = list(counts.keys())
print("Unique:", unique)
# [4, 7, 2, 3, 9]

# Find duplicate numbers only
duplicates = [n for n, c in counts.items() if c > 1]
print("Duplicates:", duplicates)
# [4, 7, 2]

# Replace all duplicates with -1 (keep one copy)
new_list = []
seen = set()
for n in nums:
    if n in seen:
        new_list.append(-1)
    else:
        new_list.append(n)
        seen.add(n)
print("Modified list:", new_list)
# [4, 7, 2, -1, 3, -1, -1, 9, -1, -1, -1]
