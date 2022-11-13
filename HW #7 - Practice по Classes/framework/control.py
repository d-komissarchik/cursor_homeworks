from models.models import Saloon, Employee


class Controller:

    @staticmethod
    def add_new_salon():
        name = input("Type name of the new Saloon: ")
        location = input("Type location of the new saloon: ")
        salon = Saloon(name, location)
        salon.save()

    @staticmethod
    def get_all_saloons():
        saloons = Saloon.get_all()
        for saloon in saloons:
            print(saloon["id"])
            print(saloon["name"])
            print(saloon["location"])
    @staticmethod
    def get_saloon_by_id():
        id = int(input('Type id of saloon: '))
        saloon = Saloon.get_by_id(id)
        print(saloon["id"])
        print(saloon["name"])
        print(saloon["location"])

    @staticmethod
    def delete_saloon_by_id(id):
        id = int(input('Type id of saloon, which you want to delete: '))
        Saloon.delete(id)

    @staticmethod
    def add_new_employ():
        name = input("Type name of employee: ")
        email = input("Type email of employee: ")
        name_saloon = input("Type name of saloon: ")
        employee = Employee(name, email, name_saloon)
        employee.save()

    @staticmethod
    def get_all_employees():
        employees = Employee.get_all()
        for employee in employees:
            print(employee["id"])
            print(employee["name"])
            print(employee["email"])
            print("Name of saloon is", employee["name_saloon"])
    @staticmethod
    def get_employee_by_id():
        id = int(input('Type id of employee: '))
        employee = Employee.get_by_id(id)
        print(employee["id"])
        print(employee["name"])
        print(employee["email"])
        print("Name of saloon is", employee["name_saloon"])

    @staticmethod
    def delete_employee_by_id():
        id = int(input('Type id of employee: '))
        Employee.delete(id)

    @staticmethod
    def exit_program():
        print("Goodbye!")
        exit()



