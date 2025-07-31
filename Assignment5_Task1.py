student_info = {"Alice":89,"Bob":99,"Ross":69,"Tim":100,"Ruby":95}
input_name = input("Enter the students name: ")

print(student_info[input_name] if input_name in student_info else "Student not found.")