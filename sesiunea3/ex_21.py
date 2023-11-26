import random
dice_roll = random.randint(1,6)

input_user = int(input("DAti cu zarul "))

if input_user > 0 and input_user <=6:
    print("ZAR VALID")
    if input_user < dice_roll :
        print(f"Ai ales {input_user} a fost {dice_roll}"  )
    elif input_user > dice_roll:
        print(f"Ai ales {input_user} a fost {dice_roll}")
    else:
        print("Felicitari")
else:
    print("Introdu un nr valid")
