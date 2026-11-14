if __name__ == "__main__":
    numbers = [float(value) for value in input(
        "Введите элементы списка через пробел: "
    ).split()]

    if not numbers:
        print("Ошибка: список не должен быть пустым")
        raise SystemExit(1)

    product = 1.0
    has_negative = False

    for number in numbers:
        if number < 0:
            product *= number
            has_negative = True

    if not has_negative:
        product = 0

    max_index = numbers.index(max(numbers))

    total = 0.0
    for number in numbers[:max_index]:
        if number > 0:
            total += number

    numbers.reverse()

    print(f"Произведение отрицательных элементов: {product:g}")
    print(f"Сумма положительных элементов до первого максимума: {total:g}")
    print("Список в обратном порядке:", numbers)