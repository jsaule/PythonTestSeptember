"""Trečia testo užduotis."""

# Duotas "audi" žodynas.

# Parašykite funkciją "get_dict_values", kuri:
# * Turės 'docstring' tipo komentarą apie tai, ką ji atlieka.
# * Nekeis žodyno, priimto kaip argumento, savo viduje.
# * Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).

from webbrowser import get


audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

# funkcija "get_dict_values"
def get_dict_values(all):
  """Grąžina sąrašą su visomis jo reikšmėmis (values)."""

  result = list(all.values())

  return result

################################ TEST ################################

print(" Test: 1. funkcija 'get_dict_values'")

values_list = get_dict_values(audi)
print(values_list)