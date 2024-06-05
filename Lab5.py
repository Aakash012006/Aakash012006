# i. Function to determine if the number of even numbers is greater than the number of odd numbers
def even_or_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    if even_count > odd_count:
        return "even"
    else:
        return "odd"

# ii. Function to find students present in both lists
def common_students(list1, list2):
    return list(set(list1) & set(list2))
