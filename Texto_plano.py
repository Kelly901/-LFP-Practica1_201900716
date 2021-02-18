from tkinter import filedialog as FileDialog
from Lista import Lista

lista=Lista()

class Texto_Plano:
    
    texto=0

    def test(self):
        fichero= FileDialog.askopenfilename(title="Abrir un fichero")
        fi=open(fichero,'r')
        mensaje=fi.read()
        self.texto=mensaje
        lista.descomponer(mensaje)
        
        
        
        


lista.imprimir()
