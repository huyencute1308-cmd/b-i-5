import numpy as np
data = [('James', 5, 48.5),
        ('Nail', 6, 52.5),
        ('Paul', 5, 42.1),
        ('Pit', 5, 40.11)]
dtype = [('name', 'U10'), ('grade', 'i4'), ('height', 'f4')]
students = np.array(data, dtype=dtype)

sorted_students = np.sort(students, order=['grade', 'height'])

print(sorted_students)
