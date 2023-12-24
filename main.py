import random
a = 1
rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while a==1:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice = random.randint(0, 2)
    if user_choice==0:
        print(rock)
        print('Computer\'s Choice')

        if computer_choice==0:
            print(rock)
            print("draw")
        elif computer_choice==1:
            print(paper)
            print("you lose")
        elif computer_choice==2:
            print(scissors)
            print("you win")
    elif user_choice==1:
        print(paper)
        print('Computer\'s Choice')
        if computer_choice == 1:
            print(paper)
            print("draw")
        elif computer_choice == 2:
            print(scissors)
            print("you lose")
        elif computer_choice == 0:
            print(rock)
            print("you win")
    elif user_choice==2:
        print(scissors)
        print('Computer\'s Choice')
        if computer_choice == 2:
            print(scissors)
            print("draw")
        elif computer_choice == 0:
            print(rock)
            print("you lose")
        elif computer_choice == 1:
            print(paper)
            print("you win")
    else:
        print("Please Choose a correct option.")