from conn import Connection


class User:
    def __init__(self):
        self.connection = Connection()
        self.cass = self.connection.db["user"]

    def insert(
            self,
            name,
            email,
            cpf,
            addresses,
            password
    ):
        document = {
            "nome": name,
            "email": email,
            "cpf": cpf,
            "end": addresses,
            "senha": password
        }

        self.cass.insert_one(document)

        print("Usuário adicionado")

    def update(
        self,
        user_id,
        name,
        email,
        cpf,
        addresses,
        password
    ):
        update_fields = {}

        if name:
            update_fields["nome"] = name
        if email:
            update_fields["email"] = email
        if cpf:
            update_fields["cpf"] = cpf
        if addresses:
            update_fields["end"] = addresses
        if password:
            update_fields["senha"] = password

        if not update_fields:
            print("Nenhum campo para atualizar.")
            return

        self.cass.update_one(
            {"_id": user_id},
            {"$set": update_fields}
        )

        print("Usuário atualizado!")
