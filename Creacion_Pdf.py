import pdfkit;
import jinja2;
import datosEmpleado as dem;
import calculadoraRecibo as cR;


contenido = {
             'nombre': dem.nombre,
             'apellido': dem.apellido,
             'fecha_actual':  cR.fecha_actual,
             'cuil':  dem.cuil,
             'cargo': dem.cargo,
             'puestoTrabajador': dem.puesto,
             'fechaDeIngreso': dem.año_de_ingreso,
             'añosAntiguedad': dem.añosAntiguedad,
             'salario_base': cR.cuenta,
             'remu_horas_extras': cR.remu_horas_extras,
             'cantidad_horas': cR.cantidad_horas,
             'dedu_jubilacion_porcentaje': cR.dedu_jubilacion_porcentaje,
             'dedu_jubilacion_efectivo': cR.dedu_jubilacion_efectivo,
             'dedu_impuestosganancias_porcentaje': cR.dedu_impuestosganancias_porcentaje,
             'dedu_impuestosganancias_efectivo': cR.dedu_impuestosganancias_efectivo,
             'dedu_aporte_sindical_porcentaje': cR.dedu_aporte_sindical_porcentaje,
             'dedu_aporte_sindical_efectivo': cR.dedu_aporte_sindical_efectivo,
             'debu_total_porcentaje': cR.debu_total_porcentaje,
             'debu_Total': cR.debu_Total,
             'cantidad_horas': cR.cantidad_horas,
             'info_obra_social': cR.info_obra_social,
             'debu_obra_social_porcentaje': cR.debu_obra_social_porcentaje,
             'dedu_obra_social_efectivo': cR.dedu_obra_social_efectivo,
             'total_remu': cR.total_remu,
             'saldo_Cobrar': cR.saldo_Cobrar
             }


#Lectura del directorio y template html con ninja y erea
template_loader = jinja2.FileSystemLoader('./tb_1_logicaProgramacion2/');
template_env=jinja2.Environment(loader=template_loader);

html_template = 'index.html';

template = template_env.get_template(html_template); 

input_Text = template.render(contenido);

config = pdfkit.configuration(wkhtmltopdf= '/usr/bin/wkhtmltopdf');

output_pdf = dem.nombre + dem.apellido +".pdf";


pdfkit.from_string(input_Text,output_pdf,configuration=config, css='./tb_1_logicaProgramacion2/styles.css')