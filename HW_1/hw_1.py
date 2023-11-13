def sort_list_imperative(numbers):
    # Императивный код
    count = 0
    len_list = len(numbers)
    while count < len_list - 1:
        j = 0
        while j < len_list - 1 - count:
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            j += 1
        count += 1
    return numbers

def sort_list_declarative(numbers):
    # Декларативный код
    return sorted(numbers)

if __name__ == ('__main__'):
    some_list = [23, 4, 56, 67,43, 2, 34]

    sorted_list_imperative = sort_list_imperative(some_list)
    print(sorted_list_imperative)

    sorted_list_declarative = sort_list_declarative(some_list)
    print(sorted_list_declarative)
