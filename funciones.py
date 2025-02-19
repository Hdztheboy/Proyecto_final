def cartelera():
    print("\n¡Cartelera de películas!")
    print("1 Moana2 - $12")
    print("2 Intensamente - $11")
    print("3 Mufasa - $13")
    print("4 Wicked - $15")
    print("5 La Balada de Hortensia- $17")
    
    
def boletos():
 
    pelicula = int(input("Selecciona el múmero de la película que quieres ver: "))
    asientos = int(input("Cuántos asientos quiere comprar?: "))
    precios = {1: 12, 2: 11, 3: 13, 4: 15, 5: 17}

    if pelicula in precios:
        total= precios [pelicula] * asientos
    print(f"\nEl total de su compra es:${total}")
    confirmación_de_compra = input("Confirma que quere hacer la compra (si/no): "). lower ()
    
    if confirmación_de_compra == "si":
        compras_hechas.append(f"Película {pelicula} - {asientos} asientos - ${total}")
        print("Hiciste la compra con exito")
    else:
     print("No se pudo papito")

def lista_de_las_compras_hechas():
    if compras_hechas:
        print("\nCompras realizadas:")
        for compras in compras_hechas:
            print("Has comprado papito")
    else :
        print("No compró nadota")

compras_hechas = []
while True:
    print("\nBienvenido  a tu cine!!!!!!")
    print("1-Ver cartelera")
    print("2-Comprar boletos")
    print("3-Ver compras hechas")
    print("4-Salir")
    
    opcion= int(input("\nSelecciona un número: "))

    if opcion == 1:
       cartelera()
    elif opcion == 2:
     boletos()
    elif opcion == 3:
     lista_de_las_compras_hechas()
    elif opcion == 4:
        break

    else:
     print(" Te equivocaste muchacit@")
     