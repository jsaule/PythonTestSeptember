"""Antra testo užduotis."""

# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "get_user_average_age" - kaip argumentą priims "users" sąrašą ir
# duoto sąrašo atveju grąžins visų vartotojų amžiaus vidurkį kaip skaičių,
# suapvalintą iki artimiausio sveikojo skaičiaus.

# 2. funkcija "get_users_names" - kaip argumentą priims sąrašą ir duoto sąrašo
# atveju grąžins sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka,
# pvz. ['Alex John', 'Ann Smith', ...].

users = [
  { 'id': '1', 'name': 'John Smith', 'age': 20 },
  { 'id': '2', 'name': 'Ann Smith', 'age': 24 },
  { 'id': '3', 'name': 'Tom Jones', 'age': 31 },
  { 'id': '4', 'name': 'Rose Peterson', 'age': 17 },
  { 'id': '5', 'name': 'Alex John', 'age': 25 },
  { 'id': '6', 'name': 'Ronald Jones', 'age': 63 },
  { 'id': '7', 'name': 'Elton Smith', 'age': 16 },
  { 'id': '8', 'name': 'Simon Peterson', 'age': 30 },
  { 'id': '9', 'name': 'Daniel Cane', 'age': 51 },
]

# 1. funkcija "get_user_average_age"
def get_user_average_age(people):
    """GrąžinA visų vartotojų amžiaus vidurkį kaip skaičių, suapvalintą iki artimiausio sveikojo skaičiaus."""
    
    avg = 0    
  
    for person in people:
      if person['age']:
        avg += person['age'] / len(people)

    return round(avg)

# 2. funkcija "get_users_names"
def get_users_names(persons):
   """Grąžina sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka."""
   
   name_list = [persons['name'] for persons in persons if persons['name']]

   return sorted(name_list) 

################################ TEST ################################

print(" Test: 1. funkcija 'get_user_average_age'")
average_age = get_user_average_age(users)
print(average_age)

print("\n","Test: 2. funkcija 'get_users_names'")
names = get_users_names(users)
print(names)

