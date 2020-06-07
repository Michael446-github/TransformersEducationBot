import telebot as tb

TOKEN = '1170507053:AAEV4pYWfIerISpthd2ULz9-_36SyeCkPi0'
bot = tb.TeleBot(TOKEN)

products = {
	'arduino nano': {
		'price': 40,
		'available': 10,
		'short_info': 'Arduino Nano - Arduino platalar oilasiga mansub bir kontroller. Atmega328p-u mikrokontrollerida, 8 yoki 16hz chastotada ishlaydi',
		'video_tutorial': 'https://website.org/arduino_nano',
		'image_path': './img/arduino_nano.jpg'
	},
	'arduino uno': {
		'price': 70,
		'available': 1,
		'short_info': 'Arduino Uno - Arduino platalar oilasiga mansub bir kontroller. Atmega328p-u mikrokontrollerida, 16hz chastotada ishlaydi',
		'video_tutorial': 'https://website.org/arduino_uno',
		'image_path': './img/arduino_uno.jpg'
	},
	'LCD display': {
		'price': 20,
		'available': 16,
		'short_info': 'LCD display - bu kichik bir ekrancha, u yordamida har hil matn malumot, yoki binary media chiqarishingiz mumkin',
		'video_tutorial': 'https://website.org/lcd_display',
		'image_path': './img/lcd_display.jpg'
	},
	'Servo motor': {
		'price': 15,
		'available': 13,
		'short_info': 'Servo motor - bu burilish burchagini sozlash imkoniyatiga ega kichik bir motorcha.',
		'video_tutorial': 'https://website.org/servo_motor',
		'image_path': './img/servo_motor.jpg'
	}
}

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
	chat_id = message.chat.id
	welcome_data = 'Assalomu Aleykum! Men Transformer Education o\'quv markazining hizmat botiman. Men sizga har hil datchiklar haqida malumot, narx-navo va o\'quv manbalar berishim mumkin. Shunchaki biror datchik, modul yoki plata nomini kiriting.'
	bot.send_photo(chat_id, photo=open('./img/logo.jpg', 'rb'), caption=welcome_data)

@bot.message_handler(func=lambda message: True)
def serve(message):
	chat_id = message.chat.id
	answer = ''
	message_text = message.text
	found = False
	for i in products.keys():
		if i == message_text and products[i]['available'] != 0:
			answer = '<b>' + str(message_text).capitalize() + '</b>' + ' mavjud. U haqida qisqacha malumot: \n\n<b>Narxi:</b> ' + str(products[i]['price']) + '000 so\'m' + '\n\nSoni: ' + str(products[i]['available']) + 'ta' + '\n\n<b>Malumot:</b>\n ' + str(products[i]['short_info']) + '\n\n<b>Video darslik:</b> ' + str(products[i]['video_tutorial'])
			found = True
			bot.send_photo(chat_id, photo=open(products[i]['image_path'], 'rb'), parse_mode='html', caption=answer)
			break
		else:
			answer = 'Afsuski, siz qidirayotgan tovar tugab qolgan yoki bizga hali yetib kelmagan'
	if not found:
		bot.send_message(chat_id, answer)

bot.polling(none_stop=True)