import re

from aiogram import types, Dispatcher

from assets.antispam import antispam
from commands.db import url_name
from user import BFGuser



rplist = {  # Спасибo @ x0x1dead за составление списка рп команд
	'ударить': '{} ударил(-а) {}',
	'выебать': '{} выебал(-а) {}',
	'дать пять': '{} дал(-а) пять {}',
	'испугать': '{} испугал(-а) {}',
	'извиниться': '{} извинился(-ась) перед {}',
	'изнасиловать': '{} изнасиловал(-а) {}',
	'кусь': '{} куснул(-а) {}',
	'кастрировать': '{} кастрировал(-а) {}',
	'лизнуть': '{} лизнул(-а) {}',
	'лизь': '{} лизнул(-а) {}',
	'обнять': '{} обнял(-а) {}',
	'отравить': '{} отравил(-а) {}',
	'отдаться': '{} отдался(-ась) {}',
	'поздравить': '{} поздравил(-а) {}',
	'поцеловать': '{} поцеловал(-а) {}',
	'прижать': '{} прижал(-а) {}',
	'потрогать': '{} потрогал(-а) {}',
	'пожать руку': '{} пожал(-а) руку {}',
	'послать наxуй': '{} послал(-а) наxуй {}',
	'похвалить': '{} похвалил(-а) {}',
	'понюхать': '{} понюхал(-а) {}',
	'погладить': '{} погладил(-а) {}',
	'дать по лбу': '{} дал(-а) по лбу {}',
	'пнуть': '{} пнул(-а) {}',
	'покормить': '{} покормил(-а) {}',
	'расстрелять': '{} расстрелял(-а) {}',
	'секс': '{} занялся сексом с {}',
	'сжечь': '{} сжег(-ла) {}',
	'трахнуть': '{} трахнул(-а) {}',
	'ущипнуть': '{} ущипнул(-а) {}',
	'уебать': '{} уебал(-а) {}',
	'укусить': '{} укусил(-а) {}',
	'убить': '{} убил(-а) {}',
	'шлепнуть': '{} шлепнул(-а) {}',
	'куснуть': '{} куснул(-а) {}',
	'облизать': '{} облизал(-а) {}',
	'отсосать': '{} отсосал(-а) у {}',
	'отлизать': '{} отлизал(-а) {}',
	'отпиздохать': '{} отпиздошил(-а) {}',
	'повесить': '{} повесил(-а) {}',
	'казнить': '{} казнил(-а) {}',
	'воскресить': '{} воскресил(-а) {}',
	'изыди': '{} изыдил(-а) {}',
	'пожать': '{} пожал(-а) {}',
	'съедение': '{} съел(-а) {}',
	'мандаринка': '{} мандаринку с {}',
	'фейерверк': '{} устроил фейерверк для {}',
	'санки': '{} катался на санках с {}',
	'сугроб': '{} прыгнул в сугроб с {}'
	
}




@antispam
async def rp_cmd(message: types.Message, user: BFGuser):
	if message.chat.type != 'supergroup' or not message.reply_to_message:
		return
	
	rname = await url_name(message.reply_to_message.from_user.id)
	
	action_key = re.search(pattern, message.text.lower()).group(0)
	response = rplist[action_key].format(user.url, rname)
	
	await message.answer(response)
	
	
rplist_keys = '|'.join(re.escape(key) for key in rplist.keys())
pattern = rf'\b({rplist_keys})\b'

