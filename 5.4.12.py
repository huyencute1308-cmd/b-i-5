import numpy as np
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

indices = np.lexsort((student_id, student_height))

print("Các chỉ số sắp xếp:", indices)

sorted_ids = student_id[indices]
sorted_heights = student_height[indices]

print("Student IDs sau khi sắp xếp:", sorted_ids)
print("Student heights sau khi sắp xếp:", sorted_heights)
