import numpy as np


# update/add code below ...

# Exercise 1
def ways(n):
    count = 0
    for nickels in range(n // 5 + 1):
        pennies = n - 5 * nickels
        if pennies >= 0:
            count += 1
    return count


print(ways(12))

# Exercise 2
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])


# Part 1
def lowest_score(names, scores):
    student_lowest = np.argmin(scores)
    return names[student_lowest]


print(lowest_score(names, scores))

# Part 2
def sort_names(names, scores):
    sort_descend = np.argsort(scores)[::-1]
    return names[sort_descend]


print(sort_names(names, scores))