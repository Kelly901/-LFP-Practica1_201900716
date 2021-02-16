import re
from Lista import Lista
from Datos import Datos
dato=Lista()
class Orden:
    #Metodo de ordenamietno de burbuja
    def bubleSort(self,a):
        b=re.split(r" ",a)
        c="".join(b)
        
        arreglo=c.split(",")
        #print(f)
        
        longitud=len(arreglo)
        print(longitud)
        cont=0
        for i in range(1,longitud):
            
            for j in range(0,longitud-i):
                if arreglo[j+1]<arreglo[j]:

                    temp=arreglo[j]
                    arreglo[j]=arreglo[j+1]
                    arreglo[j+1]=temp
                    print(arreglo)
        arreglo2=",".join(arreglo)
        
        return arreglo2

    #Metodo para obtener los datos del arreglo de objetos Datos.    
    def ordenamiento_bublesort(self):
        for dato in Lista.datos:
            if dato.ordenar=="ORDENAR":
                print(dato.nombre+": ORDENADOS ="+self.bubleSort(dato.lista))
                
        return "."        

    


