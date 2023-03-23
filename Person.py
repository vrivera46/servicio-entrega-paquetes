class Person(object):
    """
    Class used to represent a Person
    """

    def __init__(self, id_person: int = 0, name: str = 'Name', last_name: str = "LastName", phone: str = "phone number",
                 mail="example@mail.com"):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :param phone: phone of person
        :type phone: str
        :param mail: mail of the person
        :type  str
        :returns: Person object
        :rtype: object
        """
        self._id_person = id_person
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._mail = mail

    @property
    def id_person(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_person

    @id_person.setter
    def id_person(self, id_person: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._last_name = last_name
    
    @property
    def phone(self) -> str:
        """ Returns the phone of the person
        :returns  phone of the person
        :rtype    str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """ Phone of the person
        :param phone: phone of the person
        :type  str 
        """
        self._phone = phone

    @property
    def mail(self) -> str:
        """ Returns the mail of the person
        :returns    mail of the person
        :rtype      str
        """
        return self._mail

    @mail.setter
    def mail(self, mail: str):
        """ The mail of the person
        :param mail: mail of the person
        :type  str
        """
        self._mail = mail

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1} {2}, {3}, {4})'.format(self.id_person, self.name, self.last_name, self.phone, self.mail)

    def __eq__(self, other):
        """ Compares if two Person objects are equal by checking if each of the attributes are equals
           :param   other: Person object used to compare
           :type    other: Person
           :return: true if the attributes are equal, false if they are not
           :rtype:  boolean
        """
        if isinstance(other, Person):
            return(
                self._id_person == other._id_person and self._mail == other._mail and self._name == other._name,
                self._last_name == other._last_name and self._phone == other._phone
            )
        return False


if __name__ == '__main__':

    edwin = Person(id_person=73577376, name="Edwin", last_name="Puertas", phone="00000000", mail="email@hotmail.com")
    edwin.name = "Edwin. A"
    print(edwin)

    juan = Person()
    miguel = Person()
    miguel.name = "miguel"
    print(juan.__eq__(miguel))
