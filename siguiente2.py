import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QLineEdit
from siguiente3 import Siguiente3


class Siguiente2(QMainWindow):

    def __init__(self):
        super(Siguiente2, self).__init__()



        self.setWindowTitle("siguiente")
        self.setStyleSheet("background-color: #EDEDED;")

        self.ancho = 600
        self.alto = 400
        self.resize(self.ancho, self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap("imagenes/Bienvenidos.png")

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
        self.boton1.move(1045, 625)
        self.boton1.setFixedWidth(199)
        self.boton1.setFixedHeight(50)
        self.boton1.clicked.connect(self.metodo_siguiente3)

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(600)
        self.editName.move(390, 172)
        self.editName.setStyleSheet("background-color: white;")

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(600)
        self.editName.move(390, 279)
        self.editName.setStyleSheet("background-color: white;")

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(600)
        self.editName.move(390, 392)
        self.editName.setStyleSheet("background-color: white;")

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(600)
        self.editName.move(390, 530)
        self.editName.setStyleSheet("background-color: white;")

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(600)
        self.editName.move(390, 665)
        self.editName.setStyleSheet("background-color: white;")

    def metodo_siguiente3(self):
        self.hide()
        self.siguiente3 = Siguiente3()
        self.siguiente3.show()


if __name__ == '__main__' :
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo ventana1 con el nombre ventana1
    ventana = Siguiente2()

    # Hacer que el objeto ventana 1 se vea
    ventana.show()

    # Para terminar la aplicacion
    sys.exit(app.exec_())
