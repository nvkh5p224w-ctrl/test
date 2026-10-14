# Problem 3: Student class using a dictionary of tuition rates

class Student:
    # Dictionary maps each district code to tuition per credit hour.
    TUITION_RATES = {
        "I": 250.00,  # In district
        "O": 500.00,  # Out of district
        "X": 800.00,  # International
        "G": 250.00   # Reciprocity
    }

    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        # Any unknown code is charged the out-of-district rate.
        if self.district_code in Student.TUITION_RATES:
            rate = Student.TUITION_RATES[self.district_code]
        else:
            rate = Student.TUITION_RATES["O"]
        return self.enrolled_credits * rate

students = [
    Student("Alex", "Morgan", "I", 12),
    Student("Jamie", "Lee", "O", 9),
    Student("Sam", "Patel", "X", 6),
    Student("Taylor", "Reed", "G", 12)
]

code_names = {
    "I": "In district",
    "O": "Out of district",
    "X": "International",
    "G": "Reciprocity"
}

print("Student Tuition by District Code")
print("-" * 76)
print(f"{'Student':<20}{'Code':<8}{'District Type':<20}{'Credits':>9}{'Tuition':>16}")
print("-" * 76)
for student in students:
    district_type = code_names[student.district_code]
    print(f"{student.first_name + ' ' + student.last_name:<20}"
          f"{student.district_code:<8}{district_type:<20}"
          f"{student.enrolled_credits:>9}{student.compute_tuition():>16,.2f}")
