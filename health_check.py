#!/usr/bin/env python3

##
import os
import socket
import shutil
import psutil
from datetime import datetime
import telegramio
import valida_port
from dotenv import load_dotenv, find_dotenv
#import platform
load_dotenv(find_dotenv()) #Lee el archivo local .env

TOKEN = os.environ.get("BOT_API_KEY")
IDGio = os.environ.get("TEL_GIO_KEY")
IDVlipcodeg = os.environ.get("TEL_VLI_KEY")
Ipodominio = os.environ.get("IP_DOMI_KEY")
path1 = "/"
path2 = "/home"
path3 = "/var"
###
IDusar = IDGio
#

#lista d tuplas puerto(int), descripcion , comando start
ListPuertos = [(5432, "postgres", "/usr/bin/systemctl start postgresql-12.service"), (443, "Nginx", "/usr/bin/systemctl nginx.service"), (4848, "Payara", "/usr/bin/systemctl start payara.service"), (21, "vsftp", "/usr/bin/systemctl vsftpd.service"), (5858, "Glassfish", "/opt/glassfish-4.1-vacio/glassfish/glassfish/bin/asadmin start-domain domain1"]



"""
cpu_porcentaje = psutil.cpu_percent(4)

if cpu_porcentaje < 80:
    print ("cpu menos de 80% :" )
else:
    print ("cpu más de 80% :")
print(cpu_porcentaje)    
print("-.-.-.-.")


disco_usado = shutil.disk_usage(path).used
print(disco_usado)
disco_free = shutil.disk_usage(path).free
print(disco_free)
disco_total = shutil.disk_usage(path).total
print(disco_total)
porcentaje_disco = disco_free * 100 / disco_total
if porcentaje_disco < 20:
    print ("disco libre menos de 20%")
else:
    print ("disco libre más de 20%")


print("-.-.-.-.")

memoria = psutil.virtual_memory()
print(memoria)
memoria_total = psutil.virtual_memory().total
print(memoria_total)
memoria_available = psutil.virtual_memory().available
print(memoria_available)
memoria_available_MB = memoria_available/1024/1024
if memoria_available_MB < 500:
    print ("memoria disponible menos de 500MB")
else:
    print ("memoria disponible más de 500MB")
print(memoria_available_MB)
"""

def check_cpu():
    """
    Obtiene porcenaje si mayor al 80%
    """
    cpu_porcentaje = psutil.cpu_percent(1)
    return cpu_porcentaje < 80

def check_disco():
    """
    Obtiene porcenaje de partición si mayor al 80%
    """
    disco = shutil.disk_usage(path1)
    porcentaje_disco_free = disco.free * 100.0 / disco.total
    return porcentaje_disco_free > 20 

def check_memoria():
    """
    Obtiene porcenaje de memoria si mayor al 80%
    """
    memoria_available = psutil.virtual_memory().available
    #memoria_available_MB = memoria_available/1024.0/1024.0
    memoria_total = psutil.virtual_memory().total
    porcentaje_memora_libre = memoria_available * 100.00 / memoria_total
    #print(porcentaje_memora_libre)
    return porcentaje_memora_libre > 20

def check_localhost():
    """
    Para  pruebas
    """
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def envia_mensaje(Mensaje):
    """
    Evnia mensaje acorde a item en servidor a validar por meido de telegram
    """
    tl = telegramio
    nombre = socket.gethostname()
    extra_data = ""
    TMensaje = Mensaje + ", en servidor " + str(nombre) + " " + getip() + " con fecha: " + fecha() + extra_data
    tl.envio_mensaje(TOKEN, IDusar, TMensaje)
    #print(email)
    
def fecha():
    """
    Genera la fech actual.
    """
    hoy = datetime.today()
    shoy = str(hoy)
    return shoy

def getip():
    """
    Obtienen la ip del servidor
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.0.0.0', 0))
    sip = (s.getsockname()[0])
    return sip

def validapuerto(Ipodominio, ListPuertos):
    """
    Valida si un porto esta en escucha acorde a una lista proporcionada
    """
    cont=0
    vp = valida_port
    for servicio in ListPuertos:
        #print(ListPuertos[cont])
        elvp = vp.checkHost(Ipodominio, ListPuertos[cont][0], ListPuertos[cont][2])
        if not elvp:
            Mensaje1 = "Error en puerto: "
            Mensaje = Mensaje1 + str(ListPuertos[cont][0]) + " del servicio " + ListPuertos[cont][1]
            #print(Mensaje)
            envia_mensaje(Mensaje)
        
        cont += 1
    return elvp


#########
if not check_cpu():
    Mensaje = "Error uso de cpu mayor al 80%"
    #print(subject)
    envia_mensaje(Mensaje)

if not check_disco():
    Mensaje = "Error espacio disponible de disco {} menor al 20%".format(path1)
    #print(subject)
    envia_mensaje(Mensaje)

if not check_memoria():
    Mensaje = "Error memoria disponible menos de 20%"
    #print(subject)
    envia_mensaje(Mensaje)
    
if not check_localhost():
    Mensaje = "Error localhost no puede ser resuelto a 127.0.0.1"
    #print(subject)
    envia_mensaje(Mensaje)

if not validapuerto(Ipodominio, ListPuertos):
    #Mensaje = "Error puerto "
    #print(subject)
    #envia_mensaje(Mensaje)
    print("")
    
#ff = fecha()
#nombre = socket.gethostbyname(socket.gethostname())
#nombre = platform.node()
#print(nombre)


 
