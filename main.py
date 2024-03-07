class Circle:
    """
        A class to represent a circle.
        ...

        Attributes
        ----------
        radius : int
            radius of the circle

        Methods
        -------
        area():
            Counts the area of a circle.
        """
    PI = 3.14

    def __init__(self, radius: int) -> None:
        """
        Constructs all the necessary attributes for a circle object.
        :param radius:
        """
        self.radius = radius

    def area(self) -> float:
        """
        Counts the area of a circle.
        :return:
        """
        return Circle.PI * self.radius ** 2

