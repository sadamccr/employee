from Employee import *
if __name__ == "__main__":
    emp_list = []
    while True:
        print("Press 1 for Employees.")
        print("Press 2 for Exiting.")

        enter = input("")
        if enter == "1":
            while enter == "1" or enter == "2":
                if enter == "1":
                    print("Press 1 for Add Employee.")
                    print("Press 2 for View Employee.")
                    print("Press 3 for Main Menu.")
                    enter = input("")
                    if enter == "1":
                        name = input("Name = ")
                        sal = int(input("Salary = "))
                        emp = Employee(name,sal)
                        emp_list.append(emp)
                    elif enter == "2":
                        for i in emp_list:
                            print(i.displayEmployee())
                    else:
                            break
                elif enter == "2":
                    break
        else:
            break      