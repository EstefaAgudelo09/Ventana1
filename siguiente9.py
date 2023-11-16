import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QLineEdit


class Siguiente9(QMainWindow):

    def __init__(self, ventana3):
        super(Siguiente9, self).__init__()

        self.ventanaAnterior = ventana3;


        self.setWindowTitle("siguiente")
        self.setStyleSheet("background-color: #EDEDED;")


        self.ancho = 600
        self.alto = 400
        self.resize(self.ancho, self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap("imagenes/Ayuda.png")

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
        self.boton1.clicked.connect(self.metodo_atras3)

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(725)
        self.editName.move(210, 168)
        self.editName.setStyleSheet("background-color: white;")

        self.edittelefono = QLineEdit(self)
        self.edittelefono.setFixedWidth(725)
        self.edittelefono.move(210, 274)
        self.edittelefono.setStyleSheet("background-color: white;")

        self.editCuentanos1 = QLineEdit(self)
        self.editCuentanos1.setFixedWidth(725)
        self.editCuentanos1.move(210, 368)
        self.editCuentanos1.setStyleSheet("background-color: white;")

        self.editCuentanos2 = QLineEdit(self)
        self.editCuentanos2.setFixedWidth(725)
        self.editCuentanos2.move(210, 430)
        self.editCuentanos2.setStyleSheet("background-color: white;")

        self.editCuentanos3= QLineEdit(self)
        self.editCuentanos3.setFixedWidth(725)
        self.editCuentanos3.move(210, 460)
        self.editCuentanos3.setStyleSheet("background-color: white;")

        self.editCuentanos4 = QLineEdit(self)
        self.editCuentanos4.setFixedWidth(725)
        self.editCuentanos4.move(210, 490)
        self.editCuentanos4.setStyleSheet("background-color: white;")

        self.editCuentanos5 = QLineEdit(self)
        self.editCuentanos5.setFixedWidth(725)
        self.editCuentanos5.move(210, 399)
        self.editCuentanos5.setStyleSheet("background-color: white;")

    def metodo_atras3(self):
        self.hide()
        self.ventanaAnterior.show()


if __name__ == '__main__' :
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo ventana1 con el nombre ventana1
    ventana = Siguiente9()

    # Hacer que el objeto ventana 1 se vea
    ventana.show()

    # Para terminar la aplicacion
    sys.exit(app.exec_())