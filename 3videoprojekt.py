user_input = int(input("Adj meg egy háromjegyű egész számot!\n> "))

if user_input // 100 < 1 or user_input // 100 > 9:
    print("Nem háromjegyű számot adtál meg!")

else:
    digit1 = user_input // 100
    digit2 = (user_input % 100) // 10
    digit3 = (user_input % 100) % 10


    if digit1**3 + digit2**3 + digit3**3 == user_input:
        print(f"{user_input} egy Armstrong szám!")
    else:
        print(f"{user_input} nem egy Armstrong szám!")
