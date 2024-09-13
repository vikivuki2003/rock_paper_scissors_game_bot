from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_r import LEXICON_RU

router = Router()

@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])