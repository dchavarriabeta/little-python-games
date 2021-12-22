import random

def play():
  user = input('Selecciona entre: "R" para roca, "T" para tijeras y "P" para papel')
  computer_random_choice = random.choice(['r', 'p', 't'])

  if(user == computer_random_choice):
    print(computer_random_choice)
    return print('Empate')

  if getWinner(user, computer_random_choice):
    print(computer_random_choice)
    return print('Tu ganas')

  print(computer_random_choice)
  return print('Tu pierdes :(')

def getWinner(player, opponent):
  if(player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
    return True

play()