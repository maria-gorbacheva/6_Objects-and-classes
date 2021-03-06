class Animals:
    name = 'Без имени'
    weight = 0.1  # in kg
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, food):
        self.weight += food
        return self

    def voice_(self):
        print(f'{self.name} {self.voice}')


class Birds(Animals):
    eggs = 0

    def get_eggs(self, eggs):
        self.eggs = eggs


class Mammals(Animals):
    milk = 0

    def get_milk(self, milk):
        self.milk = milk


class Geese(Birds):
    voice = 'гагочет'


class Cows(Mammals):
    voice = 'мычит'


class Sheep(Animals):
    wool = 2  # in kg
    voice = 'блеет'

    def get_wool(self, wool):
        self.wool = wool


class Chicken(Birds):
    voice = 'кококо'


class Goats(Mammals):
    voice = 'млеет'


class Ducks(Birds):
    voice = 'крякает'


animals_dict = {'goose_grey': Geese('Серый', 3),
                'goose_white': Geese('Белый', 4),
                'cow_manka': Cows('Манька', 350),
                'sheep_barashek': Sheep('Барашек', 350),
                'sheep_curly': Sheep('Кудрявый', 170),
                'chicken_koko': Chicken('Коко', 2),
                'chicken_kukareku': Chicken('Кукареку', 2.5),
                'goat_roga': Goats('Рога', 80),
                'goat_kopita': Goats('Копыта', 76),
                'duck_kriakva': Ducks('Кряква', 5)
                }


def feed(animals, class_type, food):
    for animal in animals.values():
        if isinstance(animal, class_type):
            animal.eat(food)
            print(f'Накормили всех {class_type}')


def eggs(animals, class_type, eggs_num):
    for animal in animals.values():
        if isinstance(animal, class_type):
            animal.get_eggs(eggs_num)
    return animals


animals_dict['cow_manka'].get_milk(10)

animals_dict['sheep_barashek'].get_wool(3)

animals_dict['goat_roga'].get_milk(5)

animals_dict['duck_kriakva'].get_eggs(6)


def total_weight(dictionary):
    weight = 0
    for item in dictionary.values():
        weight += item.weight
    print(f'Суммарный вес: {weight}')


def heaviest_animal(dictionary):
    """
    Function finds out the heaviest animal in dictionary, prints its name and its weight.
    Weakness: if there are two or more animals with the same max weight,
    the function returns the fist it meets
    :param dictionary: must be a dictionary with values of Animals class
    :return: a cortege: (<'animal's name'>, <animal's weight>)
    """
    max_animal_name = ''
    max_weight = 0
    for animal in dictionary.values():
        if animal.weight > max_weight:
            max_weight = animal.weight
            max_animal_name = animal.name
    print(f'Животное с максимальным весом: {max_animal_name}\nВес: {max_weight}')
    return max_animal_name, max_weight


heaviest_animal(animals_dict)
total_weight(animals_dict)
animals_dict['goose_grey'].voice_()