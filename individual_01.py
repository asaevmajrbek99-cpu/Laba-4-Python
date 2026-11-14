import sys

if __name__ == "__main__":
    algebra = [int(value) for value in input(
        "Оценки по алгебре: "
    ).split()]

    geometry = [int(value) for value in input(
        "Оценки по геометрии: "
    ).split()]

    physics = [int(value) for value in input(
        "Оценки по физике: "
    ).split()]

    if not algebra or not geometry or not physics:
        print("Ошибка: списки не должны быть пустыми", file=sys.stderr)
        sys.exit(1)

    if len(algebra) != len(geometry) or len(algebra) != len(physics):
        print("Ошибка: списки должны иметь одинаковую длину", file=sys.stderr)
        sys.exit(1)

    for grade in algebra + geometry + physics:
        if not 2 <= grade <= 5:
            print("Ошибка: оценки должны быть от 2 до 5", file=sys.stderr)
            sys.exit(1)

    total = 0
    for grade in algebra:
        total += grade

    average = total / len(algebra)

    without_twos = 0
    for index in range(len(algebra)):
        if (algebra[index] != 2 and
            geometry[index] != 2 and
            physics[index] != 2):
            without_twos += 1

    print(f"Средняя оценка по алгебре: {average:.2f}")
    print(f"Количество учеников без двоек: {without_twos}")