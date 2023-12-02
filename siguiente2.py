import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QLineEdit,QMessageBox
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
        self.imagenFondo = QPixmap("imagenes/Bienvenidos.jpg")

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

        self.letra2 = QFont()
        self.letra2.setFamily("Arial")
        self.letra2.setPointSize(20)


        self.boton1 = QPushButton(self)
        self.boton1.setText("Crear")
        self.boton1.setFont(self.letra1)
        self.boton1.setStyleSheet("background-color: white; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton1.move(1045, 625)
        self.boton1.setFixedWidth(199)
        self.boton1.setFixedHeight(50)
        self.boton1.clicked.connect(self.metodo_siguiente3)

        self.editName1 = QLineEdit(self)
        self.editName1.setFixedWidth(600)
        self.editName1.move(390, 172)
        self.editName1.setStyleSheet("background-color: white;")

        self.editName2= QLineEdit(self)
        self.editName2.setFixedWidth(600)
        self.editName2.move(390, 279)
        self.editName2.setStyleSheet("background-color: white;")

        self.editName3 = QLineEdit(self)
        self.editName3.setFixedWidth(600)
        self.editName3.move(390, 392)
        self.editName3.setStyleSheet("background-color: white;")

        self.editName4 = QLineEdit(self)
        self.editName4.setFixedWidth(600)
        self.editName4.move(390, 530)
        self.editName4.setStyleSheet("background-color: white;")

        self.editName5= QLineEdit(self)
        self.editName5.setFixedWidth(600)
        self.editName5.move(390, 665)
        self.editName5.setStyleSheet("background-color: white;")



    def metodo_siguiente3(self):
        self.datosCorrectos = True

        if (
                self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Los passwords no son iguales")

            self.ventanaDialogo.exec_()

        if (
                self.nombreYapellidos.text() == ''
                or self.mail.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.numero.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe ingresar todos los campos")

            self.ventanaDialogo.exec_()

        if self.datosCorrectos:
            # Escribir los datos en binarios.
            self.file = open('datos/cliente.txt', 'ab')

            self.file.write(bytes(self.nombreYapellidos.text() + ";"
                                  + self.mail.text() + ";"
                                  + self.password.text() + ";"
                                  + self.password2.text() + ";"
                                  + self.numero.text() + "\n", encoding='UTF-8'))
            self.file.close()

            self.file = open('datos/cliente.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

        self.hide()
        self.siguiente3 = Siguiente3(self)
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
