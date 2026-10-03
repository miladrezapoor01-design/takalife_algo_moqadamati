

list_nomarat=[] 
list_miyangin=[]

while True:
   
    
    menu_nomarat_miyangin=input("1.vared kardan nomarat 2.exit")
    match menu_nomarat_miyangin:
        case"1":
            nom_riyazi=float(input("nom riyazi ra vared konid:"))
            nom_tarikh=float(input("nom tarikh ra vared konid:"))
            nom_zist=float(input("nom zist ra vared konid:"))
            list_nomarat.append(nom_riyazi)
            list_nomarat.append(nom_tarikh)
            list_nomarat.append(nom_zist)
            print(list_nomarat)
                
            
            jame_nom=sum(list_nomarat)
            miu=jame_nom/len(list_nomarat)
            print(miu)

                
                
            break


