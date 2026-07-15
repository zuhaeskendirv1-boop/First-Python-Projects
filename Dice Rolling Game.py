import random
while True:
    choice = input("Do you want to roll a dice? (y/n): ")
    if choice == 'n':
        print("Thanks for using our app!")
        break
    else:
        num = input("How many dices do want to roll? (1-100): ")
        
        rolls = [random.randint(1, 6) for _ in range(int(num))]
        
        print(rolls)
        
        
        #if num == '1':
         #   print(random.randint(1, 6))
        #elif num == '2':
         #   print(random.randint(1,6), random.randint(1,6))
        #elif num == '3':
         #   print(random.randint(1,6), random.randint(1,6), random.randint(1,6))
        #else:
         #   print(random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6))


    