# Problem 1: Employee class with a bonus method

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def compute_bonus(self, bonus_rate):
        # Bonus rate is entered as a decimal (for example, 0.10 means 10%).
        return self.salary * bonus_rate

employee = Employee("Jordan", "Taylor", 60000.00)

print("Employee Bonus Calculator")
print("-------------------------")
print(f"Employee: {employee.first_name} {employee.last_name}")
print(f"Annual salary: ${employee.salary:,.2f}")
bonus_rate = float(input("Enter bonus rate as a decimal (example: 0.10 for 10%): "))
bonus = employee.compute_bonus(bonus_rate)
print(f"Bonus: ${bonus:,.2f}")
