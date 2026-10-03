




import random

while True:

    menu_qore=input("1.vorod 2.qore 3.exit")
    list_qore=["milad","ali","akbar","mohamad","amekokab","fariborz"]
    
    while True:
        match menu_qore:
            case "1":
                user_admin=input("user ra vared konid:")
                password_admin=input("password ra vared konid:")

                if user_admin=="ame_kokab" and password_admin=="ame_ame":
                    print("log in")
                else:
                    print("hoshtar")
                break    
                    
            case "2":
                barande=random.choices(list_qore,cum_weights=[1,1,1,1,1,10])
                print(barande)
                break
                    
            case"3":
                break
