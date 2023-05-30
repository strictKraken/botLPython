import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from src.keyboards import main_keyboard, exportGas_keyboard, back_button, year_keyboard
from src.actions.getRegionData import getRegionData, getRegionDataID
from src.actions.getExportData import getExportData
from src.actions.getIncomeData import getIncomeData

load_dotenv()


bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

default_message = "Привет! Предлагаю выбрать регион и год, что бы узнать сколько было добыто кубометров газа, за какой год и в каком регионе."

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
  keyboard = InlineKeyboardMarkup(row_width=1)
  bot.send_message(message.chat.id, default_message, reply_markup=main_keyboard()) 


# base button check 
@bot.callback_query_handler(func=lambda call: call.data == "getRegionsExport")
def handle_get_region_callback(call):
    # Handle getRegion action
    # You can implement the logic to retrieve and send region data here
    # bot.answer_callback_query(call.id, text="You clicked 'Добыча газа'")
    region_data = "Выберите год для отчета"

    bot.edit_message_text(region_data, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=getRegionData())


@bot.callback_query_handler(func=lambda call: call.data == "goToExport")
def handle_get_region_callback(call):
    # Handle getRegion action
    
    
    bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите вид данных", reply_markup=exportGas_keyboard())


# ====================
# Экспорт газа из России
@bot.callback_query_handler(func=lambda call: call.data == "getFullExport")
def handle_get_region_callback(call):
    # Handle getRegion action
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(back_button())
    data = getExportData()
    
    reply_text ="Экспорт газа из России\n"
    for item in data:
        year = item[1]
        value = item[2]
        reply_text += f"{year} г. | {value} млрд кб м\n"

    bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text=reply_text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "getChartExport")
def handle_get_region_callback(call):
    image_path = "./chart.png"
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(back_button())

    with open(image_path, "rb") as image_file:
        bot.send_photo(chat_id=call.message.chat.id, photo=image_file)

    bot.send_message(chat_id=call.message.chat.id, text="Выберите действие", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "getFullIncome")
def handle_get_region_callback(call):
    # Handle getRegion action
    # You can implement the logic to retrieve and send region data here
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(back_button())
    
    data = getIncomeData()
    
    reply_text ="Доходы России от экспорта природного газа\n"
    for item in data:
        year = item[1]
        value = item[2]
        reply_text += f"{year} г. | {value} $\n"

    bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text=reply_text, reply_markup=keyboard )


# Действие назад
@bot.callback_query_handler(func=lambda call: call.data == "goBack")
def handle_get_region_callback(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=default_message, reply_markup=main_keyboard())



@bot.callback_query_handler(func=lambda call: call.data.startswith("regionInfo"))
def handle_region_info_query(call):
    data_parts = call.data.split("-")
    region_id =  int(data_parts[1])
    region_name = data_parts[2]

    keyboard = year_keyboard(region_id, region_name)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите год", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith("getRegionByYear"))
def handle_region_by_year_query(call):
    data_parts = call.data.split("-")
    id = int(data_parts[1])
    year = int(data_parts[2])
    name = data_parts[3]
    # Call your function to handle the getRegionByYear query with the year
    # For example: getRegionByYear(int(year))
    data = getRegionDataID(int(id), int(year))
    print(f"DATA = {data}")
    
    reply_text = f"{name}\n"
    if len(data) != 0:
        year = data[0][2]
        value = data[0][3]
        reply_text +=f"{year} г. \n{value} млрд куб м"
    else:
        reply_text="Данных нет"        
    

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(back_button())
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=reply_text, reply_markup=keyboard)

bot.polling()