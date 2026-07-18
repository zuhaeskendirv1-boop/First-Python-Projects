import random
while True:
    choice = input("Rock, paper, scissors? (r/p/s): ")

    if choice != 'r' and choice != 'p' and choice != 's':
        print("Invalid choice")
    else:
        number = (random.randint(1, 3))
        if number == 1:
            print("Computer chose rock🪨")
            if choice == 'r':
                print("You chose rock🪨")
                print("Draw! Try again")
            elif choice == 'p':
                print("You chose paper📃")
                print("You won! Congrats!")
            else:
                print("You chose scissors✂️")
                print("You lose!")
            ans = input("Continue? (y/n): ")
            if ans == 'n':
                break;
        elif number == 2:
            print("Computer chose paper📃")
            if choice == 'p':
                print("You chose paper📃")
                print("Draw! Try again")
            elif choice == 's':
                print("You chose scissors✂️")
                print("You won! Congrats!")
            else:
                print("You chose rock🪨")
                print("You lose!")
            ans = input("Continue? (y/n): ")
            if ans == 'n':
                break;
        else:
            print("Computer chose scissors✂️")
            if choice == 's':
                print("You chose scissors✂️")
                print("Draw! Try again")
            elif choice == 'r': 
                print("You chose rock🪨")
                print("You won! Congrats!")
            else:
                print("You chose paper📃")
                print("You lose!")
            ans = input("Continue? (y/n): ")
            if ans == 'n':
                break;

    