from tkinter import *
import time
from random import random, randint
from math import hypot
from random import shuffle


class City:
    def __init__(self, name: str, coords: tuple):
        self._name = name
        self._x, self._y = coords

    @property
    def name(self):
        return self._name

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @staticmethod
    def distance(city1, city2):
        return hypot(city2.x - city1.x, city2.y - city1.y)

    def __repr__(self):
        return f'{self._name}'


class Country:
    def __init__(self):
        self._cities = []

    def add(self, x):
        if isinstance(x, list):
            self.cities.extend(x)
        elif isinstance(x, City):
            self.cities.append(x)
        else:
            assert False, "Wrong type"

    @property
    def cities(self):
        return self._cities


class Route:
    def __init__(self, cities, shuffled=False):
        self._genes = cities[:]
        if not shuffled:
            shuffle(self._genes)
        self._fitness = None
        self.chance = None


    @property
    def fitness(self):
        distances = (City.distance(self._genes[i], self._genes[i + 1]) for i in range(-1, len(self._genes) - 1))
        self._fitness = 10 / sum(distances)
        return self._fitness

    @property
    def raw_fitness(self):
        return self._fitness

    @property
    def genes(self):
        return self._genes

    def copy(self):
        clone = Route(self._genes, shuffled=True)
        clone._fitness = self.raw_fitness
        clone.chance = None
        return clone

    def __repr__(self):
        return f'<Route ({self._fitness})>'

    def __str__(self):
        return '->'.join(repr(city) for city in self._genes)




def selection(pop):
    i = -1
    rand = random()
    while rand > 0:
        i += 1
        rand -= pop[i].chance
    return pop[i]


def mutation(population, rate):
    for chromosome in population:
        if random() < rate:
                r1 = randint(0, len(chromosome.genes) - 1)
                r2 = randint(0, len(chromosome.genes) - 1)
                chromosome.genes[r1], chromosome.genes[r2] = chromosome.genes[r2], chromosome.genes[r1]


def crossover(chromosome1, chromosome2):
    end = randint(0, len(chromosome1.genes))
    start = randint(0, end)
    section = chromosome1.genes[start:end]
    offspring_genes = list(gene if gene not in section else None for gene in chromosome2.genes)
    g = (x for x in section)
    for i, x in enumerate(offspring_genes):
        if x is None:
            offspring_genes[i] = next(g)
    offspring = Route(offspring_genes, shuffled=True)

    return offspring


class GeneticAlgorithm:
    """Создание начальной популяции"""
    def __init__(self, size, mutation_rate=0.01, ptype=None, args=tuple()):
        assert ptype is not None, 'Population type cannot be None'
        assert type(args) == tuple, 'Arguments must be a tuple instead of ' + str(type(args))
        self._population = [ptype(*args) for _ in range(size)]
        self._mutation_rate = mutation_rate
        self._generation = 0
        self._fittest = self._population[0]
        self.evaluation()

    def individuals(self):
        for chromosome in self._population:
            yield chromosome

    """Подсчет функции приспособленности"""
    def evaluation(self):
        fitness_sum = sum(chromosome.fitness for chromosome in self._population)
        for chromosome in self._population:
            chromosome.chance = chromosome.fitness / fitness_sum

    """Отбор (селекция)"""
    def best(self):
        return max(self._population, key=lambda k: k.fitness)

    @property
    def alltime_best(self):
        return self._fittest

    @property
    def generation(self):
        return self._generation

    def next_generation(self):
        new_population = []
        for _ in range(len(self._population)):
            chromosome1 = selection(self._population)
            chromosome2 = selection(self._population)
            new_population.append(crossover(chromosome1, chromosome2))
            mutation(new_population, self._mutation_rate)
        self._population = new_population
        self.evaluation()

    def run(self, seconds=5, reps=None):
        #print(reps)
        if reps is not None:
            assert isinstance(reps, int), 'Argument `reps` must be of integer type'
            for _ in range(reps - 1):
                pretender = self.best()
                if pretender.fitness > self._fittest.raw_fitness:
                    self._fittest = pretender.copy()

                self._generation += 1
                self.next_generation()
            pretender = self.best()
            if pretender.fitness > self._fittest.raw_fitness:
                self._fittest = pretender.copy()
            self._generation += 1
        else:
            t0 = time.time()
            while True:
                pretender = self.best()
                if pretender.fitness > self._fittest.raw_fitness:
                    self._fittest = pretender.copy()

                self._generation += 1
                if time.time() - t0 >= seconds:
                    break
                self.next_generation()




def main():
    window = Tk()
    window.title('Shortest way between cities')
    window.geometry("800x600")
    spain = Country()
    spain.add([
        City('Мадрид', (40, 3)),
        City('Барселона', (41, 2)),
        City('Валенсия', (39, 0)),
        City('Севилья', (37, 5)),
        City('Саргоса', (41, 0)),
        City('Малага', (36, 4)),
        City('Мурсия', (37, 1)),
        City('Пальма-де-Майорка', (39, 2)),
        City('Лас-Пальмос-де-Гранд-Канария', (28, 15)),
        City('Бильбао', (43, 2))
    ])

    def applytoLabel():
        n = 10
        element = ''
        for i in range(n):
           element = element + str(i+1) +'. ' + str(spain.cities[i]) + '\n'
        return element

    print(applytoLabel())

    l1 = Label(window, justify=LEFT, background="light goldenrod yellow", text="10 крупнейших городов Испаниии по численности населения:")
    l1.config(font=(10))
    l1.grid(row=0, column=0, columnspan=2, padx=20)

    l2 = Label(window, justify=LEFT, text= applytoLabel())
    l2.config(font=(8))
    l2.grid(row=1, column=0, columnspan=2, padx=30)

    #print('Cities:', end=' ')
    #print(*(city for city in spain.cities), sep=', ')
    ga = GeneticAlgorithm(100, mutation_rate=0.5, ptype=Route, args=(spain.cities,))
    ga.run(seconds=10)
    fittest = ga.alltime_best
    best_fitness = fittest.fitness

    ln = Label(window, justify=LEFT, background="light goldenrod yellow", text="Оптимальное расстояние:")
    ln.config(font=(8))
    ln.grid(padx=0)

    l3 = Label(window, justify=LEFT, text=fittest, wraplength=500)
    l3.config(font=(8))
    l3.grid(row=3, column=0, columnspan=2, padx=20)

    bf = ga.generation*5
    lf = Label(window, justify=LEFT, background="light goldenrod yellow", text="Функция приспособленности:")
    lf.config(font=(8))
    lf.grid(padx=100)

    l4 = Label(window, justify=LEFT, text=best_fitness)
    #l4 = Label(window, justify=LEFT, text=d)
    l4.config(font=(8))
    l4.grid(padx=20)

    lg = Label(window, background="light goldenrod yellow", text="Количество поколений:")
    lg.config(font=(8))
    lg.grid(padx=0)

    l5 = Label(window, justify=LEFT, text=ga.generation)
    l5.config(font=(8))
    l5.grid(padx=0)

    lw = Label(window, background="light goldenrod yellow", text="Значение оптимального расстояния в км:")
    lw.config(font=(8))
    lw.grid(padx=0)

    l6 = Label(window, justify=LEFT, text=bf)
    l6.config(font=(8))
    l6.grid(padx=0)

    #print('Best route:', fittest)
    #print('Best fitness:', best_fitness)
    #print('Generations:', ga.generation)
    window.mainloop()


if __name__ == '__main__':
    main()


