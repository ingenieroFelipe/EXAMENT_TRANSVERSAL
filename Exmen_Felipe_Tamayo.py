juegos = {}
inventario = {}

def mostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")

def leer_Opcion():
    try:
        opcion = int(input("Ingrese una opción a ejecutar: "))
        if 1 >= opcion >=6:
            return opcion
        else:
            return False
    except ValueError:
        return False

def stock_plataforma(plataforma): 

def busqueda_precio(p_min, p_max):
    if p_min >=0 and p_max >= 0 and p_max > p_min:
    else:
        print("")

def eliminar_juego(codigo):
    for codigo in listadelcodigo:
        if codigo == #el de la lista:
            inventario.pop(codigo)
            juegos.pop(codigo)
        else:
            return False

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):

def buscar_codigo(codigo):
    for codigo in inventario:
        if codigo == inventario["codigo"]:
            return True
        else:
            return False

def actualizar_precio(codigo, nuevo_precio):
    actualizarCodigo = buscar_codigo(codigo, nuevo_precio)
    if actualizarCodigo == True:
        #aquí se inserta el comando que actualiza los precios
    else:
        return False

def validar_codigo(codigo):
    if codigo.strip()=="":
        return True
    else:
        return False
    
def validar_titulo(titulo):
    if titulo.strip() == "":
        return True
    else:
        return False
    
def validar_plataforma(plataforma):
    if plataforma.strip() == "":
        return True
    else:
        return False
    
def validar_genero(genero):
    if genero.strip() == "":
        return True
    else:
        return False
    
def validar_clasificacion(clasificacion):
    if clasificacion.upper() == "E" or clasificacion.upper() == "T" or clasificacion.upper() == "M":
        return True
    else:
        return False

def validar_multiplayer(multiplayer):
    if multiplayer.lower() == "s":
        return True
    elif multiplayer.lower() == "n":
        return False
    
def validar_editor(editor):
    if editor.strip() == "":
        return True
    else:
        return False

def validar_precio(precio):
    if int(precio) > 0:
        return True
    else:
        return False

def validar_stock(stock):
    if int(stock) > 0:
        return True
    else:
        return False

listaJuegosAlmacenados = []

while True:
    
    mostrarMenu()

    opcionSeleccionada = leer_Opcion()

    if opcionSeleccionada == 1:

        plataforma = input("Ingrese la platafoma del juego: ")

        print(f"El total de stock disponible es: {stock_plataforma(plataforma)}")
    
    elif opcionSeleccionada == 2:
        while True:
            print("=Busqueda por rango de precios=")
            try:
                p_min = int(input("Ingrese el precio mínimo del juego: "))
                p_max = int(input("Ingrese el precio máximo del juego: "))

                for 
            
            except ValueError:
                print("Debe ingresr valores enteros")

    elif opcionSeleccionada == 3:
        while True:
            try:
                codigo = (input("Ingrese el código del juego"))
                nuevo_precio = int(input("Ingrese el nuevo precio del juego: "))

                actualizar = actualizar_precio(codigo, nuevo_precio)

                if actualizar == True:
                    print("Precio actualizado con éxito")
                else:
                    print("El código no existe")
            except ValueError:
                print("ingrese caracteres válidos")

    elif opcionSeleccionada == 4:
        print("==Aregrar datos del juego==")

        codigo = input("Ingrese el código del juego: ")
        titulo = input("Ingrese el titulo del juego: ")
        plataforma = input("Ingrese el plataforma del juego: ")
        genero = input("Ingrese el genero del juego: ")
        clasificacion = input("Ingrese el clasificacion del juego: ")
        multiplayer = input("Ingrese el multiplayer del juego: ")
        editor = input("Ingrese el editor del juego: ")
        precio = input("Ingrese el precio del juego: ")
        stock = input("Ingrese el stock del juego: ")

        codigoValidado = validar_codigo(codigo)
        tituloValidado = validar_titulo(titulo)
        plataformaValidado = validar_plataforma(plataforma)
        generoValidado = validar_genero(genero)
        clasificacionValidado = validar_clasificacion(clasificacion)
        multiplayerValidado = validar_multiplayer(multiplayer)
        editorValidado = validar_editor(editor)
        precioValidado = validar_precio(precio)
        stockValidado = validar_stock(stock)

        if codigoValidado == True and tituloValidado == True and plataformaValidado == True and generoValidado == True and clasificacionValidado == True and multiplayerValidado == True and editorValidado == True and precioValidado == True and stockValidado == True:
        
            juego = {
                "codigo": [codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor,]
            }

            inventario = {
                "codigo": [precio, stock]
            }

        juego.append(listaJuegosAlmacenados)
        inventario.append(listaJuegosAlmacenados)

    elif opcionSeleccionada == 5:
        print("Ingrese el codigo del juego a eliminar: ")
        
        if eliminar_juego == True:
            print("Juego eliminado")
        elif eliminar_juego == False:
            print("El código no existe")

    elif opcionSeleccionada == 6:
        print("Programa Finalizado")
        break