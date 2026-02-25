 

user_name = input("Enter your name : ")

total = 0
count = 0
while True:
    if count == 3:
        break

    price = input("Enter the price : ")

    if price.isdigit() and int(price) > 0:
        total += int(price)
        count += 1

    else:
        print("Invalid input, please try again!")
        continue

print("The Total amount is :", total)

discount = input("Wants to apply a membership discount (y/n): ").strip().lower()

if discount == "y":
    dis_rate = 0.1  # 10%
    discount_amount = total * dis_rate
    total = total - discount_amount
    print("Your Total is :", total)

else:
    print("Thanks for purchasing the items")
    print("Your Total is :", total)
 