from Package import Package


class OwPackage(Package):

    def __init__(self, id_package: int = 0, weight: float = 0.1, description: str = "Description",
                 overweight: float = 0.1):
        """ Constructor of the overweight package object
        :param id_package: id of package
        :type  int
        :param weight: weight of package (Kg)
        :param description: description of package
        :type  str
        :param overweight: amount of overweight of the package  (Kg)
        :return overweight package object
        :rtype  OwPackage
        """
        self.OW_PRICE: float = 2.0
        self._overweight = overweight
        super().__init__(id_package, weight, description)

    @property
    def overweight(self) -> float:
        """ Returns the overweight of the package (kg)
        :return: overweight of package
        :rtype   float
        """
        return self._overweight

    @overweight.setter
    def overweight(self, overweight: float):
        """ The overweight of the package (kg)
        :param overweight:
        :return:
        """
        if overweight <= 0.0:
            raise "overweight must me positive"
        self._overweight = overweight

    def calculate(self) -> float:
        """ Returns the cost of the Overweight Package
        :return: cost of overweight package
        :rtype   float
        """
        ow = self.overweight * 10 * self.OW_PRICE
        x = (self.weight * 10) * self.VAL_GR_100
        y = self.FIX_PRICE + x + ow
        return y

    def __str__(self):
        """ Returns str of overweight package
        :return: string overweight package
        :rtype:   str
        """
        return ' package id: {0} \n description: {1} \n weight: {2} kg, overweight {3} Kg \n cost: ${4} ' \
               '\n Overweight package'.format(self._id_package, self._description, self._weight, self.overweight,
                                              self.cost)

    def __eq__(self, other):
        """ Compares if two OwPackage objects are equal by checking if each of the attributes are equals
           :param   other: OwPackage object used to compare
           :type    other: OwPackage
           :return: true if the attributes are equal, false if they are not
           :rtype:  boolean
        """
        if isinstance(other, OwPackage):
            return(self._id_package == other._id_package and self._weight == other._weight and
                   self._cost == other._cost and self._description == other._description and self._overweight ==
                   other._overweight)
        return False


if __name__ == '__main__':

    a1 = OwPackage()
    a1.overweight = 0
    print(a1)
