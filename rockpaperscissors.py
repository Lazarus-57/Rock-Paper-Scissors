import random
import time

print("Let's Play!")

while(True):
    user_choice=input("Enter your choice [Rock,Paper or Scissors]: ").title()
    x=['Rock', 'Paper', 'Scissors']
    celebrations="YOU WON!"
    condolences="YOU LOST :("
    time.sleep(0.75)
    computer_choice=random.choice(x)
    print("Computer chose :", computer_choice)

    
    time.sleep(1)
    if user_choice==computer_choice:
        print('You tied!')
    elif user_choice=="Rock":
        if computer_choice=="Paper":
            print(condolences)
        else:
            print(celebrations)
    elif user_choice=="Paper" :
        if computer_choice=='Rock':
            print(celebrations)
        else:
            print(condolences)
    elif user_choice=="Scissors":
        if computer_choice=='Rock':
            print(condolences)
        else:
            print(celebrations)
    
    time.sleep(0.75)
    play_again=input('Shall we dance again?(y/n)').lower()
    if play_again!='y':
        print('Goodbye!')
        break

