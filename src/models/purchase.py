from conn import Connection


class Purchase:
    def __init__(self):
        self.connection = Connection()
        self.cass = self.connection.db["purchase"]
        self.cass_product = self.connection.db["product"]
        self.cass_buyer = self.connection.db["user"]

    def insert(
        self,
        product_id,
        buyer_id,
        date
    ):
        product = self.cass_product.find_one({"_id": {"$eq": product_id}})
        buyer = self.cass_buyer.find_one({"_id": {"$eq": buyer_id}})

        document = {
            "produto": product,
            "comprador": buyer,
            "data": date
        }

        self.cass.insert_one(document)

        print("Compra adicionada.")

    def delete(self, purchase_id):
        self.cass.find_one_and_delete({"_id": {"$eq": purchase_id}})

        print("Compra deletada.")
