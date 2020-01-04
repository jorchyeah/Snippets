#este programa cambia los nombres de screenshots guardados en un directorio
import os

#cambio de directorio
os.chdir('/Users/Jorch/Desktop/Nueva carpeta')

#listado de archivos
for f in os.listdir():
    f_nombre, f_ext = os.path.splitext(f)
    f_screenshot, f_feCompleta = f_nombre.split('_')
    f_fecha, f_hora = f_feCompleta.split('-')

    f_fecha = f_fecha.strip()
    f_hora = f_hora.strip()

    f_fecha = f_fecha[0:4]+"-"+f_fecha[4:6]+"-"+f_fecha[6:8]
    f_hora = f_hora[0:2]+"."+f_hora[2:4]+"."+f_hora[4:6]

    f_nombre = '{} {}{}'.format(f_fecha,f_hora,f_ext)

    os.rename(f,f_nombre)



