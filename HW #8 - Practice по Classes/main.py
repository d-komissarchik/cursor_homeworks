# from datetime import date
# from decimal import Decimal
# from classes import Employee
#
# john = Employee(name='John', start=date(2022, 10, 5), rate=Decimal("11"), taxes=10)
#
# john.update_rate(Decimal("10"))
# print(john.how_long())
# print(john._rate)
#
# Employee.show_line()
# Employee.show_row(john)
# Employee.show_line()


from decimal import Decimal
from datetime import date

from decorator import timer
from classes import Employee


employees = [
    Employee(name="John", start=date(2022, 5, 20), rate=Decimal("11"), taxes=10),
    Employee(name="Alex", start=date(2022, 5, 1), rate=Decimal("50"), taxes=20),
    Employee(name="Kseniya", start=date(2022, 5, 10), rate=Decimal("50"), taxes=40),
    Employee(name="Valeriy", start=date(2022, 4, 20), rate=Decimal("60"), taxes=50),
    Employee(name="Vera", start=date(2019, 5, 20), rate=Decimal("99"), taxes=60),
    Employee(name="Suzanna", start=date(2021, 5, 20), rate=Decimal("20"), taxes=10),
    Employee(name="Gleb", start=date(2021, 5, 20), rate=Decimal("20"), taxes=10),
]



@timer(func_name = "Show table")
def show_table():
    Employee.show_header()
    for employee in employees:
        employee.show_row()
        employee.show_line()


def update_table():
    for employee in employees:
        employee.update_rate(employee.rate + 10)


if __name__ == "__main__":
    show_table()
    update_table()
    show_table()


