import re
from Lista import Lista
from Datos import Datos
dato=Lista()
class Orden:

    #Prueba
    def MetodoPrueba(self):

        arreglo=['2','3','5','34']
        arreglo2=[]
        for i in arreglo:
            arreglo2.append(int(i))

        

    #Metodo de ordenamietno de burbuja
    def bubleSort(self,a):
        #Se convierte una cadena de caracteres en una lista de String
        arregloN=[]
        b=re.split(r" ",a)
        c="".join(b)
        
        arreglo=c.split(",")
        #For para convertir los numeros de una lista en enteros
        for i in arreglo:
            arregloN.append(int(i))
        
        #Longitud de la cadena
        longitud=len(arregloN)
        
        #Metodo de ordenamiento bubblesort o burbuja
        for i in range(1,longitud):
            
            for j in range(0,longitud-i):
                if arregloN[j+1]<arregloN[j]:

                    temp=arregloN[j]
                    arregloN[j]=arregloN[j+1]
                    arregloN[j+1]=temp
        #Convertir a String un arreglo de enteros
        arreglo3=[]
        for i in arregloN:
            arreglo3.append(str(i))
        #Convertir una lista en cadena
        arreglo2=",".join(arreglo3)
        
        return arreglo2

    #Metodo para obtener los datos del arreglo de objetos Datos.    
    def ordenamiento_bublesort(self):
        for dato in Lista.datos:
            if dato.ordenar=="ORDENAR":
                print(dato.nombre+": ORDENADOS ="+self.bubleSort(dato.lista))
                
        return "."        

  


