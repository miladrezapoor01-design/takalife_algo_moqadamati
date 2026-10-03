

password = input("ramz ra vared kon: ")

if password != "4321":
    print("ramz qalat")
else:
    balance = int(input("mojodi ra vared kon :  "))
    withdraw = int(input("mablaqe bardasht :  "))


    if withdraw <= 0:
        print("mablaq bayad bishtar az sefr bashad")

    

    elif withdraw > balance:
        print("mojodi kafi nist")

    else:
        balance = balance - withdraw
        print("bardasht anjam shod")
        print("mojodi jadid : ", balance, "toman")
        