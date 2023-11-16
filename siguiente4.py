import sys
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
from siguiente5 import Siguiente5
from siguiente6 import Siguiente6
from siguiente7 import Siguiente7
from siguiente8 import Siguiente8


class Siguiente4(QMainWindow):

    def __init__(self, ventana3):
        super(Siguiente4, self).__init__()

        self.ventanaAnterior = ventana3;

        self.setWindowTitle("siguiente")
        self.setStyleSheet("background-color: #EDEDED;")


        self.ancho = 600
        self.alto = 400
        self.resize(self.ancho, self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap("imagenes/Tipos de acoso.png")

        # agregamos la imagen en el fondo
        self.fondo.setPixmap(self.imagenFondo)

        # establecer el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # el tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana fondo como la ventana control
        self.setCentralWidget(self.fondo)



        self.letra2 = QFont()
        self.letra2.setFamily("Arial")
        self.letra2.setPointSize(55)

        self.letra3 = QFont()
        self.letra3.setFamily("Arial")
        self.letra3.setPointSize(20)

        self.letra4 = QFont()
        self.letra4.setFamily("Arial")
        self.letra4.setPointSize(20)

        self.letra5 = QFont()
        self.letra5.setFamily("Arial")
        self.letra5.setPointSize(20)

        self.letra6 = QFont()
        self.letra6.setFamily("Arial")
        self.letra6.setPointSize(20)



        self.boton2 = QPushButton(self)
        self.boton2.setText("<")
        self.boton2.setFont(self.letra2)
        self.boton2.setStyleSheet("background-color: white; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton2.move(40, 599)
        self.boton2.setFixedWidth(110)
        self.boton2.setFixedHeight(110)

        self.boton2.clicked.connect(self.metodo_atras3)

        self.boton3 = QPushButton(self)
        self.boton3.setText("Acoso Sexual")
        self.boton3.setFont(self.letra3)
        self.boton3.setStyleSheet("background-color: #EAECEE; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton3.move(58, 270)
        self.boton3.setFixedWidth(240)
        self.boton3.setFixedHeight(60)
        self.boton3.clicked.connect(self.metodo_siguiente5)

        self.boton4 = QPushButton(self)
        self.boton4.setText("Acoso Cibernético")
        self.boton4.setFont(self.letra4)
        self.boton4.setStyleSheet("background-color: #EAECEE; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton4.move(58, 350)
        self.boton4.setFixedWidth(300)
        self.boton4.setFixedHeight(60)
        self.boton4.clicked.connect(self.metodo_siguiente6)

        self.boton5 = QPushButton(self)
        self.boton5.setText("Acoso Laboral")
        self.boton5.setFont(self.letra5)
        self.boton5.setStyleSheet("background-color: #EAECEE; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton5.move(56, 430)
        self.boton5.setFixedWidth(250)
        self.boton5.setFixedHeight(60)
        self.boton5.clicked.connect(self.metodo_siguiente7)

        self.boton6 = QPushButton(self)
        self.boton6.setText("Acoso Escolar(Bullying)")
        self.boton6.setFont(self.letra6)
        self.boton6.setStyleSheet("background-color: #EAECEE; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton6.move(54, 508)
        self.boton6.setFixedWidth(380)
        self.boton6.setFixedHeight(60)
        self.boton6.clicked.connect(self.metodo_siguiente8)

    def metodo_siguiente2(self):
        pass

    def metodo_atras3(self):
        self.hide()
        self.ventanaAnterior.show()

    def metodo_siguiente5(self):
        self.hide()
        self.siguiente5 = Siguiente5(self)
        self.siguiente5.show()

    def metodo_siguiente6(self):
        self.hide()
        self.siguiente6 = Siguiente6(self)
        self.siguiente6.show()


    def metodo_siguiente7(self):
        self.hide()
        self.siguiente7 = Siguiente7(self)
        self.siguiente7.show()

    def metodo_siguiente8(self):
        self.hide()
        self.siguiente8 = Siguiente8(self)
        self.siguiente8.show()


if __name__ == '__main__' :
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo ventana1 con el nombre ventana1
    ventana = Siguiente4()

    # Hacer que el objeto ventana 1 se vea
    ventana.show()

    # Para terminar la aplicacion
    sys.exit(app.exec_())
