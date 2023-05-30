from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_keyboard():
  keyboard = InlineKeyboardMarkup(row_width=1)

  button1 = InlineKeyboardButton(text="Добыча газа", callback_data="getRegionsExport")
  button2 = InlineKeyboardButton(text="Экспорт газа из России", callback_data="goToExport")
  button3 = InlineKeyboardButton(text="Доходы России от экспорта природного газа", callback_data="getFullIncome")

  keyboard.add(button1, button2, button3)

  return keyboard

def exportGas_keyboard():
  keyboard = InlineKeyboardMarkup(row_width=1)

  button1 = InlineKeyboardButton(text="Данные", callback_data="getFullExport")
  button2 = InlineKeyboardButton(text="График", callback_data="getChartExport")

  keyboard.add(button1, button2, back_button())

  return keyboard

def back_button():
  keyboard = InlineKeyboardMarkup(row_width=1)

  button1 = InlineKeyboardButton(text="<<< Назад", callback_data="goBack")

  return button1


def year_keyboard(id, region_name):
  keyboard = InlineKeyboardMarkup(row_width=2)
  current_year = 2012
  end_year = 2018

  while (current_year <= end_year):
    callback_data = f"getRegionByYear-{id}-{current_year}-{region_name}"
    button = InlineKeyboardButton(text=str(current_year), callback_data=callback_data)
    keyboard.add(button)
    current_year += 1

  return keyboard
   