from abc import ABC, abstractmethod

# ==========================================
# 1. INHERITANCE & POLIMORFISME
# ==========================================


# Konsep Open/Closed Principle (OCP)
class Employee(ABC):
    """Base Class (Kelas Induk)"""

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    # Polimorfisme: Method ini akan di-override oleh kelas turunan
    # def get_role_description(self):
    #     return f"{self.name} is a general employee."

    # def work(self):
    #     return f"{self.name} is doing general tasks."

    @abstractmethod
    def get_role_description(self):
        pass

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):
    """Sub-class 1"""

    def get_role_description(self):
        return f"{self.name} is a Software Developer."

    def work(self):
        return f"{self.name} is writing code and fixing bugs."


class Manager(Employee):
    """Sub-class 2"""

    def get_role_description(self):
        return f"{self.name} is a Project Manager."

    def work(self):
        return f"{self.name} is managing the team and planning sprints."


class Designer(Employee):
    """Sub-class 3"""

    def get_role_description(self):
        return f"{self.name} is a UI/UX Designer."

    def work(self):
        return f"{self.name} is designing wireframes and prototypes."


# ==========================================
# 2. MULTI-CLASS (Interaksi antar kelas)
# ==========================================


class HRSystem:
    """Kelas kedua yang berinteraksi dengan kelas Employee"""

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    # def get_employee(self):
    #     return self.employees


class PayrollService:
    # Menggunakan if/elif untuk mengecek tipe kelas
    def process_payroll(self, employees):
        print("\n--- Processing Payroll ---")
        for emp in employees:
            if isinstance(emp, Developer):
                bonus = emp.base_salary * 0.10
            elif isinstance(emp, Manager):
                bonus = emp.base_salary * 0.25
            elif isinstance(emp, Designer):
                bonus = emp.base_salary * 0.15
            else:
                bonus = 0

            total = emp.base_salary + bonus
            print(
                f"Paying {emp.name}: Base ${emp.base_salary} + Bonus ${bonus} = Total ${total}"
            )


class EmployeeReport:
    # Kelas ini mengurus logika bisnis, cetak laporan, DAN simulasi database
    def generate_report(self, employees):
        print("\n--- Generating Employee Report ---")
        for emp in employees:
            # Di sini kita menggunakan POLIMORFISME dengan benar
            print(f"- {emp.get_role_description()} | Task: {emp.work()}")

        print("Report generated and printed to console.")


class EmployeeRepository:
    def save_to_database(self, employees):
        print("\n--- Saving to Database ---")
        # Simulasi menyimpan ke database
        print(f"Saved {len(employees)} employees to SQL Database.")
        print("Database connection closed.")


# ==========================================
# 3. EKSEKUSI PROGRAM
# ==========================================
if __name__ == "__main__":
    # Inisialisasi HR System (Multi-class)
    hr_system = HRSystem()
    payroll_service = PayrollService()
    employee_report = EmployeeReport()
    employee_repository = EmployeeRepository()

    # Membuat objek dari berbagai kelas turunan (Inheritance)
    dev = Developer("Budi", 8000)
    mgr = Manager("Siti", 12000)
    des = Designer("Joko", 7000)

    # Menambahkan ke sistem
    hr_system.add_employee(dev)
    hr_system.add_employee(mgr)
    hr_system.add_employee(des)

    employees = hr_system.employees

    # Memanggil method
    payroll_service.process_payroll(employees)
    employee_report.generate_report(employees)
    employee_repository.save_to_database(employees)
