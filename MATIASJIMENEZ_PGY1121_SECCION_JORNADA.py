habitaciones ={
1: {'ocupada' : False, 'mascota':''},
2: {'ocupada' : False, 'mascota':''},
3: {'ocupada' : False, 'mascota':''},
4: {'ocupada' : False, 'mascota':''},
5: {'ocupada' : False, 'mascota':''},
6: {'ocupada' : False, 'mascota':''},
7: {'ocupada' : False, 'mascota':''},
8: {'ocupada' : False, 'mascota':''},
9: {'ocupada' : False, 'mascota':''},
10: {'ocupada' : False, 'mascota':''},

def validar_rut (rut)
rut = rur.replace (".","").replace ("-","")
    if not re.match ()
     return False
     return True:
    
def validar_nombre (nombre):
    if len (nombre ) < 3:
     return False
     return True:

def grabar_mascota():
    rut = input ("ingrese rut del dueño: ")
    if not validar_rut (rut):
    print ("el rut ingresado no es valido")
    return
      nombre_dueño = input ("debe ingresa el nombre del dueño: ")
      validar_nombre (nombre dueño):
            print ("el nombre del dueño debe tener al menos 3 letras.")
            return
        identificador = len (habitacion) + 1 
        nombre_mascota = input ("ingrese el nombre de la mascota: ")
        if not
        validar_nombre (validar_mascota):
            print ("el nombre de la mascota debe tener al menos 3 letras. ")
            return
        
      dias_guarderia = int(input("ingrese la cantidad de dias en la guarderia: "))
      habitacion_elegida = int(input("ingrese el numero de habitacion del (1 al 10): "))
      
      if habitacion elegida 
      not int habitaciones.keys():
        print ("la habitacion", habitacion_elegida, "no es valida.",)
        return
      if
      habitaciones [habitaciones_elegidas]['ocupada']:
        print ("la habitacion", habitacion_elegida, "la habitacion elegida, ya esta ocupada por favor elija otra habitacion.")
        return 
      habitaciones [habitaciones_elegidas]['ocupada'] = True
      habitaciones [habitacion_elegida]['mascota'] = nombre_mascota
       print ("mascota asignadamente en la habitacion", habitacion_elegida, "!")

       def buscar_mascota ():

        
    

    



    