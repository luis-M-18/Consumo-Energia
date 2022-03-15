
consumo_energia = {
    "Coca Codo Sinclair" :{
        "Quito" : {"consumos" : (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213, 400), "tarifa" : 65},
    "Guayaquil": { "consumos": (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),"tarifa": 84}, 
    },
    
    "Sopladora": {
        "Guayaquil":{ "consumos": (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321), "tarifa" : 55},
        "Quito": { "consumos": (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),"tarifa": 79},
        "Loja": { "consumos": (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),"tarifa": 32},
    },
}
informacion = {
 "costa": ("Guayaquil", "Manta"),
 "sierra": ("Quito", "Ambato", "Loja"),
 "oriente": ("Tena", "Nueva Loja")
}

def buscar_planta_ciudad(planta, ciudad):
    energia = []
    for h in consumo_energia:
        if h == planta:
                Object = consumo_energia[h]
                for key in Object:
                        if key == ciudad:
                                Object2 = Object[key]
                                energia.append(sum(Object2["consumos"])) 
    return energia
def ingresar_informacion(data,ciudad):
    Vinculo = {}
    Vinculo[ciudad] = data
    return Vinculo

def registrar_plantas(diccionario,plantas):
    energia = []
    for h in consumo_energia :
            energia.append(h)
            diccionario[plantas] = energia
    return diccionario

def registrar_ciudades(diccionario,plantas):
    energia = []
    for h in consumo_energia :
            Object = consumo_energia[h]
            for key in Object :
                    Object2 = Object[key] 
                    energia.append(sum(Object2["consumos"])) 
                    diccionario[plantas] = energia
    return diccionario

def consultar_ciudad(nombre_ciudad):
    verificar_ciudad = True
    for h in consumo_energia :
            Object = consumo_energia[h] 
            for key in Object :
                    if key == nombre_ciudad : 
                            verificar_ciudad = False
    return verificar_ciudad

def TotalSierra(region):
    total_Dinero = 0
    if region == "Sierra": 
        tarifaQuitoS = consumo_energia["Sopladora"]["Quito"]["tarifa"]  
        tarifaLoja = consumo_energia["Sopladora"]["Loja"]["tarifa"] 
        tarifaQuitoC = consumo_energia["Coca Codo Sinclair"]["Quito"]["tarifa"]
        total_Dinero = (tarifaQuitoS*12) + (tarifaQuitoC*12) + (tarifaLoja*12)
        return total_Dinero
    else:
        print("Región no disponible")
op = -1

while op != 0:
    print("(1)Mostrar consumo de energia por planta y ciuda")
    print("(2)Mostrar megavatios de cada ciudad existente")
    print("(3)Mostrar información del consumo de cada región")

    op = int(input("Ingrese su opción: "))

    if op == 1 :
        planta = input("Ingresar planta: ")
        ciudad = input("Ingresar ciudad: ")
        plantas = buscar_planta_ciudad(planta, ciudad)       
        print("Total de Megavatios de consumo" + str(plantas))
    elif op == 2:
        Vinculo = {}
        
        ciudad = input("Ingrese el nombre de una ciudad: ")
        verificar_ciudad = consultar_ciudad(ciudad)
        if(verificar_ciudad):
            Vinculo = ingresar_informacion(ciudad,"ciudad")
            print("La ciudad Ingresada fue:" + str(Vinculo))
        
            Vinculo =registrar_ciudades(Vinculo, "Coca Codo Sinclair")
            Vinculo = registrar_ciudades(Vinculo, "Sopladora")
            print("La Plantas con el total cosumido por ciudad son:" + str(Vinculo))
        else:
            print("La ciudad que ingresaste ya se encuentra registrada")

    elif op == 3:
       luz = input("Ingrese el nombre de una región: ")
       energia = TotalSierra(luz)
       if luz == "Sierra":
           print("Total de dinero recaudado de la region",luz,":", energia)