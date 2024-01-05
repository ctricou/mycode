from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

class Dieopp():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)


# Make a 6-sided die..
d6 = Die()
d6opp = Dieopp()

# Your 6 sided die roll
def rolls():
    yourresults = []
    for roll_num in range(1):
        result = d6.roll_die()
        yourresults.append(result)
    print("Your roll of a 6-sided die:", yourresults)
# Opponents 6 sided die roll
    oppresults = []
    for roll_num in range(1):
        result = d6opp.roll_die()
        oppresults.append(result)
    print("Computer's roll of a 6-sided die:", oppresults)
# If statement announcing winner
    if yourresults > oppresults:
        print("You are the winner.")
    elif yourresults == oppresults:
        print("You have tied, roll again.")
    else:
        print("The computer has won.")
rolls()