import random


class DIE:
    """Represent a die with a configurable number of sides."""

    def __init__(self, sides=6):
        """Initialize the die with the given number of sides."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides."""
        print(random.randint(1, self.sides))


# Create a 6-sided die and roll it 10 times.
die_6 = DIE()

print("6-sided die:")
for _ in range(10):
    die_6.roll_die()


# Create a 10-sided die and roll it 10 times.
die_10 = DIE(10)

print("\n10-sided die:")
for _ in range(10):
    die_10.roll_die()


# Create a 20-sided die and roll it 10 times.
die_20 = DIE(20)

print("\n20-sided die:")
for _ in range(10):
    die_20.roll_die()
