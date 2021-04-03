userName = input("User:")
userPass = input("Password:")
apple = 10
banana = 12
orange = 15
if userName == "Paramee" and userPass == "1234":
    print("------Fruits-Shop-------")
    print("Item--------------------------Price/Each")
    print("1 Apple-------------------------", apple, "THB")
    print("2 Banana------------------------", banana, "THB")
    print("3 Orange------------------------", orange, "THB")
    print("Please Select Number")
    e1 = int(input(">>"))
    if e1 == 1:
        quantity = int(input("Quantity to buy:"))
        print("Total price:",apple*quantity, "THB")
    elif e1 == 2:
        quantity = int(input("Quantity to buy:"))
        print("Total price:",banana*quantity, "THB")
    elif e1 == 3:
        quantity = int(input("Quantity to buy:"))
        print("Total price:",orange*quantity, "THB")
    else:
        print("Error")
else:
    print("Error")