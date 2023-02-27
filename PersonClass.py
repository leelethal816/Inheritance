class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def print_person(self):
        print(f"Name is {self.__name}")
        print(f"Address is {self.__address}")
        print(f"Phone is {self.__phone}")


class Customer(Person):
    def __init__(self, name, address, phone, cn, mailing):
        Person.__init__(self, name, address, phone)

        self.__cn = cn
        self.__mailing = mailing

    def print_person(self):
        Person.print_person(self)
        print(f"Customer number is {self.__cn}")
        print(f"Mailing list preference is {self.__mailing}")
