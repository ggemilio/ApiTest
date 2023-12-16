import os
from supabase import create_client, Client

class DbClient():

    def __init__(self):
        SUPABASE_URL="https://heqseakdnctsztytvgbq.supabase.co"
        SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhlcXNlYWtkbmN0c3p0eXR2Z2JxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMjcwNTI0MCwiZXhwIjoyMDE4MjgxMjQwfQ.P4rUCwTENiNzjaT16OfIfpQQz3IKEeQbGPR7ftoDV7o"
        url: str = SUPABASE_URL
        key: str = SUPABASE_KEY
        self.supabase: Client = create_client(url, key)

    def getDataFromTable(self, table: str, column: str = "*") -> list:
        response = self.supabase.table(table).select(column).execute()
        return response.data
