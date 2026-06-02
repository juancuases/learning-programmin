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

def mainMenu():
    os.system('clear')
    print("=== MARKET MAIN MENU ===")
    print("[1] Registrar cliente")
    print("[2] Registrar producto")
    print("[3] Listar clientes")
    print("[4] Listar productos")
    print("[5] Buscar cliente")
    print("[6] Buscar producto")
    print("[7] Actualizar cliente")
    print("[8] Actualizar producto")
    print("[9] Eliminar cliente")
    print("[10] Eliminar producto")
    print("[11] Salir")

def registrarCliente():
    os.system('clear')
    print("=== REGISTRAR CLIENTE ===")
    ident = input("Identificacion: ")
    if ident in client_ident:
        print("Esa identificacion ya existe.")
        input("Enter para continuar.")
        return
    client_ident.append(ident)
    client_fullname.append(input("Nombre completo: "))
    client_address.append(input("Direccion: "))
    client_mobile.append(input("Telefono: "))
    client_email.append(input("Email: "))
    client_gender.append(input("Genero (M/F): "))
    client_age.append(input("Edad: "))
    print("Cliente registrado!")
    input("Enter para continuar.")

def registrarProducto():
    os.system('clear')
    print("=== REGISTRAR PRODUCTO ===")
    code = input("Codigo del producto: ")
    if code in product_code:
        print("Ese codigo ya existe.")
        input("Enter para continuar.")
        return
    product_code.append(code)
    product_name.append(input("Nombre del producto: "))
    product_quantity.append(input("Cantidad en stock: "))
    product_unit_val.append(input("Valor unitario: "))
    print("Producto registrado!")
    input("Enter para continuar.")

def listarClientes():
    os.system('clear')
    print("=== LISTA DE CLIENTES ===")
    if len(client_ident) == 0:
        print("No hay clientes registrados.")
    else:
        i = 0
        while i < len(client_ident):
            print(f"ID: {client_ident[i]} | Nombre: {client_fullname[i]} | Dir: {client_address[i]} | Tel: {client_mobile[i]} | Email: {client_email[i]} | Genero: {client_gender[i]} | Edad: {client_age[i]}")
            i += 1
    input("Enter para continuar.")

def listarProductos():
    os.system('clear')
    print("=== LISTA DE PRODUCTOS ===")
    if len(product_code) == 0:
        print("No hay productos registrados.")
    else:
        i = 0
        while i < len(product_code):
            print(f"Codigo: {product_code[i]} | Nombre: {product_name[i]} | Cantidad: {product_quantity[i]} | Valor: {product_unit_val[i]}")
            i += 1
    input("Enter para continuar.")

def buscarCliente():
    os.system('clear')
    print("=== BUSCAR CLIENTE ===")
    ident = input("Ingrese la identificacion: ")
    i = 0
    encontrado = False
    while i < len(client_ident):
        if client_ident[i] == ident:
            print(f"Nombre: {client_fullname[i]}")
            print(f"Direccion: {client_address[i]}")
            print(f"Telefono: {client_mobile[i]}")
            print(f"Email: {client_email[i]}")
            print(f"Genero: {client_gender[i]}")
            print(f"Edad: {client_age[i]}")
            encontrado = True
            break
        i += 1
    if not encontrado:
        print("Cliente no encontrado.")
    input("Enter para continuar.")

def buscarProducto():
    os.system('clear')
    print("=== BUSCAR PRODUCTO ===")
    code = input("Ingrese el codigo: ")
    i = 0
    encontrado = False
    while i < len(product_code):
        if product_code[i] == code:
            print(f"Nombre: {product_name[i]}")
            print(f"Cantidad: {product_quantity[i]}")
            print(f"Valor: {product_unit_val[i]}")
            encontrado = True
            break
        i += 1
    if not encontrado:
        print("Producto no encontrado.")
    input("Enter para continuar.")

def actualizarCliente():
    os.system('clear')
    print("=== ACTUALIZAR CLIENTE ===")
    ident = input("Ingrese la identificacion: ")
    i = 0
    while i < len(client_ident):
        if client_ident[i] == ident:
            client_fullname[i] = input(f"Nuevo nombre ({client_fullname[i]}): ")
            client_address[i] = input(f"Nueva direccion ({client_address[i]}): ")
            client_mobile[i] = input(f"Nuevo telefono ({client_mobile[i]}): ")
            client_email[i] = input(f"Nuevo email ({client_email[i]}): ")
            client_gender[i] = input(f"Nuevo genero ({client_gender[i]}): ")
            client_age[i] = input(f"Nueva edad ({client_age[i]}): ")
            print("Cliente actualizado!")
            input("Enter para continuar.")
            return
        i += 1
    print("Cliente no encontrado.")
    input("Enter para continuar.")

def actualizarProducto():
    os.system('clear')
    print("=== ACTUALIZAR PRODUCTO ===")
    code = input("Ingrese el codigo: ")
    i = 0
    while i < len(product_code):
        if product_code[i] == code:
            product_name[i] = input(f"Nuevo nombre ({product_name[i]}): ")
            product_quantity[i] = input(f"Nueva cantidad ({product_quantity[i]}): ")
            product_unit_val[i] = input(f"Nuevo valor ({product_unit_val[i]}): ")
            print("Producto actualizado!")
            input("Enter para continuar.")
            return
        i += 1
    print("Producto no encontrado.")
    input("Enter para continuar.")

def eliminarCliente():
    os.system('clear')
    print("=== ELIMINAR CLIENTE ===")
    ident = input("Ingrese la identificacion: ")
    i = 0
    while i < len(client_ident):
        if client_ident[i] == ident:
            client_ident.pop(i)
            client_fullname.pop(i)
            client_address.pop(i)
            client_mobile.pop(i)
            client_email.pop(i)
            client_gender.pop(i)
            client_age.pop(i)
            print("Cliente eliminado!")
            input("Enter para continuar.")
            return
        i += 1
    print("Cliente no encontrado.")
    input("Enter para continuar.")

def eliminarProducto():
    os.system('clear')
    print("=== ELIMINAR PRODUCTO ===")
    code = input("Ingrese el codigo: ")
    i = 0
    while i < len(product_code):
        if product_code[i] == code:
            product_code.pop(i)
            product_name.pop(i)
            product_quantity.pop(i)
            product_unit_val.pop(i)
            print("Producto eliminado!")
            input("Enter para continuar.")
            return
        i += 1
    print("Producto no encontrado.")
    input("Enter para continuar.")

# Main
while True:
    mainMenu()
    opt = int(input("Opcion: "))

    if opt == 1:
        registrarCliente()
    elif opt == 2:
        registrarProducto()
    elif opt == 3:
        listarClientes()
    elif opt == 4:
        listarProductos()
    elif opt == 5:
        buscarCliente()
    elif opt == 6:
        buscarProducto()
    elif opt == 7:
        actualizarCliente()
    elif opt == 8:
        actualizarProducto()
    elif opt == 9:
        eliminarCliente()
    elif opt == 10:
        eliminarProducto()
    elif opt == 11:
        print("Hasta luego!")
        break
    else:
        input("Opcion invalida. Enter para continuar.")
