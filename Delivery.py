from Address import Address
from StPackage import StPackage
from OwPackage import OwPackage
from Bill import Bill
from Person import Person
from Package import Package


class Delivery (object):

    def __init__(self, id_delivery: int = 0, date: str = "day/month/year", time: str = "00:00", sender: Person = Person,
                 receiver: Person = Person, sender_add: Address = Address, receiver_add: Address = Address,
                 contact: Person = Person, items: Package = Package, bill: Bill = Bill):
        """ Constructor of the Delivery object
        :param id_delivery: id of
        :param date:
        :param time:
        :param sender:
        :param receiver:
        :param sender_add:
        :param receiver_add:
        :param contact:
        :param items:
        :param bill:
        """
        self._id_delivery = id_delivery
        self._date = date
        self._time = time
        self._sender = sender
        self._receiver = receiver
        self._sender_add = sender_add
        self._receiver_add = receiver_add
        self._contact = contact
        self._items = items
        self._bill = bill

    @property
    def id_delivery(self) -> int:
        """ Returns the id of the delivery
        :return: id of delivery
        :rtype   int
        """
        return self._id_delivery

    @id_delivery.setter
    def id_delivery(self, id_delivery: int):
        """ The id of the delivery
        :param id_delivery: id of delivery
        :type  int
        """
        self._id_delivery = id_delivery

    @property
    def date(self) -> str:
        """ Return the date of creation of the delivery
        :return: date of delivery
        :rtype   Str
        """
        return self._date

    @date.setter
    def date(self, date: str):
        """ The date of creation of the delivery
        :param date: date of delivery
        :return: str
        """
        self._date = date

    @property
    def time(self) -> str:
        """ Returns the time of the creation of the delivery
        :return: time of delivery
        :rtype   str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """The time of delivery
        :param time: time of delivery
        :type  str
        """
        self._time = time

    @property
    def sender(self) -> Person:
        """ Returns the sender of the delivery
        :return: sender of delivery
        :rtype Person
        """
        return self._sender

    @sender.setter
    def sender(self, sender: Person):
        """ The sender of the delivery
        :param sender: sender of delivery
        :typer person
        """
        self._sender = sender

    @property
    def receiver(self) -> Person:
        """ Returns the receiver of the delivery
        :return: receiver of delivery
        :rtype Person
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver: Person):
        """ The receiver of the delivery
        :param receiver: receiver of delivery
        :typer person
        """
        self._receiver = receiver

    @property
    def sender_add(self) -> Address:
        """ Returns the sender's address
        :return: sender's address
        :type    Address
        """
        return self._sender_add

    @sender_add.setter
    def sender_add(self, sender_add: Address):
        """ The address of the sender
        :param sender_add: sender's address
        :type  Address
        """
        self._sender_add = sender_add

    @property
    def receiver_add(self) -> Address:
        """ Returns the receiver's address
        :return: receiver's address
        :type    Address
        """
        return self._receiver_add

    @receiver_add.setter
    def receiver_add(self, receiver_add):
        """ The address of the receiver
        :param receiver_add: receiver's address
        :type  Address
        """
        self._receiver_add = receiver_add

    @property
    def contact(self) -> Person:
        """ Returns the contact of the delivery
        :return: contact of deliver
        ;:rtype  Person
        """
        return self._contact

    @contact.setter
    def contact(self, contact: Person):
        """ The contact of the delivery
        :param contact:
        :return:
        """
        self._contact = contact

    @property
    def items(self) -> Package:
        """ Returns the items of the delivery
        :return: items of deliver
        :rtype  Package
        """
        return self._items

    @items.setter
    def items(self, items: Package):
        """ The items of the delivery
        :param items: items of delivery
        :type  package
        """
        self._items = items

    def __str__(self):
        """ Returns str of Delivery
        :return: string of delivery
        :rtype:   str
        """
        return 'id of deliver: {0} \n {1}, {2} \n sender: {3} \n sender address: {4}\n receiver:{5}\n ' \
               'receiver address:{6} \n contact: {7} \n items: {8} \n bill: {9}'.format(self._id_delivery, self._date,
                                                                                        self._time, self._sender,
                                                                                        self._sender_add, self._receiver
                                                                                        , self._receiver_add,
                                                                                        self._contact, self._items,
                                                                                        self._bill)

    def __eq__(self, other):
        """ Compares if two Delivery objects are equal by checking if each of the attributes are equals
           :param   other: Delivery object used to compare
           :type    other: Delivery
           :return: true if the attributes are equal, false if they are not
           :rtype:  boolean
        """
        if isinstance(other, Delivery):
            return (self._id_delivery == other._id_delivery and self._date == other._date and self._time == other.time
                    and self._sender == other._sender and self._receiver == other._receiver and self._contact ==
                    other._contact and self._items == other._items and self._bill == other._bill)
        return False


if __name__ == '__main__':
    person1 = Person(1007733, "victor", "Rivera", "3217384810", "abc@gmail.com")
    person2 = Person(1068423, "David", "hoyos", "3113286554", "abd@hotmail.com")
    add1 = Address("bolivar", "cartagena", "95000", "Santa lucia", "#46", "M18", "segundo piso")
    add2 = Address("atlantico", "barranquilla", "73000", "San juan", "#29", "M48", "primer piso")
    date = "15/03/2023"
    time = "08:20"
    bill = Bill("452", person1, 15000, date, time)
    item1 = StPackage(123, 0.5, "clothes")
    item2 = OwPackage(124, 1.2, "shows")
    delivery1 = Delivery(486, date, time, person1, person2, add1, add2, person1, item1, bill)
    delivery2 = Delivery(576, date, time, person1, person2, add1, add2, person1, item2, bill)
    print(delivery1, "\n\n")
    print(delivery2, "\n\n")
    print(item2.__eq__(item1))
    item3 = item2
    print(item2.__eq__(item3))

