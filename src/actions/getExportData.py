import os
import sqlite3
# from dbConnection import dbConnection
# import dbConnection


def getExportData():
  current_dir = os.path.dirname(os.path.abspath(__file__))
  database_path = os.path.join(current_dir, "..", "..", "db", "gazv.db")
  connection = sqlite3.connect(database_path)

  cursor = connection.cursor()
  rows = cursor.execute("select * from ruexport").fetchall()
  print(rows)

  connection.close()

  return rows
