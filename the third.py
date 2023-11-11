def drukuy_litery_B(symbol):
    # Виводимо літеру "В" у вигляді 5 рядків
    for i in range(5):
        if i == 0 or i == 2 or i == 4:
            print(symbol * 2 + " " + symbol * 2)
        else:
            print(symbol + " " * 2 + symbol)

# Запитуємо користувача ввести символ для відображення літери "В"
korystuvach_symbol = input("Введіть символ: ")

# Викликаємо функцію та передаємо користувацький символ
drukuy_litery_B(korystuvach_symbol)