import random,playsound
def win_music():
    """This function is for play winning music"""
    playsound.playsound("win.mp3")

def lose_music():
    """This function is for play winning music"""
    playsound.playsound("lose.mp3")

def draw_music():
    """This function is for play winning music"""
    playsound.playsound("draw.mp3")

print("\n\n-----------------------Welcome to Snake Water Gun Game------------------------")
print("Caution : You Can only attempts 10 times.\n")
attempts=0
my_point=0
com_point=0
while(attempts<10):
    list=["s","w","g"]
    rand=random.choice(list)
    print("Choose 1 Between Theese Three....\n s(Snake)\n w(Water)\n g(Gun)\n")
    my_choice=input("Enter Your Choice : \n")
    if my_choice == rand:
        print(f"Your choice is {my_choice} and Computer's Choice is {rand}")
        print("This round is Draw")
        draw_music()
    elif my_choice=="s" and rand =="w":
        my_point +=1
        print(f"Your choice is {my_choice} and Computer's Choice is {rand}")
        print(f"You won This Round.\nYou get 1 Point.\nYour point is : {my_point} & computer point is : {com_point}")
        win_music()
    elif my_choice=="w" and rand =="s":
        com_point += 1
        print(f"Your choice is {my_choice} and Computer's Choice is {rand}")
        print(f"You lose This Round.\nComputer get 1 Point.\nYour point is : {my_point} & computer point is : {com_point}")
        lose_music()

    elif my_choice=="w" and rand =="g":
        my_point += 1
        print(f"Your choice is {my_choice} and Computer's Choice is {rand}")
        print(f"You won This Round.\nYou get 1 Point.\nYour point is : {my_point} & computer point is : {com_point}")
        win_music()
    elif my_choice=="g" and rand =="w":
        com_point += 1
        print(f"Your choice is {my_choice} and Computer's Choice is {rand}")
        print(f"You lose This Round.\nComputer get 1 Point.\nYour point is : {my_point} & computer point is : {com_point}")
        lose_music()

    elif my_choice=="g" and rand =="s":
        my_point += 1
        print(f"Your choice is {my_choice} and Computer's Choice is {rand}")
        print(f"You won This Round.\nYou get 1 Point.\nYour point is : {my_point} & computer point is : {com_point}")
        win_music()
    elif my_choice=="s" and rand =="g":
        com_point += 1
        print(f"Your choice is {my_choice} and Computer's Choice is {rand}")
        print(f"You lose This Round.\nComputer get 1 Point.\nYour point is : {my_point} & computer point is : {com_point}")
        lose_music()
    else:
        print("Invalid input\n")
    attempts+=1
    print(f"You have left {10-attempts} attempts")
    if attempts==10:
        print("Game is Over! \n")
print(f"Your Final Point is : {my_point} \n")
print(f"Computer Final Point is : {com_point} \n")
if my_point>com_point:
    print("Congratulations !!!!! You Won this game.\n")
    win_music()
else:
    print("You lose!!!!!!!!Better luck next time.....\n")
    lose_music()
print("-----------------------Thanks for Playing.-----------------------")
