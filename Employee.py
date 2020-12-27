from Salary import *

class Employee:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
        self.obj_salary = Salary(pay)
    
    def displayEmployee(self):
        print(f"Name = {self.name}, Pay = {self.pay}, Total Salary = {self.obj_salary.annualPay()}")
