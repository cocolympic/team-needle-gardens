def find_first_even(numbers):
    return next((x for x in numbers if x % 2 == 0), None)

test_numbers = [1, 3, 7, 4, 9, 6]
first_even = find_first_even(test_numbers)
print(f"最初の偶数: {first_even}")
