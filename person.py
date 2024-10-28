""" provides a class to describe a person """


class Person:
    """
    Defines a "general" person with

    Attributes
    ----------
    - name: str
        The full name of the person
    - birth_year: int
        The year the person was born
    - address: str
        The address of the person
   """

    def __init__(self, name, year):
        """
        Initializes the object
        :param name: Name of the person
        :param year: The year the person was born
        """

        self._name = name
        self._birth_year = year
        self._address = ''

    @property
    def name(self):
        """
        Returns the name of the person
        :return: Name of the person
        """
        return self._name

    @property
    def birth_year(self):
        """
        Returns the age of the person
        :return: Age of the person
        """
        return self._birth_year

    @property
    def address(self):
        """
        Returns the address of the person
        :return: Address of the person
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of the person
        :param address: The address of the person
        """
        self._address = address

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return f'Person: {self._name}\n\tAlter :   {self.birth_year}\n\tAdresse : {self.address}'


# nur für Test
if __name__ == '__main__':
    person = Person('Max', 2000)
    person.address = 'Musterdorf'
    print(person)
