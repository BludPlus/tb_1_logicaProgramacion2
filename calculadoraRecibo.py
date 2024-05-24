from datetime import datetime;
import os;
fecha_actual = datetime.today().strftime("%Y-%m-%d %H:%M")


cuenta  = 0;


os.system("clear")


salario_base = int(input("Ingrese salario: "))
salarioTotal = salario_base;

os.system("clear")

dedu_impuestosganancias_porcentaje = 0;
dedu_impuestosganancias_efectivo = 0;
if(salarioTotal >= 500000):
    dedu_impuestosganancias_porcentaje = 11;
    dedu_impuestosganancias_efectivo = salarioTotal * 0.11;
    salarioTotal = salarioTotal - (salarioTotal * 0.11)



remu_horas_extras = 0;

realizoExtras = input("Realizo horas extras? S/N \n")
cantidadHoras = 0;

if(realizoExtras.lower() == "s"):
    salarioPorDia = salario_base / 30;
    salarioPorHora = salarioPorDia / 8;
    print(salarioPorHora)
    cantidadHoras  = int(input("Cuantas horas: "))
    pagoHorasExtras = cantidadHoras * salarioPorHora * 1.5;
    remu_horas_extras = pagoHorasExtras;
    

salarioTotal = salarioTotal + remu_horas_extras;
os.system("clear")




dedu_jubilacion_porcentaje = 11;
dedu_jubilacion_efectivo = salarioTotal * (dedu_jubilacion_porcentaje / 100)

salarioTotal  = salarioTotal - dedu_jubilacion_efectivo;


dedu_aporte_sindical_porcentaje = 0;
dedu_aporte_sindical_efectivo = 0;
aporteS = input("Esta asociado a un sindicato? S/N")
if(aporteS.lower() == "s"):
    dedu_aporte_sindical_porcentaje = 3;
    dedu_aporte_sindical_efectivo = salarioTotal * (dedu_jubilacion_porcentaje /100)
    salarioTotal = salarioTotal - dedu_jubilacion_efectivo;




cuenta = salarioTotal;
