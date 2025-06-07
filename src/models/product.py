from conn import Connection


class Product:
    def __init__(self):
        self.connection = Connection()
        self.cass = self.connection.db["product"]
        self.cass_seller = self.connection.db["seller"]

    def insert(
        self,
        name,
        price,
        seller_id
    ):
        seller = self.cass_seller.find_one({"_id": {"$eq": seller_id}})
        document = {
            "nome": name,
            "preco_unitario": price,
            "vendedor": seller
        }

        self.cass.insert_one(document)

        print("Produto adicionado.")

    def search(self, name):
        entries = self.cass.find({"nome": {"$eq": name}})
        for entry in entries:
            name = entry["nome"]
            price = entry["preco_unitario"]
            seller = entry["vendedor"]["nome"]
            yield f"Nome: {name}\nPreço: {price}\nVendedor: {seller}"
