from datetime import datetime;

fecha_actual = datetime.today().strftime("%Y-%m-%d %H:%M")
total_a_cobrar  = 0;
os.system("clear")
salario_Neto = int(input("Ingrese salario: "))
salarioTotal = salario_Neto;

os.system("clear")

dedu_impuestosganancias_porcentaje = 0;
dedu_impuestosganancias_efectivo = 0;
if(salario_Neto >= 500000):
    dedu_impuestosganancias_porcentaje = 11;
    dedu_impuestosganancias_efectivo = salarioTotal * 0.11;
    salarioTotal = salarioTotal - (salarioTotal * 0.11)



remu_horas_extras = 0;

realizoExtras = input("Realizo horas extras? S/N \n")
cantidadHoras = 0;

if(realizoExtras.lower() == "s"):
    salarioPorDia = salario_Neto / 30;
    salarioPorHora = salarioPorDia / 8;
    cantidadHoras  = int(input("Cuantas horas: "))
    pagoHorasExtras = cantidadHoras * salarioPorHora * 1.5;
    remu_horas_extras = pagoHorasExtras;


salario_Neto = salario_Neto + remu_horas_extras;
os.system("clear")




dedu_jubilacion_porcentaje = 11;
dedu_jubilacion_efectivo = salario_Neto * (dedu_jubilacion_porcentaje / 100)

salarioTotal  = salarioTotal - dedu_jubilacion_efectivo;


dedu_aporte_sindical_porcentaje = 0;
dedu_aporte_sindical_efectivo = 0;
aporteS = input("Esta asociado a un sindicato? S/N")
if(aporteS.lower() == "s"):
    dedu_aporte_sindical_porcentaje = 3;
    dedu_aporte_sindical_efectivo = salario_Neto * (dedu_jubilacion_porcentaje /100)
    salarioTotal = salarioTotal - dedu_aporte_sindical_efectivo;




total_a_cobrar = salarioTotal;
