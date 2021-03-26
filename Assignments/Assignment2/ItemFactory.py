import abc

from Toy import SantasWorkshop, RCSpider, RobotBunny
from StuffedAnimal import DancingSkeleton, Reindeer, EasterBunny
from Candy import PumpkinCaramelToffee, CandyCanes, CremeEggs


class ItemFactory(abc.ABC):
    """
    A factory that creates store items during for different theme.
    """

    @abc.abstractmethod
    def create_toy(self):
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self):
        pass

    @abc.abstractmethod
    def create_candy(self):
        pass


class ChristmasItemFactory(ItemFactory):
    """
    Christmas Item Factory.
    """

    def create_toy(self, **kwargs):
        """
        Create a Santa's Workshop.
        """
        return SantasWorkshop(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """
        Create a Stuffed Animal.
        """
        return Reindeer(**kwargs)

    def create_candy(self, **kwargs):
        """
        Create a Candy.
        """
        return CandyCanes(**kwargs)


class HalloweenItemFactory(ItemFactory):
    """
    Halloween Item Factory.
    """

    def create_toy(self, **kwargs):
        """
        Create a RCSpider.
        """
        return RCSpider(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """
        Create a Dancing Skeleton
        """
        return DancingSkeleton(**kwargs)

    def create_candy(self, **kwargs):
        """
        Create a Pumpkin Caramel Toffee.
        """
        return PumpkinCaramelToffee(**kwargs)


class EasterItemFactory(ItemFactory):
    """
    Easter Item Factory.
    """

    def create_toy(self, **kwargs):
        """
        Create a Robot Bunny.
        """
        return RobotBunny(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """
        Create a Easter Bunny.
        """
        return EasterBunny(**kwargs)

    def create_candy(self, **kwargs):
        """
        Create a Creme Eggs.
        """
        return CremeEggs(**kwargs)
