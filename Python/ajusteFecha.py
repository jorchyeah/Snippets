#este programa cambia los nombres de screenshots guardados en un directorio
import os
from sys import argv, exit

#comprueba que no falten argumentos
if len(argv) < 2:
    print("Modo de uso: python ajusteFecha.py directorio_de_archivos_a_cambiar")
    exit(1)

#cambio de directorio a la dirección indicada en el argumento
os.chdir(argv[1])

#listado de archivos en ese directorio
for f in os.listdir():
    #divide el string antes y después de algún punto, guión o guión bajo
    f_nombre, f_extension = os.path.splitext(f)
    f_screenshot, f_fechaCompleta = f_nombre.split('_')
    f_fecha, f_hora = f_fechaCompleta.split('-')

    #elimina espacios al final del string
    f_fecha = f_fecha.strip()
    f_hora = f_hora.strip()

    #da formato al string
    f_fecha = f_fecha[0:4]+"-"+f_fecha[4:6]+"-"+f_fecha[6:8]
    f_hora = f_hora[0:2]+"."+f_hora[2:4]+"."+f_hora[4:6]

    #arma un nuevo string juntando los strings anteriores
    f_nombre = '{} {}{}'.format(f_fecha,f_hora,f_extension)

    #cambia el nombre del archivo al nuevo string
    os.rename(f,f_nombre)
