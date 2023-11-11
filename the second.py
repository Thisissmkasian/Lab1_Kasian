
                 
def stvori_nove_chyslo(number):
    # Перетворюємо введене число у рядок для зручності обробки
    number_str = str(number)

    # Обчислюємо суми за вказаними правилами
    suma_1 = int(number_str[0]) + int(number_str[2]) + int(number_str[4])
    suma_2 = int(number_str[1]) + int(number_str[3])

    # Об'єднуємо отримані суми в одне число
    result = int(str(suma_1) + str(suma_2))

    return result

# Задаємо п'ятизначне десяткове число
input_number = 12345  # Можна ввести інше число, якщо потрібно

# Викликаємо функцію та виводимо результат
result_number = stvori_nove_chyslo(input_number)
print("Отримане число: " , result_number )