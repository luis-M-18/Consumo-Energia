consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
tot_cocaguaya = (120 + 55 + 32 + 120 + 75 + 32 + 150 + 55 + 32 + 120 + 97 + 32)
tot_cocaquito = (400 + 432 + 400 + 420 + 432 + 460 + 432 + 400 + 432 + 300 + 213)
tot_soplaguaya = (310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321)
tot_soplaquito = (400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587)
tot_soplaloja = (50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32)

informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}

costa = tot_cocaguaya + tot_soplaguaya
sierra = tot_soplaquito + tot_cocaquito + tot_soplaloja
oriente = ('No hay planta de enería en el oriente')

print('''
    ===============================
         CONSUMO DE ENERGÍA
    ===============================
    ''')
print('<1>. Total de consumo en Planta y Ciudad ')
print('<2>. Total de Energia por Ciudad ')
print('<3>. Dinero Recaudado por Region ')
print('<4>. Escriba (salir) para Salir del programa')
opcion = input('Elija una opcion: ')

if opcion == 'salir':
    exit

#1. Solicite al usuario el nombre de una planta y de una ciudad y presente el total de
#megavatios de consumos para dicha ciudad en dicha planta.
elif opcion == '1':
    
    print('''
    ===============================
         TOTAL DE CONSUMO
               PLANTAS
    Coca Codo Sinclair, Sopladora
              CIUDADES
    Guayaquil, Quito, Loja
    ===============================
    ''')

    n_planta = input('Ingrese el nombre de la planta: ')

    if n_planta == 'Coca Codo Sinclair':
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de Megavatios de consumo en Coca Codo Sinclair, Quito: ', tot_cocaquito, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de Megavatios de consumo en Coca Codo Sinclair, Guayaquil: ', tot_cocaguaya, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa'])
        elif n_ciudad =='Loja':
            print("No hay una planta de Coca Codo Sinclair en Loja")
    print()

    if n_planta == 'Sopladora':
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de MMegavatios de consumo en Sopladora, Quito: ', tot_soplaquito, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de Megavatios de consumo en Sopladora, Guayaquil: ', tot_soplaguaya, 'Megavatios')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Guayaquil']['tarifa'])
        elif n_ciudad == 'Loja':
            print('Total de Megavatios de consumo en Sopladora, Loja: ', tot_soplaloja)
            print('Con tarifa de: ', consumo_energia['Sopladora']['Loja']['tarifa'])
    else:
        print("Digite correctamente la primera en mayuscula")

    exit
    

    

#2. Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves
#son los nombres de las plantas generadoras y el valor es el total megavatios que cada
#planta le ha dado a ciudad. Si la planta no entrega energía a la ciudad entonces esa planta
#no debería aparecer en el nuevo diccionario  
elif opcion == '2':
    print('''
    ====================================================
                TOTAL DE ENERGIA DADA A CADA
                   CIUDAD POR CADA PLANTA
       Guayaquil, Quito, Loja, Ambato, Tena, Nueva loja
    =====================================================
    '''),

    n_ciudad2 = input('Ingrese el nombre de la ciudad: ')

    if n_ciudad2 == 'Guayaquil':
        print('Total de Megavatios, Coca Codo Sinclair: ', tot_cocaguaya, 'Megavatios')
        print('Total de Megavatios, Sopladora:', tot_soplaguaya, 'Megavatios')
    elif n_ciudad2 == 'Quito':
        print('Total de Megavatios, Coca Codo Sinclair: ', tot_cocaquito, 'Megavatios')
        print('Total de Megavatios, Sopladora:', tot_soplaquito, 'Megavatios')
    elif n_ciudad2 == 'Loja':
        print('Total de Megavatios, Sopladora:', tot_soplaloja, 'Megavatios')
    else:
        print('Ninguna planta otorga energía a la ciudad seleccionada')
    print()

    exit


#3. Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la
#región
elif opcion == '3':
    print('''
    ===============================
          DINERO RECAUDADO 
              REGIONES
    Costa  --   Sierra  --  Oriente
    ===============================
    '''),

    region = input('Ingrese nombre de una Región: ')

    if region == 'Costa':
        print('Total Recaudado en la Región Costa: ', costa, '$')
    elif region == 'Sierra':
        print('Total Recaudado en la Región Sierra: ', sierra, '$')
    elif region == 'Oriente':
        print(oriente)
    else:
        print("Digite la primera letra en")
    exit