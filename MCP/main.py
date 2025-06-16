# main.py
from db import initialize_db
from api import mcp

if __name__ == "__main__":
    initialize_db()  
    mcp.run()
