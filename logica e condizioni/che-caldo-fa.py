#
# caldissimo 35 caldo 28 ok 18 freddo 16 freddissimo
#
#
temperatura = int(input("inserisci la temperatura\n"))

if temperatura > 35:
    print("caldissimo!!!")
else:
    if temperatura > 28:
        print("che caldo!")
    else:
        if temperatura > 18:
            print("ok")
        else:
            if temperatura > 16:
                print("che freddo")
            else:
                print("freddissimo!")

