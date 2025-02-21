import os
import supabase
from dotenv import load_dotenv

load_dotenv()

def get_db_client():
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    return supabase.create_client(SUPABASE_URL, SUPABASE_KEY)