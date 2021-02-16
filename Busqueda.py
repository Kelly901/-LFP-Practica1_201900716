import re
from Lista import Lista
class Busqueda:

    def buscar(self,nombre,lista,numero):
        
        num=re.split(r" ",numero)
        n=num[len(num)-1]
        
        b=re.split(r" ",lista)
        c="".join(b)
        
        arreglo=c.split(",")
        
        #print(f)
        b=[]
        cont=0
        for i in arreglo:
            cont=cont+1
            if i==n:
                
                b.append(cont)
        if len(b)==0:
            return nombre+": "+lista +"BUSQUEDA: "+ n +" POSICIONES = NO ENCONTRADO"        
                
        return nombre+": "+lista+" BUSQUEDA POSICIONES = ",b

        
    

    def buscar_posicion(self):
        
        for dato in Lista.datos:
           
            if dato.buscar=="BUSCAR":
                
                print(self.buscar(dato.nombre,dato.lista,dato.numero))
                
        return "."