input_number = int(input("Введіть п'ятизначне десяткове число: "))

# Отримання окремих цифр числа
digit_5 = input_number % 10
digit_4 = (input_number // 10) % 10
digit_3 = (input_number // 100) % 10
digit_2 = (input_number // 1000) % 10
digit_1 = (input_number // 10000) % 10

# Обчислення сум
sum_1 = digit_1 + digit_3 + digit_5
sum_2 = digit_2 + digit_4

# Формування нового числа
result_number = int(str(sum_1) + str(sum_2))

# Виведення результату
print("Нове число:", result_number)
