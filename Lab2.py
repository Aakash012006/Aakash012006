# i. Function to reverse a list
def reverse_list(input_list):
    return input_list[::-1]

# ii. Function to calculate grades
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test the functions
input_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(input_list)
print("Reversed List:", reversed_list)

score = 85
grade = calculate_grade(score)
print("Grade:", grade)
