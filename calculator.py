# Student Grade Evaluation Program using Command Line Arguments

import sys

# Check if exactly 5 marks are given as arguments
if len(sys.argv) != 6:
    print("Usage: python student_grade_args.py mark1 mark2 mark3 mark4 mark5")
    sys.exit()

# Convert arguments to float values
marks = [float(m) for m in sys.argv[1:]]

# Calculate average
average = sum(marks) / 5

# Determine grade
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'

# Display results
print("\n--- Student Grade Evaluation ---")
print(f"Marks: {marks}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")

