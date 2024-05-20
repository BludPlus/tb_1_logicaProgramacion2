import pdfkit;
import jinja2;
import datosEmpleado as dem;
from datetime import datetime;


contenido = {'nombre':dem.nombre,
             'apellido':dem.apellido,
             'fecha_actual': dem.fecha_actual,
             'cuil': dem.cuil}

#Lectura del directorio y template html con ninja y erea
template_loader = jinja2.FileSystemLoader('./');
template_env=jinja2.Environment(loader=template_loader);

html_template = 'index.html';

template = template_env.get_template(html_template); #ERROR 0x72dd1446fc70>

output_Text = template.render(contenido);

config = pdfkit.configuration(wkhtmltopdf= '/usr/bin/wkhtmltopdf');

output_pdf = dem.nombre + dem.apellido +".pdf";


pdfkit.from_string(output_Text,output_pdf,configuration=config, css='styles.css')