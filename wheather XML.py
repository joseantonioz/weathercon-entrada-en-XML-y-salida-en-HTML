#coding: utf-8
import requests
import webbrowser
from lxml import etree
from jinja2 import Template


ciudades = ['Almeria','Cadiz','Cordoba','Huelva','Jaen','Malaga','Sevilla']
plantilla = open("plantilla.xml","r")
xml = ''

tempemin = []
tempemax = []
viento = []
direccionviento = []

for ciudad in ciudades:


valdef = {'q': '%s,spain' % ciudadp,'mode': 'xml','units': 'metric','lang': 'sp'}
resp = requests.get('http://api.openweathermap.org/data/2.5/weather', params=p)

raiz = etree.fromstring(r.text.encode("utf-8"))


city = raiz.find("city")
city.attrib["name"]
temmin = raiz.find("temperature")
temmin2 = int(float(temmin.attrib["min"]),1)
temmax = raiz.find("temperature")
temmax2 = int(float(temmax.attrib["max"]),1)
wind = raiz.find("wind/speed")
wind2 = round(float(wind.attrib["value"]),1)
orient = raiz.find("wind/direction")
orient2 = orientacion.attrib["name"]
list_min.append(temmin2)
list_max.append(temmax2)
listspeed.append(wind2)
listorientacion.append(orient2)



for linea in plantilla
        xml += plantilla
        
        
plantillatem = Template(xtml)
plantillatem = mitemplate.render(ciudades=ciudades,temp_min=list_min,temp_max=list_max,viento=listspeed,direccion=listorientacion)
web.write(plantillatem)

webbrowser.open('plantilla.xml')
