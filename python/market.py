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
    

    # MAIN
    menu_status = True
while menu_status:
    mainmenu()
    opt = int(input())

    
 # REGISTER CLIENT
    # =====================
    if opt == 1:

        os.system("cls" if os.name == "nt" else "clear")

        ident = input("Client identification: ")

        if ident in client_ident:
            print("Client already exists.")
        else:
            fullname = input("Full name: ")
            address = input("Address: ")
            mobile = input("Mobile: ")
            email = input("Email: ")
            gender = input("Gender: ")
            age = int(input("Age: "))

            client_ident.append(ident)
            client_fullname.append(fullname)
            client_address.append(address)
            client_mobile.append(mobile)
            client_email.append(email)
            client_gender.append(gender)
            client_age.append(age)

            print("Client registered successfully!")

        input("Press ENTER to continue...")

    # =====================
    # REGISTER PRODUCT
    # =====================
    elif opt == 2:

        os.system("cls" if os.name == "nt" else "clear")

        code = input("Product code: ")

        if code in product_code:
            print("Product code already exists.")
        else:
            name = input("Product name: ")
            quantity = int(input("Quantity: "))
            value = float(input("Unit value: "))

            product_code.append(code)
            product_name.append(name)
            product_quantity.append(quantity)
            product_unit_val.append(value)

            print("Product registered successfully!")

        input("Press ENTER to continue...")

    # =====================
    # LIST CLIENTS
    # =====================
    elif opt == 3:

        os.system("cls" if os.name == "nt" else "clear")

        print("-" * 120)
        print(
            f'{"ID":<15} {"FULL NAME":<20} {"ADDRESS":<20} {"MOBILE":<15} {"EMAIL":<25} {"GENDER":<10} {"AGE":<5}'
        )
        print("-" * 120)

        for i in range(len(client_ident)):
            print(
                f'{client_ident[i]:<15} '
                f'{client_fullname[i]:<20} '
                f'{client_address[i]:<20} '
                f'{client_mobile[i]:<15} '
                f'{client_email[i]:<25} '
                f'{client_gender[i]:<10} '
                f'{client_age[i]:<5}'
            )

        input("\nPress ENTER to continue...")

    # =====================
    # LIST PRODUCTS
    # =====================
    elif opt == 4:

        os.system("cls" if os.name == "nt" else "clear")

        print("-" * 70)
        print(f'{"CODE":<15} {"NAME":<25} {"QTY":<10} {"VALUE":<10}')
        print("-" * 70)

        for i in range(len(product_code)):
            print(
                f'{product_code[i]:<15} '
                f'{product_name[i]:<25} '
                f'{product_quantity[i]:<10} '
                f'{product_unit_val[i]:<10.2f}'
            )

        input("\nPress ENTER to continue...")

    # =====================
    # SEARCH CLIENT
    # =====================
    elif opt == 5:

        ident = input("Identification: ")

        if ident in client_ident:
            pos = client_ident.index(ident)

            print("\nClient found")
            print("ID:", client_ident[pos])
            print("Name:", client_fullname[pos])
            print("Address:", client_address[pos])
            print("Mobile:", client_mobile[pos])
            print("Email:", client_email[pos])
            print("Gender:", client_gender[pos])
            print("Age:", client_age[pos])

        else:
            print("Client not found.")

        input("Press ENTER to continue...")

    # =====================
    # SEARCH PRODUCT
    # =====================
    elif opt == 6:

        code = input("Product code: ")

        if code in product_code:
            pos = product_code.index(code)

            print("\nProduct found")
            print("Code:", product_code[pos])
            print("Name:", product_name[pos])
            print("Quantity:", product_quantity[pos])
            print("Value:", product_unit_val[pos])

        else:
            print("Product not found.")

        input("Press ENTER to continue...")

    # =====================
    # UPDATE CLIENT
    # =====================
    elif opt == 7:

        ident = input("Identification: ")

        if ident in client_ident:
            pos = client_ident.index(ident)

            client_fullname[pos] = input("New full name: ")
            client_address[pos] = input("New address: ")
            client_mobile[pos] = input("New mobile: ")
            client_email[pos] = input("New email: ")
            client_gender[pos] = input("New gender: ")
            client_age[pos] = int(input("New age: "))

            print("Client updated successfully!")

        else:
            print("Client not found.")

        input("Press ENTER to continue...")

    # =====================
    # UPDATE PRODUCT
    # =====================
    elif opt == 8:

        code = input("Product code: ")

        if code in product_code:
            pos = product_code.index(code)

            product_name[pos] = input("New name: ")
            product_quantity[pos] = int(input("New quantity: "))
            product_unit_val[pos] = float(input("New value: "))

            print("Product updated successfully!")

        else:
            print("Product not found.")

        input("Press ENTER to continue...")

    # =====================
    # DELETE CLIENT
    # =====================
    elif opt == 9:

        ident = input("Identification: ")

        if ident in client_ident:
            pos = client_ident.index(ident)

            del client_ident[pos]
            del client_fullname[pos]
            del client_address[pos]
            del client_mobile[pos]
            del client_email[pos]
            del client_gender[pos]
            del client_age[pos]

            print("Client deleted successfully!")

        else:
            print("Client not found.")

        input("Press ENTER to continue...")

    # =====================
    # DELETE PRODUCT
    # =====================
    elif opt == 10:

        code = input("Product code: ")

        if code in product_code:
            pos = product_code.index(code)

            del product_code[pos]
            del product_name[pos]
            del product_quantity[pos]
            del product_unit_val[pos]

            print("Product deleted successfully!")

        else:
            print("Product not found.")

        input("Press ENTER to continue...")

    # =====================
    # EXIT
    # =====================
    elif opt == 11:

        print("Bye Bye...")
        break

    # =====================
    # INVALID OPTION
    # =====================
    else:
