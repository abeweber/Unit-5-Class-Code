def blackjack(a,b,c):
    valid_numbers = 1<=a<=11 and 1<=b<=11 and 1<=c<=11
    if not valid_numbers:
        print("Error")
        return
    sum = a+b+c
    if sum <= 21:
        print(sum)
    elif sum >= 21 and (a == 11 or b == 11 or c == 11):
        print(sum - 10)
    elif sum > 21:
        print("BUST")

blackjack(a=5, b=6,c=8)

def warrior(name,color):
    print(f"{name} the fierce, {color} eyed warrior")

warrior(name="Abe",color="blue")