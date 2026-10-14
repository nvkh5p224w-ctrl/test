# Problem 2: Student class with tuition calculation

class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        if self.district_code == "I":
            rate = 250.00
        else:
            rate = 500.00
        return self.enrolled_credits * rate

student = Student("Alex", "Morgan", "I", 12)

print("Student Tuition Calculator")
print("--------------------------")
print(f"Student: {student.first_name} {student.last_name}")
print(f"District code: {student.district_code}")
print(f"Enrolled credits: {student.enrolled_credits}")
print(f"Tuition owed: ${student.compute_tuition():,.2f}")
