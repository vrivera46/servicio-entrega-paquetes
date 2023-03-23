from Package import Package


class StPackage(Package):

    def __init__(self, id_package: int = 0, weight: float = 0.1, description: str = "Description"):
        """ Constructor of the standard package object
        :param id_package: id of standard package
        :type  int
        :param weight: weight of standard package
        :type  float
        :param description: description of standard package
        :type  str
        :return Standard package object
        :rtype  StPackage
        """
        super().__init__(id_package, weight, description)

    def calculate(self) -> float:
        """ Returns the cost of the standard Package
        :return: cost of standard package
        :rtype   float
        """
        x = (self.weight * 10) * self.VAL_GR_100
        y = self.FIX_PRICE + x
        return y

    def __str__(self):
        """ Returns str of Standard package
        :return: string standard package
        :rtype:   str
        """
        return ' package id: {0} \n description: {1} \n weight: {2} Kg \n cost: ${3} ' \
               '\n Standard package'.format(self._id_package, self._description, self._weight, self.cost)

    def __eq__(self, other):
        """ Compares if two StPackage objects are equal by checking if each of the attributes are equals
           :param   other: StPackage object used to compare
           :type    other: StPackage
           :return: true if the attributes are equal, false if they are not
           :rtype:  boolean
        """
        if isinstance(other, StPackage):
            return(self._id_package == other._id_package and self._weight == other._weight and
                   self._cost == other._cost and self._description == other._description)
        return False


if __name__ == '__main__':

    a1 = StPackage()
    a1.weight = 0.1
    print(a1)
