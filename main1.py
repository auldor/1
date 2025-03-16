def ob_x(a, b):
    if a > b:
        return a * b + 1
    elif a == b:
        return 25
    else:  
        return (a - 5) / b

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))

x = ob_x(a, b)

print("Результат обчислення X:", x)
