import pdfkit;
import jinja2;
import datosEmpleado as dem;
from datetime import datetime;
import calculadoraRecibo as cR;


contenido = {
             'nombre': dem.nombre,
             'apellido': dem.apellido,
             'fecha_actual':  cR.fecha_actual,
             'cuil':  dem.cuil,
             'cargo': dem.cargo,
             'puestoTrabajador': dem.puesto,
             'fechaDeIngreso': dem.fechaIngreso,
             'añosAntiguedad': dem.añosAntiguedad,
             'salario_base': cR.salario_base,
            'remu_horas_extras': cR.remu_horas_extras,
            'cantidadHoras':cR.cantidadHoras,
            'dedu_jubilacion_porcentaje': cR.dedu_jubilacion_porcentaje,
            'dedu_jubilacion_efectivo': cR.dedu_jubilacion_efectivo,
            'dedu_impuestosganancias_porcentaje': cR.dedu_impuestosganancias_porcentaje,
            'dedu_impuestosganancias_efectivo': cR.dedu_impuestosganancias_efectivo,
            'total_a_cobrar': cR.total_a_cobrar
             }

contenido = {'nombre':dem.nombre,
             'apellido':dem.apellido,
             'fecha_actual': dem.fecha_actual,
             'cuil': dem.cuil}


#Lectura del directorio y template html con ninja y erea
template_loader = jinja2.FileSystemLoader('./tb_1_logicaProgramacion2/');
template_env=jinja2.Environment(loader=template_loader);

html_template = 'index.html';

template = template_env.get_template(html_template); #ERROR 0x72dd1446fc70>

output_Text = template.render(contenido);

config = pdfkit.configuration(wkhtmltopdf= '/usr/bin/wkhtmltopdf');

output_pdf = dem.nombre + dem.apellido +".pdf";


pdfkit.from_string(output_Text,output_pdf,configuration=config, css='./tb_1_logicaProgramacion2/styles.css')