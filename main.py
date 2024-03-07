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
        from_diameter(diameter: int):
            Create an instance of a circle using a diameter.
        check_radius():
            Check a valid radius.
        """
    PI = 3.14

    def __init__(self, radius: int | float) -> None:
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

    @classmethod
    def from_diameter(cls, diameter: int) -> "Circle":
        """
        Use this method to create an instance of a circle using a diameter.
        :param diameter:
        :return:
        """
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def check_radius(radius: int) -> bool:
        """
        Method to check a valid radius.
        :param radius:
        :return:
        """
        return radius > 0

