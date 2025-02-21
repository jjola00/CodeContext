import os
import supabase
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

db_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

def get_db_client():
    return db_client 
