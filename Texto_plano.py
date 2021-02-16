from tkinter import filedialog as FileDialog
from Lista import Lista

lista=Lista()

class Texto_Plano:
    
    texto=0

    def test(self):
        fichero= FileDialog.askopenfilename(title="Abrir un fichero")
        f=open(fichero,'r')
        mensaje=f.read()
        self.texto=mensaje
        lista.descomponer(mensaje)
        
        
        
        


lista.imprimir()
