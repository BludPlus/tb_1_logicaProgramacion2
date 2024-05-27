from datetime import datetime;
from colorama import Fore;
import os;
import locale;

locale.setlocale(locale.LC_ALL, 'es_ES.ISO8859-1')

fecha_actual = datetime.today().strftime("%Y-%m-%d %H:%M")

os.system("clear")





cuenta = 0;


saldo_Cobrar = 0;


while(True):
    try:
        salario_base = float(input("Ingrese salario: "))
        cuenta = salario_base;
        break
    except ValueError:
        print("Ingreso texto")
        os.system("clear")
os.system("clear")


dedu_impuestosganancias_porcentaje = 0;
dedu_impuestosganancias_efectivo = 0;



if(cuenta >= 500000):
    dedu_impuestosganancias_porcentaje = 11;
    dedu_impuestosganancias_efectivo = cuenta * 0.11;
    
    



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

                                cantidad_horas_faltantes =   cantidad_horas - cantidadHorasFeriados;
                                
                                pagoal50 = salarioPorHora * 1.5
                                pagoHorasExtrasNormal = pagoal50 * cantidad_horas_faltantes; 

                                remu_horas_extras = pagoHorasExtrasNormal + pagoHorasExtrasFeriados
                                
                                

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
                    
                    pagoHorasExtrasNormal = pagoal50 * cantidad_horas;
                    
                    remu_horas_extras = pagoHorasExtrasNormal;
                    
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



dedu_jubilacion_porcentaje = 11;
dedu_jubilacion_efectivo = cuenta * (dedu_jubilacion_porcentaje / 100)






os.system("clear")
dedu_aporte_sindical_porcentaje = 0;
dedu_aporte_sindical_efectivo = 0;
aporteS = input("Esta asociado a un sindicato? S/N: ")
if(aporteS.lower() == "s"):
    dedu_aporte_sindical_porcentaje = 3;
    dedu_aporte_sindical_efectivo = cuenta * (dedu_aporte_sindical_porcentaje /100)
    

debu_total_porcentaje = dedu_aporte_sindical_porcentaje + dedu_jubilacion_porcentaje + dedu_impuestosganancias_porcentaje;
debu_Total = dedu_jubilacion_efectivo + dedu_aporte_sindical_efectivo + dedu_impuestosganancias_efectivo; 
saldo_Cobrar = cuenta - debu_Total + remu_horas_extras;



os.system("clear")

print(remu_horas_extras) #7816.64
print(cantidad_horas)#8
print(debu_total_porcentaje) #14
print(debu_Total) #4020 sindi 14740jubi  18760
print(saldo_Cobrar) #123056.64

