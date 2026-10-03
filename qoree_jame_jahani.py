


import random

list_temhay_1=["iran,alman,japon,bahreyn"]
list_temhay_2=["usa,mexik,hend,en"]
bazi_1=[]
bazi_2=[]
bazi_3=[]
bazi_4=[]
while True:
  
    menu_qore=input("1.qore keshi 2.exit")
    while True:
        match menu_qore:
            case "1":

              
               
                tem_1_bazi_1=random.choice(list_temhay_1)
                tem_2_bazi_1=random.choice(list_temhay_2)
                bazi_1.append(tem_1_bazi_1)
                bazi_1.append(tem_2_bazi_1)
                list_temhay_1.remove(tem_1_bazi_1)
                list_temhay_2.remove(tem_2_bazi_1)

                tem_1_bazi_2=random.choice(list_temhay_1)
                tem_2_bazi_2=random.choice(list_temhay_2)
                bazi_2.append(tem_1_bazi_2)
                bazi_2.append(tem_2_bazi_2)
                list_temhay_1.remove(tem_1_bazi_2)
                list_temhay_2.remove(tem_2_bazi_2)

                tem_1_bazi_3=random.choice(list_temhay_1)
                tem_2_bazi_3=random.choice(list_temhay_2)
                bazi_3.append(tem_1_bazi_3)
                bazi_3.append(tem_2_bazi_3)
                list_temhay_1.remove(tem_1_bazi_3)
                list_temhay_2.remove(tem_2_bazi_3)


                tem_1_bazi_4=random.choice(list_temhay_1)
                tem_2_bazi_4=random.choice(list_temhay_2)
                bazi_4.append(tem_1_bazi_4)
                bazi_4.append(tem_2_bazi_4)
                list_temhay_1.remove(tem_1_bazi_4)
                list_temhay_2.remove(tem_2_bazi_4)

                print(bazi_1)
                print(bazi_2)
                print(bazi_3)
                print(bazi_4)

                break

            case "2":
                break
                