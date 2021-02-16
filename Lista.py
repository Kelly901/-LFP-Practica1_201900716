from Datos import Datos
import re

class Lista:
    datos = []
    sin_espacio =[]
    cadena = []
    


    def descomponer(self,texto):
        ordenar=""
        espacio=texto.split("\n")
        buscar=""
        numero=""
        
        buscar3=""
        buscar4=""
        for i in espacio:
            igual=i.split("=")
            
            texto1=igual[1]
            #Nombre de la lista es el nombre de la lista
            nombreLista=igual[0]
            
            texto2= re.split(r"[BUSCARORDENAR]",texto1)
            #texto3 es la cadena de numeros
            texto3=texto2[0]
            
            letras=re.split(texto3, texto1)
            letras2=letras[1]
            #print(letras)
            
            buscar1=letras2.split(",")
            
            #buscar=re.split(r"ORDENAR",letras2)
            if len(buscar1)==2:
                for i in range(2):
                    if buscar1[0]=="ORDENAR":
                        ordenar=buscar1[0]
                        buscar=buscar1[1]
                        
                        numero1=re.split(r"BUSCAR",buscar)
                        buscar2=re.split(r"[0-9]",buscar)
                        buscar3=re.split(r" ",buscar2[0])
                        
                        buscar4=buscar3[len(buscar3)-2]
                        
                        numero=numero1[1]
                        
                    else:
                        ordenar1=re.split(r" ",buscar1[1])
                        
                        ordenar=ordenar1[len(ordenar1)-1]
                        
                        buscar=buscar1[0]
                    
                        numero1=re.split(r"BUSCAR",buscar)
                        buscar2=re.split(r"[0-9]",buscar)
                        buscar3=re.split(r" ",buscar2[0])
                        buscar4=buscar3[0]
                        
                        numero=numero1[1]

                   

            else:
                for l in buscar1:
                    if l=="ORDENAR":
                        ordenar=l
                        buscar4=" "
                        numero=" "
                   
                    else:
                        buscar=l
                        ordenar=" "
                        numero1=re.split(r"BUSCAR",buscar)
                        buscar2=re.split(r"[0-9]",buscar)
                        buscar3=re.split(r" ",buscar2[0])
                        buscar4=buscar3[0]
                        numero=numero1[1]
            self.datos.append(Datos(nombreLista,texto3,ordenar,buscar4,numero))    
                        
                
                       


        return "---"

    def imprimir(self):
        for i in self.datos:
            print("listas --"+i.nombre +"--" + i.lista +"--"+ i.ordenar+"--" + i.buscar +"--"+ i.numero)

            