from conn import Connection


class Seller:
    def __init__(self):
        self.connection = Connection()
        self.cass = self.connection.db["seller"]

    def insert(
            self,
            name,
            email,
            cpf,
            cnpj,
            password,
            addresses
    ):
        document = {
            "nome": name,
            "email": email,
            "cpf": cpf,
            "cnpj": cnpj,
            "senha": password,
            "end": addresses
        }

        self.cass.insert_one(document)

        print("Vendedor adicionado.")
