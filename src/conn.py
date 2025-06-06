from astrapy import DataAPIClient
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv("TOKEN")

client = DataAPIClient(token)
db = client.get_database_by_api_endpoint(
      "https://d9ef376d-b4eb-4def-a292-c2e261be2421-us-east1.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")
