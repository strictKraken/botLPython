import os
import sqlite3
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def getRegionData():
  current_dir = os.path.dirname(os.path.abspath(__file__))
  database_path = os.path.join(current_dir, "..", "..", "db", "gazv.db")
  connection = sqlite3.connect(database_path)

  cursor = connection.cursor()
  rows = cursor.execute("select * from regions").fetchall()
  print(rows)

  keyboard = InlineKeyboardMarkup(row_width=1)

  for row in rows:
    region_id, region_name = row
    button_text = f"{region_id} {region_name}"
    callback_data = f"regionInfo-{region_id}-{region_name}"
    button = InlineKeyboardButton(text=button_text, callback_data=callback_data)
    keyboard.add(button)

  connection.close()
  return keyboard


def getRegionDataID(region_id, year):

  current_dir = os.path.dirname(os.path.abspath(__file__))
  database_path = os.path.join(current_dir, "..", "..", "db", "gazv.db")
  connection = sqlite3.connect(database_path)

  cursor = connection.cursor()
  query = "SELECT * FROM volume WHERE region_id = ? AND year = ?"
  cursor.execute(query, (region_id, year))

  rows = cursor.fetchall()

  connection.close()

  return rows

