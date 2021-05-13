from datetime import date


class Person:

    def __init__(self, name, address, nationality, birthdate):
        self.name = name
        self._address = address
        self.nationality = nationality
        self.birthdate = birthdate

    def calculate_age(self):
        diff = date.today() - self.birthdate
        return round(diff.days / 365, 1)


class Employee(Person):

    def __init__(self, name, address, nationality, birthdate, id, department, salary):
        super().__init__(name, address, nationality, birthdate)

        self.id = id
        self.department = department
        self.performance = None
        self.salary = salary


class Programmer(Employee):

    def __init__(self, name, address, nationality, birthdate, id, department, salary):
        super().__init__(name, address, nationality, birthdate, id, department, salary)

    def change_address(self, address):
        self.address = address


class HRAdmin(Employee):

    def __init__(self, name, address, nationality, birthdate, id, department, salary):
        super().__init__(name, address, nationality, birthdate, id, department, salary)

    def change_info(self, employee, field, value):
        setattr(employee, field, value)


class Manager(Employee):
    def __init__(self, name, address, nationality, birthdate, id, department, salary, dept_managed):
        super().__init__(name, address, nationality, birthdate, id, department, salary)
        self.dept_managed = dept_managed

    def change_address(self, address):
        self.address = address

    def approve_increase(self, employee_id):
        if employee_id in self.dept_managed:
            if self.dept_managed[employee_id].performance:
                return self.dept_managed[employee_id].performance > 80
            else:
                raise AttributeError(f"Employee {employee_id} hasn't reached required performance yet.")
        else:
            raise KeyError(f"Employee '{employee_id}' is not in the managed department")

    def evaluate_performance(self, employee_id, value):
        if employee_id in self.dept_managed:
            self.dept_managed[employee_id].performance = value
        else:
            raise KeyError(f"Employee '{employee_id}' is not in the managed department")