"""
Создайте свой произвольный класс и в нём помимо обычных методов и атрибутов
создайте несколько статических методов и методов класса.
Продемонстрируйте их работу.
"""


class Films(object):
    DIRECTORS = 0
    TOTAL_RATING = None

# Magic Methods
    def __init__(self, director, year, rating):
        Films.DIRECTORS += 1
        self.name_of_director = director
        self.year_of_production = year
        self.rotten_tomatoes_rating = rating
        if self.rotten_tomatoes_rating >= 10:
            Films.TOTAL_RATING = 'Good'

    def __str__(self):
        return f'({self.name_of_director}, {self.year_of_production}' \
               f', {self.rotten_tomatoes_rating})'

# Static Methods
    @staticmethod
    def movement_cinema():
        print('Dogme 95 ')

    @staticmethod
    def add_year(year):
        return 'year ' + str(year)


# Class Methods
    @classmethod
    def country_cinema(cls):
        print('Country: Denmark, Number of directors: ', cls.DIRECTORS)

    @classmethod
    def total_rating(cls):
        print('Rating: ', cls.TOTAL_RATING)

# Instance Methods
    def age(self):
        age = 2023 - self.year_of_production
        print('Age: ', age)

    def add_year1(self):
        add_year = self.add_year(self.year_of_production)
        print(add_year)


a = Films('Trier', 2000, 10)
b = Films('Vinterberg', 1999, 11)
print('Appeal magic method via objects a, b: ')
print(a.__str__(), b.__str__())
print('Appeal static method via class: ')
Films.movement_cinema()
print('Appeal static method via objects a, b: ')
a.movement_cinema()
b.movement_cinema()
print('Appeal class method via objects a, b: ')
a.country_cinema()
b.country_cinema()
a.total_rating()
b.total_rating()
print('Appeal instance method via objects a, b: ')
a.age()
b.age()
a.add_year1()
b.add_year1()
