import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QLineEdit
from cliente import Cliente

class Siguiente11(QMainWindow):

    def __init__(self, ventana1):
        super(Siguiente11, self).__init__()

        self.ventanaAnterior = ventana1;


        self.setWindowTitle("siguiente")
        self.setStyleSheet("background-color: #EDEDED;")


        self.ancho = 600
        self.alto = 400
        self.resize(self.ancho, self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap("imagenes/Recupera tu cuenta.png")

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

        self.letra3 = QFont()
        self.letra3.setFamily("Arial")
        self.letra3.setPointSize(20)


        self.boton1 = QPushButton(self)
        self.boton1.setText("Recordar")
        self.boton1.setFont(self.letra1)
        self.boton1.setStyleSheet("background-color: white; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton1.move(820, 635)
        self.boton1.setFixedWidth(160)
        self.boton1.setFixedHeight(40)
        self.boton1.clicked.connect(self.accion_botonRecordar)


        self.boton2 = QPushButton(self)
        self.boton2.setText("Ir a inicio")
        self.boton2.setFont(self.letra2)
        self.boton2.setStyleSheet("background-color: white; color: #4A708B;"
                                  "border-radius: 30px")
        self.boton2.move(1060, 635)
        self.boton2.setFixedWidth(160)
        self.boton2.setFixedHeight(40)
        self.boton2.clicked.connect(self.metodo_atras)

        self.editUsers = QLineEdit(self)
        self.editUsers.setFixedWidth(480)
        self.editUsers.move(160, 180)
        self.editUsers.setStyleSheet("background-color: white;")

        self.editgmail= QLineEdit(self)
        self.editgmail.setFixedWidth(480)
        self.editgmail.move(160, 268)
        self.editgmail.setStyleSheet("background-color: white;")

        self.editPass = QLineEdit(self)
        self.editPass.setFixedWidth(480)
        self.editPass.move(160, 360)
        self.editPass.setStyleSheet("background-color: white;")

        self.editConfirmar = QLineEdit(self)
        self.editConfirmar.setFixedWidth(480)
        self.editConfirmar.move(160, 460)
        self.editConfirmar.setStyleSheet("background-color: white;")

        self.edittel = QLineEdit(self)
        self.edittel.setFixedWidth(480)
        self.edittel.move(712, 195)
        self.edittel.setStyleSheet("background-color: white;")

        self.editName = QLineEdit(self)
        self.editName.setFixedWidth(480)
        self.editName.move(710, 268)
        self.editName.setStyleSheet("background-color: white;")


    def metodo_atras(self):
        self.hide()
        self.ventanaAnterior.show()

    def accion_botonRecordar(self):


       self.datosCorrectos = True


       self.ventanaDialogo.setWindowTitle("Recuperar contraseña")


       if (
               self.pregunta1.text() == '' or
               self.pregunta2.text() == '' or
               self.pregunta3.text() == ''


       ):
           self.datosCorrectos = False


           self.mensaje.setText("Para recuperar la contraseña debe buscar las"
                                "\npreguntas de verificacion. Primero ingrese su"
                                "\ndocumento y luego presione el boton 'Buscar'")


           self.ventanaDialogo.exec_()


       if (
           self.pregunta1.text() != '' and
           self.respuesta1.text() == '' and
           self.pregunta2.text() != '' and
           self.respuesta2.text() == ''
       ):
           self.datosCorrectos = False


           self.mensaje.setText("Para recuperar la contraseña debe ingresar"
                                "\nlas respuestas a cada pregunta.")


           self.ventanaDialogo.exec_()


       if (
           self.datosCorrectos
       ):
           self.file = open('datos/clientes.txt', 'rb')


           usuarios = []


           while self.file:
               linea = self.file.readline().decode('UTF-8')
               lista = linea.split(";")


               if linea == '':
                   break


               u = Cliente(
                   lista[0],
                   lista[1],
                   lista[2],
                   lista[3],
                   lista[4],
                   lista[5],
                   lista[6],
                   lista[7],
                   lista[8],
                   lista[9],
                   lista[10],
                )


               usuarios.append(u)


           self.file.close()


           existeDocumento = False


           resp1 = ''
           resp2 = ''
           passw = ''


           for u in usuarios:


               if u.documento == self.documento.text():
                   existeDocumento = True


                   resp1 = u.respuesta1
                   resp2 = u.respuesta2
                   passw = u.password


                   break


           if (
                   self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                   self.respuesta2.text().lower().strip() == resp2.lower().strip()
           ):


               self.accion_botonLimpiar()


               self.mensaje.setText("Contraseña: " + passw)


               self.ventanaDialogo.exec_()
           else:


               self.mensaje.setText("Las respuestas son incorrectas para estas"
                                    "\npreguntas de recuperacion de contraseña."
                                    "\nVuelva a intentarlo.")


               self.ventanaDialogo.exec_()


if __name__ == '__main__' :
    # Hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo ventana1 con el nombre ventana1
    ventana = Siguiente11()

    # Hacer que el objeto ventana 1 se vea
    ventana.show()

    # Para terminar la aplicacion
    sys.exit(app.exec_())