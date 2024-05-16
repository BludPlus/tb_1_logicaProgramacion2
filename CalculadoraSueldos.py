import pdfkit 
import jinja2
from datetime import datetime;

try:
    print(int(input("Ingrese nombre: ")))
except ValueError:
    print("Ingrese nombre correctamente")    

