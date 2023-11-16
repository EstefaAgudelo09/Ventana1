import sys

from siguiente2 import Siguiente2
from siguiente3 import Siguiente3
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QLineEdit


class Siguiente(QMainWindow):

    def __init__(self, parent=None):
        super(Siguiente, self).__init__(parent)



        self.setWindowTitle("siguiente")
        self.setStyleSheet("background-color: #EDEDED;")


        self.ancho = 600
        self.alto = 400
        self.resize(self.ancho, self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap("imagenes/inicio.png")

        # agregamos la imagen en el fondo
        self.fondo.setPixmap(self.imagenFondo)

        # establecer el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # el tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana fondo como la ventana control
        self.setCentralWidget(self.fondo)


        self.letra1 = QFont()
        self.letra1.setFamily("Arial")
        self.letra1.setPointSize(20)


        self.boton1 = QPushButton(self)
        self.boton1.setText("Crear")
        self.boton1.setFont(self.letra1)
        self.boton1.setStyleSheet("background-color: white; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton1.move(500, 635)
        self.boton1.setFixedWidth(280)
        self.boton1.setFixedHeight(40)
        self.boton1.clicked.connect(self.metodo_siguiente2)

        self.boton2 = QPushButton(self)
        self.boton2.setText("Iniciar sesión")
        self.boton2.setFont(self.letra1)
        self.boton2.setStyleSheet("background-color: white; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton2.move(499, 560)
        self.boton2.setFixedWidth(280)
        self.boton2.setFixedHeight(40)
        self.boton2.clicked.connect(self.metodo_iniciar_sesion)

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(780)
        self.editName.move(310, 372)
        self.editName.setStyleSheet("background-color: white;")

        self.editPass = QLineEdit(self)
        self.editPass.setFixedWidth(780)
        self.editPass.move(310, 472)
        self.editPass.setStyleSheet("background-color: white;")

    def metodo_siguiente2(self):
        self.hide()
        self.siguiente2 = Siguiente2()
        self.siguiente2.show()

    def metodo_iniciar_sesion(self):
        self.name = self.editName.text()
        self.password = self.editPass.text()

        if(self.name == "isa" and self.password == "123"):
            self.hide()
            self.siguiente3 = Siguiente3()
            self.siguiente3.show()
        else:
            print("Usuario incorrecto")
            self.editName.setText("")
            self.editPass.setText("")



if __name__ == '__main__' :
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo ventana1 con el nombre ventana1
    ventana = Siguiente()

    # Hacer que el objeto ventana 1 se vea
    ventana.show()

    # Para terminar la aplicacion
    sys.exit(app.exec_())
