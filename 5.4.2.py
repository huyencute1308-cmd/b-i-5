import datetime as dt

# Chuỗi thời gian cần chuyển đổi
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# Lấy các thành phần ngày – tháng – giờ – phút – giây
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))

# Lấy thời gian hiện tại của hệ thống
t2 = dt.datetime.now()

# Tính khoảng cách thời gian (kiểu timedelta)
diff = t2 - t1

print('How many days difference? ' + str(diff.days))


