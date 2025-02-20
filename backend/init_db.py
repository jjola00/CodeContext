from database import get_db_client

def init_db():
    db = get_db_client()
    db.table("metrics").insert({"cpu_usage": 0, "ram_usage": 0}).execute()

if __name__ == "__main__":
    init_db()
