# grade_calculator.py

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'Fail'

def main():
    try:
        # Accept marks for 5 subjects
        marks = []
        for i in range(5):
            mark = float(input(f"Enter marks for Subject {i+1}: "))
            marks.append(mark)

        # Calculate average
        average = sum(marks) / len(marks)
        grade = calculate_grade(average)

        # Display result
        print(f"\nAverage Marks: {average:.2f}")
        print(f"Grade: {grade}")

    except Exception as e:
        print(f"Error: {e}")

if _name_ == "_main_":
    main()
    