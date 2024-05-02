from sum import sum
from rest import rest
from mult import mult
from div import div
from pot import pot
from mod import mod



def game():
  score = 0
  while True:
    print('======== Menu ========'
    '\n1. Add'
    '\n0. Exit')
    option = int(input('\nChoice an option: '))
    if option == 0:
      break
    num_1 = int(input('Enter first number: '))
    num_2 = int(input('Enter second number: '))
    answer = float(input('Enter you answer: '))
    
    if option == 1:
      result = sum(num_1, num_2)
      if result == answer:
        score += 1
        print('Correct!!')
      else:
        print('Incorrect')

    elif option == 2:
      result = rest(num_1, num_2)
      if result == answer:
        score += 1
        print('Correct!!')
      else:
        print('Incorrect')

    elif option == 3:
      result = mult(num_1, num_2)
      if result == answer:
        score += 2
        print('Correct!!')
      else:
        print('Incorrect')

    elif option == 4:
      if num_2 != 0:
        result = div(num_1, num_2)
        if result == answer:
          score += 2
          print('Correct!!')
      else:
        print('Incorrect')

    elif option == 5:
      result = pot(num_1, num_2)
      if result == answer:
        score += 4
        print('Correct!!')
      else:
        print('Incorrect')

    elif option == 6:
      if num_2 != 0:
        result = mod(num_1, num_2)
        if result == answer:
          score += 4
          print('Correct!!')
      else:
        print('Incorrect')

  
  print(f'======== Game Over ========'
  f'\nYou score is {score}'
  '\nKeep going!')
game()
