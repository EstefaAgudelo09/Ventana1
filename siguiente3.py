import sys
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
from siguiente4 import Siguiente4
from siguiente9 import Siguiente9
from siguiente10 import Siguiente10


class Siguiente3(QMainWindow):

    def __init__(self, parent=None):
        super(Siguiente3, self).__init__()

        self.ventana2 = Siguiente3

        self.setWindowTitle("siguiente")
        self.setStyleSheet("background-color: #EDEDED;")


        self.ancho = 600
        self.alto = 400
        self.resize(self.ancho, self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap("imagenes/Menu.png")

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
        self.boton1.setText("Información")
        self.boton1.setFont(self.letra1)
        self.boton1.setStyleSheet("background-color: #EAECEE; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton1.move(180, 290)
        self.boton1.setFixedWidth(220)
        self.boton1.setFixedHeight(60)
        self.boton1.clicked.connect(self.metodo_siguiente4)

        self.boton2 = QPushButton(self)
        self.boton2.setText("Ayuda")
        self.boton2.setFont(self.letra1)
        self.boton2.setStyleSheet("background-color: #EAECEE; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton2.move(870, 290)
        self.boton2.setFixedWidth(220)
        self.boton2.setFixedHeight(60)
        self.boton2.clicked.connect(self.metodo_siguiente9)

        self.boton3 = QPushButton(self)
        self.boton3.setText("Consejos")
        self.boton3.setFont(self.letra1)
        self.boton3.setStyleSheet("background-color: #EAECEE; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton3.move(540, 538)
        self.boton3.setFixedWidth(220)
        self.boton3.setFixedHeight(60)

        self.boton3.clicked.connect(self.metodo_siguiente10)

    def metodo_siguiente4(self):
        self.hide()
        self.siguiente4 = Siguiente4(self)
        self.siguiente4.show()

    def metodo_siguiente9(self):
        self.hide()
        self.siguiente9 = Siguiente9(self)
        self.siguiente9.show()

    def metodo_siguiente10(self):
        self.hide()
        self.siguiente10 = Siguiente10(self)
        self.siguiente10.show()

if __name__ == '__main__' :
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo ventana1 con el nombre ventana1
    ventana = Siguiente3()

    # Hacer que el objeto ventana 1 se vea
    ventana.show()

    # Para terminar la aplicacion
    sys.exit(app.exec_())
