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
        :param kwargs: dict
        :return: SantaWorkshop
        """
        return SantasWorkshop(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """
        Create a Stuffed Animal.
        :param kwargs: dict
        :return: Reindeer
        """
        return Reindeer(**kwargs)

    def create_candy(self, **kwargs):
        """
        Create a Candy.
        :param kwargs: dict
        :return: Candy
        """
        return CandyCanes(**kwargs)


class HalloweenItemFactory(ItemFactory):
    """
    Halloween Item Factory.
    """

    def create_toy(self, **kwargs):
        """
        Create a RCSpider.
        :param kwargs: dict
        :return: RCSpider
        """
        return RCSpider(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """
        Create a Dancing Skeleton
        :param kwargs: dict
        :return: Skeleton
        """
        return DancingSkeleton(**kwargs)

    def create_candy(self, **kwargs):
        """
        Create a Pumpkin Caramel Toffee.
        :param kwargs: dict
        :return: PumpkinCaramelToffee
        """
        return PumpkinCaramelToffee(**kwargs)


class EasterItemFactory(ItemFactory):
    """
    Easter Item Factory.
    """

    def create_toy(self, **kwargs):
        """
        Create a Robot Bunny.
        :param kwargs: dict
        :return: RobotBunny
        """
        return RobotBunny(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        """
        Create a Easter Bunny.
        :param kwargs: dict
        :return: EasterBunny
        """
        return EasterBunny(**kwargs)

    def create_candy(self, **kwargs):
        """
        Create a Creme Eggs.
        :param kwargs: dict
        :return: CremeEggs
        """
        return CremeEggs(**kwargs)
