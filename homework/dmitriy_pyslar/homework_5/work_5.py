
# 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# 2.1
line_1 = 'результат операции: 42'
num_1 = line_1[-2:]
num_1 = int(line_1[-2:])
result_1 = num_1 + 10
print(result_1)

# 2.2
line_2 = 'результат операции: 514'
num_2 = line_2[-3:]
num_2 = int(line_2[-3:])
result_2 = num_2 + 10
print(result_2)

# 2.3
line_3 = 'результат работы программы: 9'
num_3 = line_3[-1:]
num_3 = int(line_3[-1:])
result_3 = num_3 + 10
print(result_3)

# 2.0 Еще один вариант на разную длину числа(подсмотрел в интернете)
line = "результат операции: 1234"
start_index = line.index(":")
num = line[start_index + 2:]
num = int(line[start_index + 2:])
result = num + 10
print(result)

# 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
text1 = 'Students'
text2 = 'study these subjects:'
print(text1, ', '.join(students), text2, ', '.join(subjects))
