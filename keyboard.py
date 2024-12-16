
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
kb.row(button, button_2)
kb.add(button_3)

Inline = InlineKeyboardMarkup(resize_keyboard=True)
button4 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data="calories")
button5 = InlineKeyboardButton(text='Формулы расчета', callback_data="formulas")
Inline.row(button4, button5)

Inline2 = InlineKeyboardMarkup(resize_keyboard=True)
button6 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button7 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button8 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button9 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
Inline2.row(button6, button7, button8, button9)
