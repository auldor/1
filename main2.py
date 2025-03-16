multiples = []  
for num in range(30, 61):  
    if num % 3 == 0:
        multiples.append(num)

# Виведемо результати
print("Цілі числа, кратні 3, в діапазоні від 30 до 60:", multiples)
print("Кількість таких чисел:", len(multiples))
