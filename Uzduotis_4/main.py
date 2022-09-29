"""Ketvirta testo užduotis."""

# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.

# klasė "Movie"
class Movie:
    """Klasė sukuria objektus, turinčius 3 savybes (title, director, budget) ir vieną metodą."""

    def __init__(self, title, director, budget):
        """Metodas priskiria argumentus parametrams"""
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        """Metodas grąžina True, jei biudžetas daugiau nei 100 mln."""
        return self.budget > 100000000

# objektas 1
movie_one = Movie("The Matrix", "Wachowski", 63000000)

# objektas 2
movie_two = Movie("Westworld", "Nolan", 295000000)

################################ TEST ################################

print(" Test: objektas 1'")
print(movie_one.title)
print(movie_one.was_expensive())

print("\n","Test: objektas 2'")
print(movie_two.title)
print(movie_two.was_expensive())
