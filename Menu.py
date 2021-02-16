from Orden import Orden
from Texto_plano import Texto_Plano
from Busqueda import Busqueda
from GenerarArchivo import GenerarArchivo
gen=GenerarArchivo()
correr=Texto_Plano()
orden=Orden()
buscar=Busqueda()
class Menu:
    
    def menu(self):
        print(">>>>>>>>>>>>>>>Menu<<<<<<<<<<<<<<<")
        print("Escoja una opción:")
        print("1.Cargar archivo de entrada")
        print("2.Desplegar lista de ordenados")
        print("3.Desplegar busquedas")
        print("4.Desplegar todas")
        print("5.Desplegar todas a archivo")
        print("6.Salir")
        opcion= input("Ingrese su opcion ")
        self.opciones(opcion)

    def opciones(self,opcion):

        if opcion=="1":
            print("Cargar archivo de entrada")
            correr.test()
            print(correr.texto)
            print("----------")
            m.menu()
        elif opcion=="2":
            print("----------------")
            print(">>>>>>Datos ordenados<<<<<<<<<<")
            orden.ordenamiento_bublesort()
            print("------------------")
            self.menu()
            
        elif opcion=="3":
            print(">>>>>>>>>Busqueda de posicones de dato<<<<<<<<<")
            buscar.buscar_posicion()
            print("busqueda finalizada")
            print("---------------------")
            self.menu()

        elif opcion=="4":
            print(">>>>>>Desplegar todas<<<<<<<<<<")
            orden.ordenamiento_bublesort()
            print("      ")
            buscar.buscar_posicion()
            print("------------------")
            self.menu()
        elif opcion=="5":
            print("Esocgio la opcion 5")
            gen.generar_archivo()
        elif opcion=="6":
            print("Adios")
        else:
            print("---------------------")
            print("Opcion erronea")
            self.menu()                     

m=Menu()
m.menu()

