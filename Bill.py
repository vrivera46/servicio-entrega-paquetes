from Person import Person


class Bill(object):

    def __init__(self, number: str = "Bill number", customer: Person = Person, value: float = 0,
                 date: str = "day/month/year", hour: str = "00:00"):
        """ Constructor of the Bill object
        :param: number: number of bill
        :type  str
        :param: customer: customer of bill
        :type  person
        :param: value: value of bill
        :type  float
        :param: date: date of bill
        :type  str
        :param: hour: hour of bill
        :type  str
        :return bill object
        :rtype  Bill
        """
        self._number = number
        self._customer = customer
        self._value = value
        self._date = date
        self._hour = hour

    @property
    def number(self) -> str:
        """ Returns the number of the bill
        :return: number of bill
        :rtype   str
        """
        return self._number

    @number.setter
    def number(self, number: str):
        """ The number of the bill
        :param number: number of bill
        :type  str
        """
        self._number = number

    @property
    def customer(self) -> Person:
        """ Returns the customer of the bill
        :return: customer of bill
        :rtype   Person
        """
        return self._customer

    @customer.setter
    def customer(self, customer: Person):
        """ The customer of the bill
        :param customer: customer of bill
        :type  Person
        """
        self._customer = customer

    @property
    def value(self) -> float:
        """ Returns the value of the bill
        :return: values of the bill
        :rtype   float
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """ The value of the bill
        :param value: value of the bill
        :type  float
        """
        self._value = value

    @property
    def date(self) -> str:
        """ Returns the date of the bill
        :return: date of the bill
        :rtype   str
        """
        return self._date

    @date.setter
    def date(self, date: str):
        """ The date of the bill
        :param date: date of bill
        :type  str
        """
        self._date = date

    @property
    def hour(self) -> str:
        """ Returns the hour of the bill
        :return: hour of bill
        :rtype   str
        """
        return self._hour

    @hour.setter
    def hour(self, hour: str):
        """ The hour of the bill
        :param hour: hour of bill
        :type  str
        """
        self._hour = hour

    def __str__(self):
        """ Returns str of Bill
        :return: string of bill package
        :rtype:   str
        """
        return ' Ticket # {0} \n {1}, {2} \n {3} \n ${4}'.format(self._number, self._date, self._hour, self._customer,
                                                                 self._value)

    def __eq__(self, other):
        """ Compares if two Bill objects are equal by checking if each of the attributes are equals
           :param   other: Bill object used to compare
           :type    other: Bill
           :return: true if the attributes are equal, false if they are not
           :rtype:  boolean
        """
        if isinstance(other, Bill):
            return (self._number == other._number and self._date == other._date and self._hour == other._hour and
                    self._customer == other._customer and self._value == self._value)


if __name__ == '__main__':
    p1 = Person()
    b1 = Bill("111", p1)
    print(b1)
