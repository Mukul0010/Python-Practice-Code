
# Write a python program which will keep addding a stream of numbers inputted by the user. The adding stops as soom as user presses "q" key on the keyboard.

sum = 0
while (True):
    UserInput = input("Enter the item price or press q to quit: \n")

    if (UserInput != 'q'):

        sum = sum + int(UserInput)
        print(f"Order total so far: {sum}]")

    else:
        print(f"Yor Bill total is {sum}. Thanks for shopping with us")

        break
