# Define the Staff base class
class Staff:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def describe(self):
        print(f"Name: {self.name}, ID: {self.employee_id}")

    def perform_duties(self):
        print("Performing general staff duties.")


# Define the Chef subclass
class Chef(Staff):
    def __init__(self, name, employee_id, specialty):
        super().__init__(name, employee_id)
        self.specialty = specialty

    def perform_duties(self):
        print(f"Cooking specialty dishes: {self.specialty}.")


# Define the Waiter subclass
class Waiter(Staff):
    def __init__(self, name, employee_id, tables_assigned):
        super().__init__(name, employee_id)
        self.tables_assigned = tables_assigned

    def perform_duties(self):
        print(f"Serving tables: {self.tables_assigned}.")


# Define the staff_shift function (polymorphism requirement)
def staff_shift(staff_member):
    staff_member.describe()
    staff_member.perform_duties()
    print()  # for spacing


def main():
    # Generic staff member
    s = Staff("Alex Johnson", "S-001")

    # Chef
    c = Chef("Gordon Ramsay", "C-101", "Italian cuisine")

    # Waiter
    w = Waiter("Emily Clarke", "W-202", [1, 3, 5])

    # Test all staff members
    staff_shift(s)
    staff_shift(c)
    staff_shift(w)


if __name__ == "__main__":
    main()
