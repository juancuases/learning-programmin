import os
client_ident = []
client_fullname = []
client_address = []
client_mobile = []
client_email = []
client_gender = []
client_age = []

product_code = []
product_name = []
product_quantity = []
product_unit_val = []

def mainmenu():
    os.system("clear")
    print("::: market main menu :::")
    print(
          "[1]. register client\n" \
          "[2]. register product\n" \
          "[3]. list clients\n" \
          "[4]. list products\n" \
          "[5]. search client by ident\n" \
          "[6]. search product by code\n" \
          "[7]. update client\n" \
          "[8]. update product\n" \
          "[9]. delete client\n" \
          "[10]. delete product\n" \
          "[11]. exit\n" \
          "::: press any option :::")
    




#main
menu_status = True
while menu_status:
    mainmenu()
    opt = int(input{})

    if opt == 1:
        os.system("clear")
        print('..............................')
        print('........new clients ..........')
        print('..............................')

        ident = input("client identification: ")
        client_ident.append(ident)
        fullname = input("client fullname: ")
        client_fullname.append(fullname)
        print('client has been registered successfully !!!')
        key = input('prees any option to back to main menu: ')
    elif opt == 3:
        print ('..............................')
        print('........list of clients ..........')
        print('..............................')
        
        i= 0
        while i < len(client_ident):
            print('indentification   |      fullname')
            print(f'{client_ident[i]}  |  {client_fullname[i]}')
            i+=1

        key = input('prees any option to back to main menu: ')

    

    if opt == "11":
        print('bye,bye')
        break
    if opt < 1 or opt > 11:
        print('invalid option, try again. \n' \
            'prees any key to continue.')
