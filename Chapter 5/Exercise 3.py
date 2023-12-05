import tkinter as tk


class Employee:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = ""

    def setData(self, name, position, salary, emp_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id

    def getData(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"


class EmployeeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Details")
        self.geometry("400x300")
        self.employees_added = 0
        self.create_employee_data_fields()

        # Button to add employee
        add_button = tk.Button(self, text="Add Employee", command=self.add_employee)
        add_button.pack()

    def create_employee_data_fields(self):
        self.name_label = tk.Label(self, text="Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.position_label = tk.Label(self, text="Position")
        self.position_label.pack()
        self.position_entry = tk.Entry(self)
        self.position_entry.pack()

        self.salary_label = tk.Label(self, text="Salary")
        self.salary_label.pack()
        self.salary_entry = tk.Entry(self)
        self.salary_entry.pack()

        self.id_label = tk.Label(self, text="ID")
        self.id_label.pack()
        self.id_entry = tk.Entry(self)
        self.id_entry.pack()

    def add_employee(self):
        if self.employees_added >= 5:
            print("Maximum number of employees reached (5 employees).")
        else:
            name = self.name_entry.get()
            position = self.position_entry.get()
            salary = float(self.salary_entry.get())
            emp_id = self.id_entry.get()

            employee = Employee()
            employee.setData(name, position, salary, emp_id)
            222
            print(employee.getData())

            self.employees_added += 1


# Instantiate the EmployeeGUI class
app = EmployeeGUI()
app.mainloop()
