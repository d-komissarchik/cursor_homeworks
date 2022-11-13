from framework.models import Model


class Saloon(Model):
    file = "saloons.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employees.json"

    def __init__(self, name, email, name_saloon):
        self.name = name
        self.email = email
        self.name_saloon = name_saloon
