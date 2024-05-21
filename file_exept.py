# Function to create a file with student data
def create_result_file(file_path):
    with open(file_path, 'w') as file:
        # Write header
        file.write("Name,Register Number,Subject1,Subject2,Subject3,Subject4,Subject5,Total Marks,Percentage\n")
        # Generate data for 30 students
        for i in range(1, 31):
            name = f"Student_{i}"
            register_number = f"REG00{i}"
            grades = ['O', 'A', 'B', 'C', 'D']
            # Random grades for five subjects
            subjects_grades = ','.join([grades[randint(0, 4)] for _ in range(5)])
            # Calculate total marks and percentage
            total_marks = sum([10 if grade == 'O' else 9 if grade == 'A' else 8 if grade == 'B' else 7 if grade == 'C' else 0 for grade in subjects_grades.split(',')])
            percentage = (total_marks / 50) * 100
            # Write student data to file
            file.write(f"{name},{register_number},{subjects_grades},{total_marks},{percentage:.2f}\n")

# Function to read and display file content
def read_result_file(file_path):
    with open(file_path, 'r') as file:
        print(file.read())

# Function to analyze student data and categorize into groups
def analyze_results(input_file, output_file):
    categories = {
        "I": {"min": 90, "max": 100},
        "II": {"min": 80, "max": 89},
        "III": {"min": 70, "max": 79},
        "IV": {"min": 0, "max": 69},
        "V": {"min": 0, "max": 0}
    }

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Skip header
        next(infile)
        # Write header for analysis file
        outfile.write("Category,Name,Register Number,Percentage\n")
        for line in infile:
            data = line.strip().split(',')
            name, reg_num, _, _, _, _, _, _, percentage = data
            percentage = float(percentage)
            category = None
            for cat, limits in categories.items():
                if limits["min"] <= percentage <= limits["max"]:
                    category = cat
                    break
            outfile.write(f"{category},{name},{reg_num},{percentage}\n")

# Example usage
create_result_file("result.txt")
read_result_file("result.txt")
analyze_results("result.txt", "analysis.txt")
