# database.py
import supabase
import os

def get_db_client():
    return supabase.create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))