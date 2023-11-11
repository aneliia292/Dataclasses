from dataclasses import dataclass

@dataclass
class GoodIfrit:
    high: int
    name: str
    happy: int


    def change_goodness(self, mood):
        x = self.happy + mood
        if x < 0:
            x = 0
        self.happy = x


    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('ERROR')
        return (GoodIfrit(self.high + other, self.name, self.happy))

    def arguments(self, param):
        return f'{param * self.happy // self.high}'


    def __str__(self):
        return f'Good Ifrit {self.name}, height {self.high}, goodness {self.happy}'


    def __eq__(self, other):
        if not isinstance(other, GoodIfrit):
            raise TypeError('ERROR')
        return (self.happy, self.high, self.name) == (other.happy, other.high, other.name)


    def __gt__(self, other):
        if not isinstance(other, GoodIfrit):
            raise TypeError('ERROR')
        if self.happy > other.happy:
            if self.high > other.high:
                if self.name > other.name:
                    return True
        return False


    def __ge__(self, other):
        if not isinstance(other, GoodIfrit):
            raise TypeError('ERROR')
        if self.happy < other.happy:
            if self.high < other.high:
                if self.name < other.name:
                    return True
        return False


y = GoodIfrit(20, 'Вася', 10)
# y.change_goodness(-50)
print(y)
print(y + 5)
print(y.arguments(40))
dt = GoodIfrit(20, 'Петя', 20)
print(dt == y)