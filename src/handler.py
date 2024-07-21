from aiogram import Router
from aiogram.types import  Message
from aiogram.filters import Command, CommandStart



from connect_reids import connect_to_redis


router = Router()

start_message = "Привет!\nЯ умею Отвечать на команды:\n/exchange, отобража стоимость указанных валют.\n/rates, отправляю актуальные курсы валют."


@router.message(Command('exchange'))
async def exchange_handler(message: Message):
    
    args = message.text.split(" ")
    print(args)
    if len(args) == 4:
        from_currency = args[1].upper() 
        to_currency = args[2].upper()
        amount = float(args[3])
        r = await connect_to_redis()
        from_rate =await r.get(from_currency)
        to_rate = await r.get(to_currency)
        await r.close()
        if from_rate and to_rate:
            result = amount * (float(to_rate.decode('utf-8')) / float(from_rate.decode('utf-8')))
            await message.answer(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        await message.answer(f'нужно указать 3 аргумента:\n1. валюту в которую переводим \n2.с какой валюты переводим \n3.количество')


@router.message(Command('rates'))
async def rates_handler(message: Message):

    rates_text = "Актуальные курсы валют:\n"
    r = await connect_to_redis()
    r_keys = await r.keys()
    for currency_code in r_keys:
        currency_rate = await r.get(currency_code)
        rates_text += f"{currency_code.decode('utf-8')}: {currency_rate.decode('utf-8')}\n"
    await r.close()
    await message.answer(rates_text)


@router.message(CommandStart)
async def comand_start_handler(message: Message):
    await message.answer(start_message)