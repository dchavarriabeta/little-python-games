import random

def guessing(value):
  radon_number = random.randint(1, value)
  guess_value = 0

  while guess_value != radon_number:
    guess_value = int(input(f'Inserte un valor entre 1 y {value}'))

    if guess_value > radon_number:
      print('Es un numero muy alto ')
    elif guess_value < radon_number:
      print('Es un numero muy bajo ')
  
  print('Lo lograste!!')

guessing(10)