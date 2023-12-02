class Cliente:
    def init(self, nombreYapellidos,
                 mail,
                 password,
                 password2,
                 numero,
                 ):
        self.nombreYapellidos = nombreYapellidos
        self.mail = mail
        self.password = password
        self.password2 = password2
        self.numero = numero



    def str(self):
        return f"Nombre: {self.nombreYapellidos} Documento: {self.password}"
