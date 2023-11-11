from dataclasses import dataclass
@dataclass
class AirData:
    high: int
    clouds: int
    color: str

    def change_height(self, value):
        c = self.clouds + value
        if c < 0:
            c = 0
        self.clouds = c

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('ERROR')
        self.clouds += other
        self.high += other // 5
        return AirData(self.high, self.clouds, self.color)

    def opacity(self, degree):
        self.degree = self.high // degree * self.clouds
        print(f'Прозрачность облаков: {self.degree}')


    def __str__(self):
        return f'The AirCastle at an altitude of {self.high} meters is {self.color} with {self.clouds} clouds'


    def __eq__(self, other):
        if not isinstance(other, AirData):
            raise TypeError
        return self.clouds == other.clouds


    def __lt__(self, other):
        if not isinstance (other, AirData):
            raise TypeError
        return self.clouds < other.clouds


    def __le__(self, other):
        if not isinstance (other, AirData):
            raise TypeError('ERROR')
        return self.clouds <= other.clouds




castle = AirData(1, 3, 'green')
castle1 = AirData(1, 4, 'green')

print(castle)
castle.change_height(5)
castle.change_height(-10)
print(castle)
castle = castle + 8
print(castle)
castle.opacity(2)
print(castle)
print(castle == castle1)
print(castle <= castle1)
print(castle < castle1)