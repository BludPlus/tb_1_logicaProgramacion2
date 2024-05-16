import pdfkit;
import jinja2;
import Calculadora_Sueldos as cs;
from datetime import datetime;


contenido = {'nombre':cs.nombre,'apellido':cs.apellido, 'fecha_actual': cs.fecha_actual}

#Lectura del html con ninja y erea
template_loader = jinja2.FileSystemLoader('./');
template_env=jinja2.Environment(loader=template_loader);

html_template = 'index.html';

template = template_env.get_template(html_template);

output_Text = template.render(contenido);

config = pdfkit.configuration(wkhtmltopdf= '/usr/bin/wkhtmltopdf');

output_pdf = cs.nombre + cs.apellido +".pdf";


pdfkit.from_string(output_Text,output_pdf,configuration=config, css='styles.css')