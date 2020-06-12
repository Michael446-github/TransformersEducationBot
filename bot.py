import telebot as tb # pyTelegramBotAPI
import json  # for working with .json files


TOKEN = '1170507053:AAEV4pYWfIerISpthd2ULz9-_36SyeCkPi0' # bot token, tke it from botfather
bot = tb.TeleBot(TOKEN)

file_path = "products.json" # path to .json product list
with open(file_path, "r") as read_file:
	data = json.load(read_file)

products = data['products']

@bot.message_handler(commands=['start', 'help']) # if first use of needs help:
def welcome(message):
	chat_id = message.chat.id
	welcome_data = 'Assalomu Aleykum' + '! Men Transformers Education o\'quv markazining hizmat botiman. Men sizga har hil datchiklar haqida malumot,narx-navo va o\'quv manbalar berishim mumkin. Shunchaki biror datchik, modul yoki plata nomini kiriting.'
	bot.send_photo(chat_id, photo='https://user-images.githubusercontent.com/64916997/84414095-eba0a880-ac2a-11ea-999a-29364be2ab21.jpg', caption=welcome_data) # greeting.


@bot.message_handler(func=lambda message: True) # in all other cases
def serve(message):
	chat_id = message.chat.id # predefine chat id

	answer = '' # predefine answer
	product = '' # predefine chosen product
	message_text = message.text # predefine text message

	found = False # product not found yet

	for i in range(len(products)):
		if products[i]['name'] in [message_text, message_text.upper(), message_text.lower(), message_text.capitalize] and products[i]['available'] != 0:
			# if message text in products list:
			found = True # the product is now found
			product = i # choose that product
			break # brek the loop
		else:
			found = False
			continue # else, continue searching


	if found is True: # if product is found
		# create an HTML markup for the answer

		answer = '<b>' + message_text.capitalize() + '</b>' + ' mavjud. U haqida:\n\n'
		answer +=  '<b>' + 'ID: ' + '</b>' + products[product]['id'] + '\n\n' 
		answer +=  '<b>' + 'Narxi: ' + '</b>' + str(products[product]['price']) + '000so\'m.\n\n' 
		answer +=  '<b>' + 'Soni: ' + '</b>' + str(products[product]['available']) + 'ta qolgan.\n\n'
		answer +=  '<b>' + 'Ma\'lumot: ' + '</b>' + products[product]['short_info'] + '.\n\n'
		answer +=  '<b>' + 'To\'liq ma\'lumot ' + '</b>' + '<a href="' + products[i]['entire_info'] + '">bu yerda</a>' + '.'

		try:
			bot.send_photo(chat_id, photo=products[product]['image_url'], parse_mode='html', caption=answer) # send photo
		except:
			bot.send_message(chat_id, "Nimadir noto'g'ri ketdi, iltimos qayta urunib ko'ring yoki birozdan keyin urunib ko'ring!") # send error message
	else:
		answer = 'Afsuski, siz qidirayotgan tovar tugab qolgan yoki bizga hali yetib kelmagan.' # send "not found" message
		bot.send_message(chat_id, answer)


bot.polling(none_stop=True)
