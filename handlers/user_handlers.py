import time
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_r import LEXICON_RU
from keyboards.keyboards import game_kb, yes_no_kb
from services.services import get_bot_choice, get_winner

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)
    
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)
    
@router.message(F.text == 'Yes')
async def answer_yes(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)
    
@router.message(F.text == 'No')
async def answer_no(message: Message):
    await message.answer(text=LEXICON_RU['no'])
    
@router.message(F.text.in_(['Rock', 'Scissors', 'Paper']))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'My choice is: {bot_choice}')
    winner = get_winner(message.text, bot_choice)
    time.sleep(1)
    await message.answer(text=f'The result:\n{winner}', reply_markup=yes_no_kb)
    time.sleep(2)
    await message.answer(text='Do you want to play again?')
    