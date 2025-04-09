import importlib
from assets.logger import check_log_size
from commands.admin.module_manager import load_modules
from aiogram import executor
from assets.auto import automatisation
from commands.basic.ore.db import autokursbtc_new
from bot import dp
import sqlite3
from aiogram import types
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor


MODULES = [
    'commands.basic.property.main',
    'commands.admin.admin',
    'commands.admin.module_manager',
    'commands.admin.promo',
    'commands.admin.updater',
    'commands.admin.text_command',
    'commands.entertaining.earnings.farm.main',
    'commands.entertaining.earnings.business.main',
    'commands.entertaining.earnings.garden.main',
    'commands.entertaining.earnings.generator.main',
    'commands.entertaining.earnings.tree.main',
    'commands.entertaining.earnings.quarry.main',
    'commands.basic.balance',
    'commands.basic.status.main',
    'commands.basic.ore.main',
    'commands.help',
    'commands.entertaining.rz',
    'commands.basic.top',
    'commands.entertaining.wedlock',
    'commands.clans.main',
    'commands.games.main',
    'commands.basic.bank.main',
    'commands.entertaining.case.main',
    'commands.entertaining.earnings.garden.potions',
    'commands.basic.transfer',
    'commands.basic.rpmod',
    'commands.main',
    'commands.moderation',
]


async def main(dp):
    load_modules(dp)
    reg_handlers()
    await autokursbtc_new()
    await automatisation()


def reg_handlers():
    for module_path in MODULES:
        module = importlib.import_module(module_path)
        if hasattr(module, 'reg'):
            module.reg(dp)
      
@dp.message_handler(lambda message: message.text.lower() == "п1")
async def rules_1(message: Message):
    await message.answer("📜 <i>Пункт правил 1: 🚫 Политика, расизм запрещены. (мут 10 минут)</i>")

@dp.message_handler(lambda message: message.text.lower() == "п2")
async def rules_2(message: Message):
    await message.answer("📜 <i>Пункт правил 2: ❌ Оскорбление родителей запрещено. (бан)</i>")

@dp.message_handler(lambda message: message.text.lower() == "п3")
async def rules_3(message: Message):
    await message.answer("📜 <i>Пункт правил 3: 🔞 Контент 18+, порнография, расчленёнка запрещено. (мут 1 час)</i>")

@dp.message_handler(lambda message: message.text.lower() == "п4")
async def rules_4(message: Message):
    await message.answer("📜 <i>Пункт правил 4: 🚫 Спам и флуд категорически запрещён. (мут 30 минут)</i>")

@dp.message_handler(lambda message: message.text.lower() == "п5")
async def rules_5(message: Message):
    await message.answer("📜 <i>Пункт правил 5: 🚫 Не разводить срач в чате, иначе без разбора оба участника будут наказаны. (Наказание по решению админа и от тяжести конфликта)</i>")

@dp.message_handler(lambda message: message.text.lower() == "п6")
async def rules_6(message: Message):
    await message.answer("📜 <i>Пункт правил 6: 🚫 Любая реклама запрещена. (Бан на всегда)</i>")

@dp.message_handler(lambda message: message.text.lower() == "п7")
async def rules_7(message: Message):
    await message.answer("📜 <i>Пункт правил 7: ⛔️ Ники/стикеры/символы, которые крашат телеграм, эпилепсия, видеоматериал где громкий звук, скример. (мут 3 часа)</i>")

@dp.message_handler(lambda message: message.text.lower() == "п8")
async def rules_8(message: Message):
    await message.answer("📜 <i>Пункт правил 8: ❌ Попрошайничать и просить в долг запрещено. (мут 1 час)</i>")

@dp.message_handler(lambda message: message.text.lower() == "п9")
async def rules_9(message: Message):
    await message.answer("📜 <i>‼️ Владелец и Заместители группы вправе изменять причину, а так же время наказания для игрока без предоставления доказательств в ответ на жалобу.</i>")

@dp.message_handler(lambda message: message.text.lower() == "п10")
async def rules_10(message: Message):
    await message.answer("📜 <i>‼️P.s. по поводу рекламы, разбана пишем создателю.</i>")



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=main, skip_updates=True)
