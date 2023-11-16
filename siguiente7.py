import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QLineEdit


class Siguiente7(QMainWindow):

    def __init__(self, ventana4):
        super(Siguiente7, self).__init__()

        self.ventanaAnterior = ventana4;


        self.setWindowTitle("siguiente")
        self.setStyleSheet("background-color: #EDEDED;")


        self.ancho = 600
        self.alto = 400
        self.resize(self.ancho, self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap("imagenes/Acoso laboral.png")

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
        self.letra1.setPointSize(55)


        self.boton1 = QPushButton(self)
        self.boton1.setText("<")
        self.boton1.setFont(self.letra1)
        self.boton1.setStyleSheet("background-color: white; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton1.move(40, 599)
        self.boton1.setFixedWidth(110)
        self.boton1.setFixedHeight(110)
        self.boton1.clicked.connect(self.metodo_atras4)

    def metodo_atras4(self):
        self.hide()
        self.ventanaAnterior.show()


if __name__ == '__main__' :
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo ventana1 con el nombre ventana1
    ventana = Siguiente7()

    # Hacer que el objeto ventana 1 se vea
    ventana.show()

    # Para terminar la aplicacion
    sys.exit(app.exec_())