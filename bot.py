import logging

from aiogram import Bot, Dispatcher, executor

from client import Client

client = Client()

logging.basicConfig(level=logging.INFO)

TOKEN = client.get("/constants/TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message):
    await message.reply_photo(
        client.get("/constants/WELCOME_PHOTO"),
        parse_mode='html', caption=client.get("/constants/WELCOME"))


@dp.message_handler()
async def serve(message):
    products = client.get("/products")
    product_index = -1
    found = False

    for i in range(len(products)):
        match = message.text.lower()

        if products[i]['name'] == match:
            found = True
            product_index = i
            break
        else:
            found = False
            continue

    if found is True:
        product = products[product_index]
        answer = client.get("/constants/TEMPLATE").format(message.text.capitalize, product["id"], product["price"],
                                                          product["available"], product["short_info"],
                                                          product["entire_info"])
        try:
            await message.answer_photo(products[product_index]['image_url'], parse_mode='html',
                                       caption=answer)
        except:
            await message.answer(client.get("/constants/ERROR"))
    else:
        await message.answer(client.get("/constants/NOT_FOUND"))


executor.start_polling(dp, skip_updates=True)
