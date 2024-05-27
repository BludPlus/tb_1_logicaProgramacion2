
from colorama import Fore;
import os;
os.system("clear")
cuenta = 130000;

remu_horas_extras = 0;
cantidad_horas = 0;

while(True):
    
    realizoExtras = input(Fore.WHITE + "Realizo horas extras? S/N \n")

    
    remu_horas_extras = 0;

    if(realizoExtras.lower() == "s"):

        salarioPorDia = cuenta / 30;
        salarioPorHora = cuenta / 8;
        
        try:

            cantidad_horas  = int(input("Cuantas horas: "))

            

            while(True):

                feriados = input("Tuvo horas extras en dias feriados? S/N")
                
                if(feriados.lower() == "s"):
                    
                    while(True):
                        
                        try:
                            horasExtras = int(input("Cuantos dias?"));

                            pagoHorasExtras = cantidad_horas * salarioPorHora * 1.0;
                            remu_horas_extras = pagoHorasExtras;
                        except ValueError:
                            os.system("clear")
                            print(Fore.RED + "Ingrese dias")
                break   
        
        except ValueError:
        
            os.system("clear")
            print(Fore.WHITE + "ingrese horas extras correctamente")
    elif(realizoExtras.lower() == "n"):
        break
    os.system("clear")

remuneraciones = remuneraciones + remu_horas_extras;
os.system("clear")
