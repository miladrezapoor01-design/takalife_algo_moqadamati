



while True:
    list_asli=[]

  
    list_etelaat=[]
    menu_form=input("1.vorode_etelaat 2.exit ")
    match menu_form:
        case"1":
            nam=input("name khod bra vared konid:")
            list_etelaat.append(nam)
            name_khanevadegi=input("name khanevadegi khod ra vared konid:")
            list_etelaat.append(name_khanevadegi)
            nomre_py=float(input("nomre py ra vared konid:"))
            list_etelaat.append(nomre_py)
            nomre_jv=float(input("nomre jv ra vared konid:"))
            list_etelaat.append(nomre_jv)
            print(list_etelaat)
            list_asli.append(list_etelaat)
        case "2":
                print("by by")
                break    
      