#!/usr/bin/python
import socket
import time
import os

retry = 1
delay = 7
timeout = 3

def isOpen(ip, port):
    """
    Para validar si el puerto de una direcciòn responde
    
    Args:
        ip (string): ip o dominio
        port (int): 
        
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

def checkHost(ip, port, oscomando):
    """
    Para validar si el puerto de una direcciòn responde
    
    Args:
        ip (string): ip o dominio
        port (int)
        oscommando (string): comando a ejecutar
        
        
    """
    ipup = False
    for i in range(retry):
        if isOpen(ip, port):
            ipup = True
            #break
        else:
            time.sleep(delay)
            if not oscomando == "":
                os.system(oscomando)
            #os.system('/usr/local/bin/verificaglassfish.sh')
            #os.system('/opt/glassfish-4.1-vacio/glassfish/glassfish/bin/asadmin start-domain domain1')
            #os.system('/usr/bin/systemctl stop /etc/systemd/system/payara.service')
            #os.system('/usr/bin/systemctl stop /etc/systemd/system/multi-user.target.wants/payara.service')
            #os.system('/opt/payara/payara5/bin/asadmin start-domain --user admin --passwordfile/usr/local/bin/pass-payara.txt domain1')
    return ipup
"""
if checkHost(ip, port):
    print("")
    #print ip + " is UP"
"""  