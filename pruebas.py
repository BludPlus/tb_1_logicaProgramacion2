
from colorama import Fore;
import os;
os.system("clear")
cuenta = 134000;


remu_horas_extras = 0;

pagoHorasExtrasFeriados = 0;


cantidad_horas = 0;
comHorasEXtras = True;
while(comHorasEXtras):
    
    realizoExtras = input(Fore.WHITE + "Realizo horas extras? S/N \n")
    
    
    remu_horas_extras = 0;

    if(realizoExtras.lower() == "s"):

        salarioPorDia = cuenta / 30;
        salarioPorHora = salarioPorDia / 8;
        print(salarioPorDia);
        print(salarioPorHora)
        try:

            cantidad_horas  = int(input("Cuantas horas: "))

            
            comFeriados = True;
            while(comFeriados):

                feriados = input("Tuvo horas extras en dias feriados? S/N ")
                
                if(feriados.lower() == "s"):
                    comHorasFeriados = True;
                    while(comHorasFeriados):
                        try: 
                            
                            cantidadHorasFeriados = int(input(f"Cuantas de las {cantidad_horas} horas extras fueron feriados? "))

                            if(cantidadHorasFeriados <= cantidad_horas):

                                pagoal100 = salarioPorHora * 2.0;
                                pagoHorasExtrasFeriados = pagoal100 * cantidadHorasFeriados;

                                cantidad_horas = cantidad_horas - cantidadHorasFeriados;
                                
                                pagoal50 = salarioPorHora * 1.5
                                pagoHorasExtrasNormal = pagoal50 * cantidad_horas; 
                                remu_horas_extras = pagoHorasExtrasNormal + pagoHorasExtrasFeriados
                                print(remu_horas_extras, " con  4 feriados")
                                

                                comFeriados = False;
                                comHorasFeriados = False;
                                comHorasEXtras = False;
                                break
                            else: 
                                print("ingrese correctamente las horas extras: ")
                        except ValueError:
                            os.system("clear")
                            print("Ingrese horas")

                elif(feriados.lower() == "n"):
                    pagoal50 = salarioPorHora * 1.5
                    print(pagoal50)
                    pagoHorasExtrasNormal = pagoal50 * cantidad_horas;
                    print(pagoHorasExtrasFeriados)
                    remu_horas_extras = pagoHorasExtrasNormal;
                    print(remu_horas_extras, " sin  4 feriados")
                    comHorasEXtras = False;
                    break 
                else:
                    os.system("clear")      
                    print("Ingrese S/N")
        
        except ValueError:
            os.system("clear") 
            print("Error ingrese numero")
    elif(realizoExtras.lower() == "n"):
        comHorasEXtras = False;
    else:
        os.system("clear") 
        print(Fore.YELLOW +"Ingrese S/N")