


apple_price = 90
budget = 1000
kg = int(input("Enter how much required in kg : "))
if (apple_price*kg <= budget) :
    print(" apple_price * kg  : " )
    total = apple_price * kg
    print( total)
    print(" budget - total_price  : ")

    remain_balance = budget - total
    print(remain_balance)


else :
    print(" low budget money not sufficient ! ")

