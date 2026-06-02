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
          "[1]. register client\n"
          "[2]. register product\n"
          "[3]. list clients\n"
          "[4]. list products\n"
          "[5]. search client by ident\n"
          "[6]. search product by code\n"
          "[7]. update client\n"
          "[8]. update product\n"
          "[9]. delete client\n"
          "[10]. delete product\n"
          "[11]. exit\n"
          "::: press any option :::")


# main
menu_status = True

while menu_status:

    mainmenu()
    opt = int(input())

    if opt == 1:
        os.system('clear')
        print('..............................')
        print('........new clients..........')
        print('..............................')

        ident = input('client identification: ')
        client_ident.append(ident)

        fullname = input('client fullname: ')
        client_fullname.append(fullname)

        address = input('client address: ')
        client_address.append(address)

        mobile = input('client mobile: ')
        client_mobile.append(mobile)

        email = input('client email: ')
        client_email.append(email)

        gender = input('client gender: ')
        client_gender.append(gender)

        age = input('client age: ')
        client_age.append(age)

        print('client has been registered successfully !!!')
        key = input('press any option to back to main menu: ')

    elif opt == 2:
        os.system('clear')
        print('..............................')
        print('........new product..........')
        print('..............................')

        code = input('product code: ')
        product_code.append(code)

        name = input('product name: ')
        product_name.append(name)

        quantity = input('product quantity: ')
        product_quantity.append(quantity)

        value = input('product unit value: ')
        product_unit_val.append(value)

        print('product has been registered successfully !!!')
        key = input('press any option to back to main menu: ')

    elif opt == 3:
        os.system('clear')
        print('..............................')
        print('........list of clients......')
        print('..............................')

        print('\n')
        print('-'*50)
        print(f'{"identification":<20} {"fullname":<20}')
        print('-'*50)

        i = 0
        while i < len(client_fullname):
            print(f'{client_ident[i]:<20} {client_fullname[i]:<20}')
            i += 1

        key = input('press any option to back to main menu: ')

    elif opt == 4:
        os.system('clear')
        print('..............................')
        print('........list products........')
        print('..............................')

        print('-'*60)
        print(f'{"code":<15} {"name":<20} {"quantity":<10} {"value":<10}')
        print('-'*60)

        i = 0
        while i < len(product_name):
            print(f'{product_code[i]:<15} {product_name[i]:<20} {product_quantity[i]:<10} {product_unit_val[i]:<10}')
            i += 1

        key = input('press any option to back to main menu: ')

    elif opt == 5:
        ident = input('client identification: ')

        if ident in client_ident:
            pos = client_ident.index(ident)

            print('identification:', client_ident[pos])
            print('fullname:', client_fullname[pos])
            print('address:', client_address[pos])
            print('mobile:', client_mobile[pos])
            print('email:', client_email[pos])
            print('gender:', client_gender[pos])
            print('age:', client_age[pos])
        else:
            print('client not found')

        input('press any option to continue: ')

    elif opt == 6:
        code = input('product code: ')

        if code in product_code:
            pos = product_code.index(code)

            print('code:', product_code[pos])
            print('name:', product_name[pos])
            print('quantity:', product_quantity[pos])
            print('value:', product_unit_val[pos])
        else:
            print('product not found')

        input('press any option to continue: ')

    elif opt == 7:
        ident = input('client identification: ')

        if ident in client_ident:
            pos = client_ident.index(ident)

            client_fullname[pos] = input('new fullname: ')
            client_address[pos] = input('new address: ')
            client_mobile[pos] = input('new mobile: ')
            client_email[pos] = input('new email: ')
            client_gender[pos] = input('new gender: ')
            client_age[pos] = input('new age: ')

            print('client updated successfully')
        else:
            print('client not found')

        input('press any option to continue: ')

    elif opt == 8:
        code = input('product code: ')

        if code in product_code:
            pos = product_code.index(code)

            product_name[pos] = input('new name: ')
            product_quantity[pos] = input('new quantity: ')
            product_unit_val[pos] = input('new value: ')

            print('product updated successfully')
        else:
            print('product not found')

        input('press any option to continue: ')

    elif opt == 9:
        ident = input('client identification: ')

        if ident in client_ident:
            pos = client_ident.index(ident)

            del client_ident[pos]
            del client_fullname[pos]
            del client_address[pos]
            del client_mobile[pos]
            del client_email[pos]
            del client_gender[pos]
            del client_age[pos]

            print('client deleted successfully')
        else:
            print('client not found')

        input('press any option to continue: ')

    elif opt == 10:
        code = input('product code: ')

        if code in product_code:
            pos = product_code.index(code)

            del product_code[pos]
            del product_name[pos]
            del product_quantity[pos]
            del product_unit_val[pos]

            print('product deleted successfully')
        else:
            print('product not found')

        input('press any option to continue: ')

    elif opt == 11:
        print('bye bye')
        break

    else:
        print('invalid option, try again')
        input('press any key to continue')
