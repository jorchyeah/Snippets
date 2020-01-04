#este programa cambia los nombres de screenshots guardados en un directorio
import os

#cambio de directorio
os.chdir('/Users/Jorch/Desktop/Nueva carpeta')

#listado de archivos
for f in os.listdir():
    f_nombre, f_ext = os.path.splitext(f)
    f_screenshot, f_feCompleta = f_nombre.split('_')
    f_fecha, f_hora = f_feCompleta.split('-')

    print('{} {}{}'.format(f_fecha,f_hora,f_ext))



