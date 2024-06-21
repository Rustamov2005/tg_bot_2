# button.py  module

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(KeyboardButton("Menyu1"), KeyboardButton("Menyu2"), KeyboardButton("Menyu3"))
menu_keyboard.add(KeyboardButton("Menyu4"), KeyboardButton("Menyu5"), KeyboardButton("Menyu6"))
menu_keyboard.add(KeyboardButton("Menyu7"))
menu_keyboard.add(KeyboardButton("Menyu8"))

addresses_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
addresses_keyboard.add(KeyboardButton("1"))
addresses_keyboard.add(KeyboardButton("2"))
addresses_keyboard.add(KeyboardButton("3"))
addresses_keyboard.add(KeyboardButton("4"))
addresses_keyboard.add(KeyboardButton("Back"))

# addresses_keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True)
# addresses_keyboard1.add(KeyboardButton("1"))
# addresses_keyboard1.add(KeyboardButton("2"))
# addresses_keyboard1.add(KeyboardButton("3"))
# addresses_keyboard1.add(KeyboardButton("4"))
# addresses_keyboard1.add(KeyboardButton("Back"))
