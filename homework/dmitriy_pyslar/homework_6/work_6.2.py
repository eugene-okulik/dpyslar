list_number = range(1, 101)
new_list_number = []
for number in list_number:
    if number % 3 == 0 and number % 5 == 0:
        new_list_number.append('FuzzBuzz')
    elif number % 3 == 0:
        new_list_number.append('Fuzz')
    elif number % 5 == 0:
        new_list_number.append('Buzz')
    else:
        new_list_number.append(number)
for number in new_list_number:
    print(number, end='\n')
