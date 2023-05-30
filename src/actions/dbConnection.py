import os
import sqlite3

def dbConnection():
  current_dir = os.path.dirname(os.path.abspath(__file__))
  database_path = os.path.join(current_dir, "..", "..", "db", "gazv.db")
  connection = sqlite3.connect(database_path)

  return connection
