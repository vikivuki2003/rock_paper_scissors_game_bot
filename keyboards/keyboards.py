from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_r import LEXICON_RU

button_yes = KeyboardButton(text='Yes')
button_no = KeyboardButton(text='No')

yes_no_kb_builder = ReplyKeyboardBuilder()
yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

button1 = KeyboardButton(text='Rock')
button2 = KeyboardButton(text='Scissors')
button3 = KeyboardButton(text='Paper')

game_kb = ReplyKeyboardMarkup(
    keyboard=[[button1],
              [button2],
              [button3]],
    resize_keyboard=True)
