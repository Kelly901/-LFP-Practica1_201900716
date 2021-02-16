import webbrowser
from Lista import Lista
from Busqueda import Busqueda
bus=Busqueda()
class GenerarArchivo:
    
    def generar_archivo(self):
       
       

        f=open('Reporte.html','w')
        palabra=""
        for dato in Lista.datos:
           
            if dato.buscar=="BUSCAR":
                palabra=palabra+"<h3>"+" BUSQUEDA POSICIONES = "+str(bus.buscar(dato.nombre,dato.lista,dato.numero))+"</h3>"

        cuerpo= """<!DOCTYPE html>
                <html lang="en">

                    <head>
                <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Reporte de Datos</title>
            <style>
            body {
            margin: 0;
            padding: 0;
            background: linear-gradient(45deg, black, #121946, #1f2841, rgb(28, 26, 44), rgb(12, 12, 12));
            background-size: cover;
            font-family: sans-serif;
            height: 100vh;
            }
            </style>
            </head>

            <body>

            <style>
            #Titulo {
            color: aliceblue;
            text-align: center;
            font-variant-caps: petite-caps;
            text-transform: capitalize;
            font-size: 55pt;

            }
            #orden{
            color: aliceblue;
            margin: 27pt;
            font-variant-caps: petite-caps;
            text-transform: capitalize;
            font-size: 28pt;

            }

            #buscar{
            color: aliceblue;
            margin: 27pt;
            font-variant-caps: petite-caps;
            text-transform: capitalize;
            font-size: 28pt;

                }
            h3{
            color: rgb(144, 190, 233);
            margin: 33pt;
            
            font-size: 17pt;
            }
            </style>
            <h1 id="Titulo">Reporte de Datos</h1>
            <h3>Ordenados</h3>
            <h2 id="orden">Datos Ordenados</h2>
            
            <h2 id=buscar>Posiciones de los datos buscados</h2>
            """+palabra+"""
            </body>

            </html>"""
        f.write(cuerpo)
        f.close()
        webbrowser.open_new_tab('Reporte.html')
      