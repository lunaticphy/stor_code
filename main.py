lista_de_items = {'item1': 1, 'item2': 3, 'item3': 5, 'item4': 6, 'item5': 8, 'item6': 10}
print(lista_de_items)
cantidad = []
cant_it = []
while True:
    user = input("Que items quieres (si ya no quiere mas productos type 'ok'): ")
    if user in lista_de_items:
        cantidad.append(lista_de_items[user]) #appends the value of the item that the user picked
        cant_it.append(user) #appends that item ( items name) that the user picked
        print("Current shoping cart", cant_it)
    elif user == 'ok': #imporatant to keep this elif condition before the elif not in list condition
        print("Tu shoping cart", cant_it)
        print("Valor de cada producto en tu shoping cart", cantidad)
        break
    elif user not in lista_de_items:
        print("Item no reconozido")
        continue

while True:
    len_cantidad = len(cantidad) #number of productes that the user picked
    print("Cantidad,", len_cantidad, "productos")
    sub_total = sum(cantidad) #sums up the values in the list that the user picked
    print("Subtotal", sub_total)
    #now we ask user if they agree with the quatity and the items the chose if not go back and pick them again]
    user_list = str(input("Are you satisfied with the products you have chosen (if yes type yes/ no type no): "))

    if user_list == 'yes':
        print("..........................")
        if 1 <= len_cantidad <= 5:
            descuento = 0 * sub_total
            print("Descuento ", descuento)
        elif 6 <= len_cantidad <= 10:
            descuento = 0.10 * sub_total
            print("Descuento es del 10%, :", "$", descuento)

        elif 11 <= len_cantidad <= 20:
            descuento = 0.20 * sub_total
            print("Descuento", descuento)

        elif 21 <= len_cantidad <= 50:
            descuento = 0.3 * sub_total
            print("Descuento", descuento)

        elif len_cantidad >= 51:
            descuento = 0.4 * sub_total
            print("Descuento", descuento)
        print("Descuento", descuento)
        def total():
            total1 = sub_total - descuento
            print("Total a pagar $", total1)
            print("..........................")
        total()
        break
    elif user_list == 'no':
        continue
    else:
        print("Opcion no reconozida! ")
        continue
