from models.models import Saloon, Employee
from framework.control import Controller

while True:
    print("1. Add new saloon \n"
          "2. Get all saloons\n"
          "3. Get saloon by id\n"
          "4. Delete saloon by id\n"
          "5. Add new employee\n"
          "6. Get all employees\n"
          "7. Get employee by id\n"
          "8. Delete employee by id\n"
          "9. Exit \n"
          )
    flag = int(input("Choose: "))
    if flag == 1:
        Controller.add_new_salon()

    elif flag == 2:
        Controller.get_all_saloons()

    elif flag == 3:
        Controller.get_saloon_by_id()

    elif flag == 4:
        Controller.delete_saloon_by_id()

    elif flag == 5:
        Controller.add_new_employ()

    elif flag == 6:
        Controller.get_all_employees()

    elif flag == 7:
        Controller.get_employee_by_id()

    elif flag == 8:
        Controller.delete_employee_by_id()

    elif flag == 9:
        Controller.exit_program()



