

def get_numbers_by_remainder(limit, remainder):
    return [number for number in range(1, limit + 1) if number % 2 == remainder]


def get_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def show_sum_result(total):
    print("Сумма четных чисел от 1 до 100:", total)


def get_squares(numbers):
    return [x**2 for x in numbers]


def show_squares_result(numbers):
    print("Квадраты нечетных чисел от 1 до 10:", numbers)


def get_number():
    while True:
        try:
            number = int(input("Введите положительное число: "))
            return number
        except ValueError:
            print("Ошибка: нужно ввести число.")


def count_numbers():
    count = 0
    number = 1

    while number >= 0:
        number = get_number()

        if number >= 0:
            count += 1

    return count


def show_count_result(count):
    print("Количество введенных чисел:", count)


even_numbers = get_numbers_by_remainder(100, 0)
sum_even_numbers = get_sum(even_numbers)
show_sum_result(sum_even_numbers)


odd_numbers = get_numbers_by_remainder(10, 1)
squares_odd_numbers = get_squares(odd_numbers)
show_squares_result(squares_odd_numbers)


result = count_numbers()
show_count_result(result)
