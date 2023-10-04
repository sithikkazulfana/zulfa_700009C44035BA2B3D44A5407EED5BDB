






class student:

  def __init__(self,name,roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                          key=lambda student: student.cgpa,
                          reverse=True)
 # syntax - lambda arg:exp
  return sorted_students


# Example usage
students = [
  student("Hari","A123",7.8),
  student("Srikanth","A124",8.9),
  student("Saumya","A125",9.1),
  student("Mahidhar","A126",9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
          student.roll_number,
                                                     student.cgpa))












