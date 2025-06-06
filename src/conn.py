from astrapy import DataAPIClient
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv("TOKEN")


class Connection:
    def __init__(self):
        try:
            self.client = DataAPIClient(token)
            self.db = self.client.get_database_by_api_endpoint(
                    "https://d9ef376d-b4eb-4def-a292-c2e261be2421-us-east1."
                    "apps.astra.datastax.com"
            )
        except:
            print("Um erro aconteceu ao tentar conectar ao astradb")
