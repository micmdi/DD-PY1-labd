numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
list = numbers[:4] + numbers[5:] # список без none
int_1 = sum(list) #сумма без none
int_2 = len(numbers) #количество с none
number = round(int_1 / int_2, 2) #среднее арифметическое

numbers[4] = number
print("Измененный список:", numbers)
