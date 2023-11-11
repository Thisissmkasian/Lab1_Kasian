def masa_boroshna(masa_piroga_kg):
    # Розраховуємо масу яблук та тіста в пирозі
    masa_yabluk = 0.6 * masa_piroga_kg
    masa_tista = 0.4 * masa_piroga_kg
    
    # Розраховуємо масу яєць і цукру та масу борошна в тісті
    masa_yaic_tsukor = 0.3 * masa_tista
    masa_boroshna = 0.7 * masa_tista
    
    return masa_boroshna

# Задаємо масу пирога у кілограмах
masa_piroga_kg = 1.0  # Можете ввести іншу масу, якщо потрібно

# Викликаємо функцію та виводимо результат
masa_boroshna_gramy = masa_boroshna(masa_piroga_kg) * 1000  # Переводимо в грами
print("Маса борошна в пирозі: " , masa_boroshna_gramy )