import json
import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = '1170507053:AAEV4pYWfIerISpthd2ULz9-_36SyeCkPi0'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# messages:
welcome_message = 'Assalomu Aleykum' + '! Men Transformers Education o\'quv markazining hizmat botiman. Men sizga har hil datchiklar haqida malumot,narx-navo va o\'quv manbalar berishim mumkin. Shunchaki biror datchik, modul yoki plata nomini kiriting.'

not_found_message = 'Afsuski, siz qidirayotgan tovar tugab qolgan yoki bizga hali yetib kelmagan.'

error_message = "Nimadir noto'g'ri ketdi, iltimos qayta urunib ko'ring yoki birozdan keyin urunib ko'ring!"


file_path = "products.json" # path to .json product list
with open(file_path, "r") as read_file:
	data = json.load(read_file)

products = data['products']

@dp.message_handler(commands=['start', 'help']) # if first use or needs help:
async def welcome(message):
	await message.reply_photo('https://user-images.githubusercontent.com/64916997/84414095-eba0a880-ac2a-11ea-999a-29364be2ab21.jpg', parse_mode='html', caption=welcome_message) # greeting.


@dp.message_handler() # in all other cases
async def serve(message):
	answer = '' # predefine answer
	product = '' # predefine chosen product

	found = False # product not found yet

	for i in range(len(products)):
		if products[i]['name'] in [message.text, message.text.upper(), message.text.lower(), message.text.capitalize] and products[i]['available'] != 0:
			# if message text in products list:
			found = True # the product is now found
			product = i # choose that product
			break # brek the loop
		else:
			found = False
			continue # else, continue searching


	if found is True: # if product is found
		# create an HTML markup for the answer

		answer = '<b>' + message.text.capitalize() + '</b>' + ' mavjud. U haqida:\n\n'
		answer +=  '<b>' + 'ID: ' + '</b>' + products[product]['id'] + '\n\n' 
		answer +=  '<b>' + 'Narxi: ' + '</b>' + str(products[product]['price']) + '000so\'m.\n\n' 
		answer +=  '<b>' + 'Soni: ' + '</b>' + str(products[product]['available']) + 'ta qolgan.\n\n'
		answer +=  '<b>' + 'Ma\'lumot: ' + '</b>' + products[product]['short_info'] + '.\n\n'
		answer +=  '<b>' + 'To\'liq ma\'lumot ' + '</b>' + '<a href="' + products[i]['entire_info'] + '">bu yerda</a>' + '.'

		try:
			await message.answer_photo(products[product]['image_url'], parse_mode='html', caption=answer) # send photo
		except:
			await message.answer(error_message) # send error message
	else:
		await message.answer(not_found_message)

executor.start_polling(dp, skip_updates=True)