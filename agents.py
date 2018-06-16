class Agent(object):
    def __init__(self, endowment1, endowment2, preference1, preference2):
        """
        Agents are characterized by their allocations and preferences
        of goods 1 and 2. Economists usually call the starting value of
        a good an "endowment".
        The preference variables should be between 0 and 1.
        """
        self.good1 = max(0, endowment1)
        self.good2 = max(0, endowment2)
        self.pref1 = preference1
        self.pref2 = preference2

    @property
    def utility(self):
        """
        We'll use the Cobb-Douglas utility function for our model.
        """
        return pow(self.good1, self.pref1) * pow(self.good2, self.pref2)

    # The allocation property is just syntactic sugar that lets us assign
    # allocations using tuples a little more cleanly.
    @property
    def allocation(self): return (self.good1, self.good2)

    @allocation.setter
    def allocation(self, values): self.good1, self.good2 = values

    def demand(self, price):
        alpha = self.pref1 / (self.pref1 + self.pref2)
        quantity1 = alpha * (price * self.good1 + self.good2) / price
        quantity2 = price * quantity1 * self.pref2 / self.pref1
        return (quantity1, quantity2)

    # We need to define comparison operators in order to sort the
    # agents based on utility. I always prefer to define all of them
    # if I need to define any.
    def __gt__(self, other): return self.utility > other

    def __lt__(self, other): return self.utility < other

    def __eq__(self, other): return self.utility == other

    def __ge__(self, other): return self.utility >= other

    def __le__(self, other): return self.utility <= other

    def __ne__(self, other): return self.utility != other

    # We need to define multiplication and addition operators
    # in order to use Norvig's normalize function.
    def __mul__(self, other):
        self.good1 *= other
        self.good2 *= other
        return self

    def __radd__(self, other):
        return other + self.good1 + self.good2


class BargainingAgent(Agent):
    def __init__(self, endowment1, endowment2, preference1, preference2, cha):
        Agent.__init__(self, endowment1, endowment2, preference1, preference2)
        self.charisma = cha

    # We need to define comparison operators in order to sort the
    # agents based on charisma. I always prefer to define all of them
    # if I need to define any.
    def __gt__(self, other): return self.charisma > other

    def __lt__(self, other): return self.charisma < other

    def __eq__(self, other): return self.charisma == other

    def __ge__(self, other): return self.charisma >= other

    def __le__(self, other): return self.charisma <= other

    def __ne__(self, other): return self.charisma != other