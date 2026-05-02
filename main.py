
def get_even_numbers():
    even_numbers = []

    number = 1
    while number <= 100:
        if number % 2 == 0:
            even_numbers.append(number)
        number += 1

    return even_numbers


def get_sum(numbers):
    sum = 0

    for number in numbers:
        sum += number

    return sum


def show_results(total):
    print("Сумма четных чисел от 1 до 100:", total)


def get_odd_numbers():
    odd_numbers = []

    number = 1
    while number <= 10:
        if number % 2 != 0:
            odd_numbers.append(number)
        number += 1

    return odd_numbers


def get_squares(numbers):
    squares = [x**2 for x in numbers]
    return squares


def show_squares(numbers):
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
    number = get_number()
    while number >= 0:
        count += 1
        number = get_number()

    return count

def show_result(count):
    print("Количество введенных чисел:", count)


even_numbers = get_even_numbers()
sum_even_numbers = get_sum(even_numbers)
show_results(sum_even_numbers)


odd_numbers = get_odd_numbers()
squares_odd_numbers = get_squares(odd_numbers)
show_squares(squares_odd_numbers)


result = count_numbers()
show_result(result)
