import random

def start_game():
    guess_num = random.randint(1, 50)
    
    while True:
     user_num = int(input("Enter the number : "))
    
     if user_num == guess_num:
        print("You Won. Game is over!")
        break
     elif user_num > guess_num:
        print("Guess is Too High")
     else:
        print("Guess is Too Low")
        
    print("Thank You for Playing the Game !!!")

start_game()