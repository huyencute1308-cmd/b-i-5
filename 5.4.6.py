numbers = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))
max_value = max(numbers)
min_value = min(numbers)

max_index = numbers.index(max_value)
min_index = numbers.index(min_value)

print("Giá trị lớn nhất:", max_value, "ở vị trí:", max_index)
print("Giá trị nhỏ nhất:", min_value, "ở vị trí:", min_index)



