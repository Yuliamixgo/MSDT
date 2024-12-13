def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль невозможно."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Ошибка: деление на ноль невозможно."
    return a % b

def manual_calculator():
    print("Добро пожаловать в ручной калькулятор!")
    print("Выберите операцию:")
    print("1: Сложение (+)")
    print("2: Вычитание (-)")
    print("3: Умножение (*)")
    print("4: Деление (/)")
    print("5: Возведение в степень (**)")
    print("6: Остаток от деления (%)")
    print("Введите 'exit', чтобы выйти.")

    while True:
        choice = input("\nВыберите операцию: ")
        if choice.lower() == 'exit':
            print("Выход из программы. До свидания!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Ошибка: некорректный ввод. Попробуйте снова.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == '1':
                print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"Результат: {num1} ** {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"Результат: {num1} % {num2} = {modulus(num1, num2)}")
        except ValueError:
            print("Ошибка: введите числовые значения.")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

# Запуск программы
manual_calculator()
