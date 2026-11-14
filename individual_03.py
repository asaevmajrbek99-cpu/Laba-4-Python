if __name__ == "__main__":
    numbers = tuple(
        float(value)
        for value in input("Введите вещественные числа через пробел: ").split()
    )

    if not numbers:
        print("Ошибка: кортеж не должен быть пустым")
        raise SystemExit(1)

    result_list = []

    for k, number in enumerate(numbers, start=1):
        if k % 2 != 0:
            result_list.append(number * k)
        else:
            result_list.append(number / k)

    result = tuple(result_list)

    print("Исходный кортеж:", numbers)
    print("Новый кортеж:", result)
