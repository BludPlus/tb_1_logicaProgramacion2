
from datetime import datetime;
import os;
from colorama import Fore;



fecha_actual = datetime.today().strftime("%Y-%m-%d %H:%M")

añoAcual = datetime.today().strftime("%Y")
añoAcual = int(añoAcual);

os.system("clear")



while(True):
    nombre = (input(Fore.WHITE + "Ingrese Nombre: "))
    apellido = (input("Ingrese Apellido: "))
    
    if(nombre.isalpha() and apellido.isalpha() and not nombre.isdigit() and not apellido.isdigit() and len(nombre) > 1 and len(apellido) > 1):
        break
    os.system("clear")
    print(Fore.RED + "Ingrese nombre y apellido correctamente")



cuil = 0;
while (True):    
    try:
        
        print(Fore.WHITE + f"{nombre} {apellido}")
        cuil = int(input("Ingrese CUIL: "))
        break;
    except ValueError:
        os.system("clear")
        print(Fore.RED + "Ingrese Correctamente")
os.system("clear")



while(True):
    print(Fore.WHITE + f"{nombre} {apellido} {cuil}")
    puesto = input("Ingrese el Puesto: ")
    cargo = input("Ingrese el Cargo: ")
    if(cargo.isalpha() and cargo.isalpha()):
        break
    os.system("clear")
    print(Fore.RED + "Ingrese Correctamente el puesto y cargo")
os.system("clear")



año_de_ingreso = 0;
fechaAñoIngreso = 0;
fechaMesIngreso = 0;
fechaDiaIngreso = 0;
comprobacionAño = 0;



comprobacionAñoIngreso = True;
while(comprobacionAñoIngreso):


    
       
    while(True):
        try:
            print(Fore.WHITE + f"{nombre} {apellido}")
            fechaAñoIngreso = int(input(Fore.WHITE + "Ingrese Año de Ingreso: "));
            fechaMesIngreso = int(input("Ingrese Mes de Ingreso: "));
            fechaDiaIngreso = int(input("Ingrese Dia de Ingreso: "));
            if(fechaAñoIngreso >= 1990 and fechaAñoIngreso and añoAcual and fechaMesIngreso >= 1 and fechaMesIngreso <= 12 and fechaDiaIngreso >= 1 and fechaDiaIngreso <= 33):
                
                os.system('clear')
                
                break
            
            os.system('clear')
            print(Fore.RED + "Ingrese correctamente la fecha de ingreso")    
            
            
        except ValueError:
            os.system("clear")
            print(Fore.RED +"Ingreso texto, ingrese correctamente la fecha de ingreso")



    os.system("clear")
    
    
        
    while(True):
        
        print(Fore.WHITE + f"{fechaDiaIngreso} - {fechaMesIngreso}- {fechaAñoIngreso}")
        print(Fore.YELLOW + "¿Esta seguro de la fecha de ingreso? S/N")
        
        seguroFecha = input("S/N: ");

        
        if(seguroFecha.lower() == "s"):  

            comprobacionAñoIngreso = False;
            break;
        
        elif(seguroFecha.lower() == "n"):
            os.system("clear")
            print("Ingrese nuevamente la fecha de ingreso...")
            break;

        else:
                os.system("clear")
                print(Fore.RED + "Ingrese S/N")





añosAntiguedad =  fechaAñoIngreso - añoAcual;


