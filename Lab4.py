# i. Function to sort a list without using built-in sort function
def custom_sort(input_list):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
    return input_list

# ii. Function to calculate bonus amount
def calculate_bonus(salary, rating):
    if rating <= 2:
        return 0
    elif rating <= 4:
        return 0.05 * salary
    else:
        return 0.10 * salary

# Test the functions
numbers = [3, 1, 4, 2, 5]
sorted_numbers = custom_sort(numbers)
print("Sorted List:", sorted_numbers)

salary = 50000
rating = 4
bonus = calculate_bonus(salary, rating)
print("Bonus Amount:", bonus)
