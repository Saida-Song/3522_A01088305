"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        """
        Initialize an Auctioneer.
        """
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self._highest_bidder = None
        self.bidders.clear()
        self._highest_bid = 0

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self.bidders:
            if self._highest_bidder is not bidder:
                bidder(self)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid > self._highest_bid:
            if self._highest_bidder is not None:
                print(f"{bidder.name} bidded {bid} in response to "
                      f"{self._highest_bidder.name}'s bid of {self._highest_bid}")
            else:
                print(f"{bidder.name} bidded {bid} in response to "
                      f"Starting bid's bid of {self._highest_bid}")
            self._highest_bidder = bidder
            self._highest_bid = bid
            self._notify_bidders()

    def start_bidding(self, start_price):
        """
        Start bidding with the start price
        :param start_price: a float
        """
        self._highest_bid = start_price
        self._notify_bidders()

    def check_if_fail_auction(self):
        """
        Check if the auction failed.
        :return: a boolean
        """
        return self._highest_bidder is None

    @property
    def highest_bid(self):
        """
        Return the highest bid.
        :return: a float
        """
        return self._highest_bid

    @property
    def highest_bidder_name(self):
        """
        Return the name of the highest bid bidder.
        :return: a string
        """
        return self._highest_bidder.name


class Bidder:

    def __init__(self, name, budget=100, bid_probability=0.35, bid_increase_perc=1.1):
        """
        Initialize a bidder that requires several bidder info.
        :param name: a string
        :param budget: a float
        :param bid_probability: a float
        :param bid_increase_perc: a float
        """
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer):
        """
        Callable function of the Bidder.
        :param auctioneer: an Auctioneer
        """
        bid_or_not = random.random()
        if bid_or_not < self.bid_probability:
            bid_price = auctioneer.highest_bid * self.bid_increase_perc
            if bid_price <= self.budget:
                self.highest_bid = bid_price
                auctioneer.accept_bid(bid_price, self)

    def get_highest_bid(self):
        """
        Return the highest bid of the bidder.
        :return: a float
        """
        return self.highest_bid

    def get_budget(self):
        """
        Return the budget of the bidder.
        :return: a float
        """
        return self.budget

    def get_bid_prob(self):
        """
        Return the bid probability of the bidder.
        :return: a float
        """
        return self.bid_probability

    def get_increase_perc(self):
        """
        Return the percentage of increasing bid.
        :return: a float
        """
        return self.bid_increase_perc

    def __str__(self):
        """
        String method of the bidder.
        :return: a string
        """
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self.auctioneer = Auctioneer()
        for bidder in bidders:
            self.auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print(f"\nAuctioning {item} starting at {start_price}")
        self.auctioneer.start_bidding(start_price)
        if self.auctioneer.check_if_fail_auction():
            print("The auction failed! No one throw a bid.")
            return
        print(f"\nThe winner of the auction is: {self.auctioneer.highest_bidder_name}"
              f" at ${self.auctioneer.highest_bid}\n")

        print("Highest Bids Per Bidder")
        highest_bids = {bidder: bidder.highest_bid for bidder in self.auctioneer.bidders}
        for name, bid in highest_bids.items():
            print(f"Bidder: {name}    Highest Bid: {bid}")


def main():
    """
    Driver function of the program.
    """
    bidders = []
    while True:
        print("Welcome!\nWould you like to use hardcoded bidders or new custom bidders?\n"
              "1. Hardcoded bidders\n2. Add Custom Bidders")
        menu_input = input("please enter the number: ")
        if menu_input == "1":
            # Hardcoding the bidders.
            bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
            bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
            bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
            bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
            bidders.append(Bidder("Scott", 4000, random.random(), 2))
            break
        elif menu_input == "2":
            custom_bidders_num = input("How many bidders do you want to add?: ")
            try:
                for i in range(int(custom_bidders_num)):
                    bidder_name = input(f"The name of the bidder{i}: ")
                    bidder_budget = int(input(f"The budget of the bidder{i}: "))
                    bidders.append(Bidder(bidder_name, bidder_budget, random.random(), random.random() + 1))
                break
            except Exception as e:
                print(e)
        else:
            print("Invalid Input. Please try again")

    print("-" * 20, "The list of bidders")
    for bidder in bidders:
        print(f"Name: {bidder}, Budget: {bidder.get_budget()}, Probability of bid: {bidder.get_bid_prob()}"
              f", Percentage of increase: {bidder.get_increase_perc()}")

    while True:
        try:
            bid_item_name = input("Please enter the name of the bid item: ")
            bid_item_start_price = float(input("Please set the start price of the item: "))
            print("\n\nStarting Auction!!")
            print("------------------")
            my_auction = Auction(bidders)
            my_auction.simulate_auction(bid_item_name, bid_item_start_price)
            break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
