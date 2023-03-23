from abc import abstractmethod


class Package(object):

    def __init__(self, id_package: int = 0000, weight: float = 0.1, description: str = "Description"):
        """Package constructor object

        :param id_package: id of package
        :type  int
        :param weight: weight of package
        :type  float
        :param description: description of package
        :type  str
        :returns Package object
        :rtype Package
        """
        self.FIX_PRICE: float = 5.0
        self.VAL_GR_100: float = 1.0
        self._id_package = id_package
        self._weight = weight
        self._description = description
        self._cost = self.calculate()

    @property
    def id_package(self) -> int:
        """ Returns the id of package
        :return:id of package
        :rtype: int
        """
        return self._id_package

    @id_package.setter
    def id_package(self, id_package: str):
        """ The id of the package
        :param: id of package
        :type: str
        """
        self._id_package = id_package

    @property
    def weight(self) -> float:
        """ Returns the weight of the package
        :return: weight of package
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        """ the weight of the package
        :param weight: weight of the package
        :type: float
        """
        if weight <= 0.0:
            raise "weight must be positive"
        self._weight = weight

    @property
    def description(self) -> str:
        """ Returns the description of the package
        :return description of package
        :rtype str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """ The description of the package
        :param description: description of package
        :type  str
        """
        self._description = description

    @property
    def cost(self) -> float:
        """ Returns the cost of the package
        :return: cost of package
        :type:   float
        """
        return self._cost

    @cost.setter
    def cost(self, cost: float):
        """ The cost of the package
        :param cost: cost of package
        :type  float
        """
        self._cost = cost

    @abstractmethod
    def calculate(self):
        """
        abstract method tha calculates the cost of the package
        """
        pass

    def __str__(self):
        """ Returns str of package
          :returns: string package
          :rtype:   str
        """
        return ' package id: {0} \n description: {1} \n weight: {2} Kg \n cost: ${3}'.format(self._id_package,
                                                                                             self._description,
                                                                                             self._weight, self.cost)

    def __eq__(self, other):
        """ Compares if two Package objects are equal by checking if each of the attributes are equals
           :param   other: Package object used to compare
           :type    other: Package
           :return: true if the attributes are equal, false if they are not
           :rtype:  boolean
        """
        if isinstance(other, Package):
            return(self._id_package == other._id_package and self._weight == other._weight and
                   self._cost == other._cost and self._description == other._description)
        return False


if __name__ == '__main__':

    a1 = Package()
    a1.weight = 0.1
    print(a1)
