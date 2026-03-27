target = 100
for i in range(6):
    user=int(input())
    guess=target-user
    
    if guess == 0:
        print("Excellent")
    elif abs(guess)<=10:
        print("Good")
    elif guess >=10:
        print("Low")
    else:
        print("High")