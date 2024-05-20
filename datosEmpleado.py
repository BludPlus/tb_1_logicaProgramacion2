
from datetime import datetime;
import os;
from colorama import Fore;
fecha_actual = datetime.today().strftime("%Y-%m-%d %H:%M")


nombre = (input("Ingrese Nombre: "))
apellido = (input("Ingrese Nombre: "))
os.system("clear")


comprobacionCUIL = 0
cuil = 0;
while (comprobacionCUIL < 1):    
    try:
        
        print(Fore.WHITE + f"{nombre} {apellido}")
        cuil = int(input("Ingrese CUIL: "))
        comprobacionCUIL += 1;
    except ValueError:
        os.system("clear")
        print(Fore.RED + "Ingrese Correctamente")
os.system("clear")



print(Fore.WHITE + f"{nombre} {apellido}")
cargo = input("Ingrese el Cargo: ")
puesto = input("Ingrese el Puesto: ")
os.system("clear")



año_de_ingreso = 0;
fechaAñoIngreso = 0;
fechaMesIngreso = 0;
fechaDiaIngreso = 0;
comprobacionAñoIngreso = 0;
comprobacionAño = 0;
while(comprobacionAñoIngreso < 1):


    while(comprobacionAño < 1):
        print(Fore.WHITE + f"{nombre} {apellido}")
        try:
            fechaAñoIngreso = int(input("Ingrese Año de Ingreso: "));
            fechaMesIngreso = int(input("Ingrese Mes de Ingreso: "));
            fechaDiaIngreso = int(input("Ingrese Dia de Ingreso: "));
            comprobacionAño += 1;
        except ValueError:
            os.system("clear")
            print(Fore.RED +"Ingrese correctamente")
    

    os.system("clear")
    seguroFecha = "";
    comprobacionFecha = 0
    while(comprobacionFecha < 1):
        print(Fore.YELLOW + "¿Esta seguro de la fecha de ingreso? S/N")
        print(Fore.WHITE + f"{fechaDiaIngreso} - {fechaMesIngreso}- {fechaAñoIngreso}")
        seguroFecha = input("S/N: ");
        print(seguroFecha.lower)
        if(seguroFecha.lower == "s"):  #ERROR <built-in method lower of str object at 0x72dd1446fc70>
            comprobacionFecha += 1;
            comprobacionAño +=1
        elif(seguroFecha.lower == "n"):
            comprobacionFecha += 1;
            os.system("clear")
            print("Ingrese nuevamente la fecha de ingreso...")
            
        else:
            os.system("clear")
            print(Fore.RED + "Ingrese S/N")
            


