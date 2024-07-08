import random

your_score = 0
computer_score = 0
counter = 1
choice = ['snake', 'water', 'gun']
print(choice)

while counter <= 3:
    choose = int(input('''Enter "0" for snake
    Enter "1" for water
    Enter "2" for gun
                            '''))
    your_choice = choice[choose]
    computer_choice = random.choice(choice)
    print(f"Your choice: {your_choice}")
    print(f"Computer choice: {computer_choice}")
    
    if your_choice == computer_choice:
        your_score += 1
        computer_score += 1
        print("It's a draw....")
    elif (your_choice == 'snake' and computer_choice == 'water') or \
         (your_choice == 'water' and computer_choice == 'gun') or \
         (your_choice == 'gun' and computer_choice == 'snake'):
        your_score += 1
        print("You win!!!")
    else:
        computer_score += 1
        print("You lose <<<<>>>>")
    
    print('Your score:', your_score)
    print('Computer score:', computer_score)
    print('Counter:', counter)
    
    if counter < 3:
        tryagain = int(input('Enter "1" to try again: '))
        if tryagain == 1:
            counter += 1
        else:
            break
    else:
        break

if your_score > computer_score:
    print("You win!!!!!")
else:
    print("You lose")
