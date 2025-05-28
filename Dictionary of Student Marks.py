student_marks = {'alice':'65','bob':'85','krish':'76','arul':'100'}
student_name = input("Enter the Student's name: ")
if student_name in student_marks:
    
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found")