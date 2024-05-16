import pdfkit
import jinja2
from datetime import datetime;

today_date = datetime.today().strftime('%d %b,%Y')
nombre = (input("Ingrese nombre: "))
apellido = (input("Ingrese nombre: "))
contenido = {'nombre':nombre}

#Lectura del html con ninja y erea
template_loader = jinja2.FileSystemLoader('./');
template_env=jinja2.Environment(loader=template_loader);

html_template = 'index.html';

template = template_env.get_template(html_template);

output_Text = template.render(contenido);

config = pdfkit.configuration(wkhtmltopdf= '/usr/bin/wkhtmltopdf');

output_pdf = nombre + apellido +".pdf";


pdfkit.from_string(output_Text,output_pdf,configuration=config, css='styles.css')