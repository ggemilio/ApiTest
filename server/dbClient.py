import os
from supabase import create_client, Client
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

class DbClient():

    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)

    def getDataFromTable(self, table: str, column: str = "*") -> list:
        response = self.supabase.table(table).select(column).execute()
        return response.data
