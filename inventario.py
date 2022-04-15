import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['inventario']
col = db['productos']

def agregarArticulo(referencia, nombre, precio, cantidad, descripcion):
    articulo = {
        "referencia": referencia,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "cantidad": cantidad
    }
    col.insert_one(articulo)
    print("Articulo agregado!\n")

def editarArticulo(referencia, descripcion, cantidad, precio, nombre):
    query = {"referencia": referencia}
    update = {"$set": {"descripcion": descripcion, "cantidad" : cantidad, "precio": precio, "nombre": nombre}}
    col.update_one(query, update)
    print("Articulo actualizado!\n")

def eliminarArticulo(referencia):
    query = {"referencia": referencia}
    col.delete_one(query)
    print("Articulo eliminado!\n")

def buscarArticulo(referencia):
    query = {"referencia": referencia}
    articulo = col.find_one(query)
    print("- " + articulo['nombre'] + " (" + articulo['referencia'] + ") - " + str(articulo['precio']) + " - " + str(articulo['cantidad']) + " en stock\n")


while True:
    print("Seleccione una opcion:")
    print("1. Agregar nuevo articulo")
    print("2. Editar articulo existente")
    print("3. Eliminar articulo existente")
    print("4. Buscar significado de articulo")
    print("5. Salir")
    opcion = int(input())

    if opcion == 1:
        print("\nAgregar nuevo articulo")
        referencia = input("- Referencia: ")
        nombre = input("- Nombre: ")
        descripcion = input("- Descripcion: ")
        precio = float(input("- Precio: "))
        cantidad = int(input("- Cantidad: "))
        agregarArticulo(referencia, nombre, precio, cantidad, descripcion)
    elif opcion == 2:
        print("\nEditar articulo existente")
        referencia = input("- Referencia del articulo a actualizar: ")
        nombre = input("- Nuevo nombre: ")
        descripcion = input("- Nueva descripcion: ")
        precio = float(input("- Nuevo precio: "))
        cantidad = int(input("- Nueva cantidad: "))
        editarArticulo(referencia, descripcion, cantidad, precio, nombre)
    elif opcion == 3:
        print("\nEliminar articulo existente")
        referencia = input("- Referencia del articulo a eliminar: ")
        eliminarArticulo(referencia)
    elif opcion == 4:
        print("\nBuscar significado de articulo")
        referencia = input("- Referencia del articulo a buscar: ")
        buscarArticulo(referencia)
    elif opcion == 5:
        print("\nHasta la proxima!!\n")
        break
    else:
        print("\nOpcion invalida! Intente nuevamente\n")