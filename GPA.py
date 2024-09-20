def calculate_gpa(grades):
    # Mapping letter grades to grade points
    grade_points = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'D-': 0.7,
        'F': 0.0
    }
    
    total_points = 0
    total_courses = len(grades)

    for grade in grades:
        if grade in grade_points:
            total_points += grade_points[grade]
        else:
            print(f"Invalid grade: {grade}")
            total_courses -= 1  # Exclude invalid grades from total count
    
    if total_courses > 0:
        gpa = total_points / total_courses
        return gpa
    else:
        return 0.0  # Prevent division by zero

if __name__ == "__main__":
    print("Welcome to the GPA Calculator!")
    grades_input = input("Enter your grades separated by commas (e.g., A, B, C+): ")
    
    # Splitting input into a list and stripping whitespace
    grades = [grade.strip() for grade in grades_input.split(',')]
    
    gpa = calculate_gpa(grades)
    
    print(f"Your GPA is: {gpa:.2f}")
