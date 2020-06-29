#!/usr/bin/env python3

import subprocess as sp

""" 
Usamos una lista para los equipos que vamos a recorrer.  
Esto sería mejor tenerlo en un archivo de configuración, poder pasarlo por
parámetros, o ambas.
"""
ips = [ "192.168.30.1", "192.168.30.114", "192.168.30.44" ]
# E inicializamos un diccionario en blanco para los resultados.
results = {}

# Recorremos las ip de la lista,
for ip in ips:
  # averiguamos si se le puede hacer ping a cada una de ellas,
  status,result = sp.getstatusoutput("ping -c1 -w2 " + ip)
  # y metemos en el diccionario cada resultado, asociándolo a la ip
  results[ip]=status

"""
Al terminar de ejecutarse el ciclo anterior, terminamos con un diccionario
de esta forma:
  {
    "ip1": resultado1,
    "ip2": resultado2,
    ...
    "ipN": resultadoN
  }
  
  Nada más lo recorremos e imprimimos los resultados, pero nada nos impide
  usar la información de alguna otra manera.
""" 
for system in results.keys():
  if results[system] == 0:
    print("System " + system + " is UP !")
  else :
    print("System " + system + " is DOWN !")
