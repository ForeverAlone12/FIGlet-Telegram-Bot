from PIL import Image, ImageDraw, ImageFont
import pyfiglet
import telebot
import datetime
import os

bot = telebot.TeleBot('5222611252:AAEBqNB3gOLeAYe3jWvH7lWS0rXOPe5SPIE')

@bot.message_handler(content_types=["text"])
def ge_text(message):
    text = message.text
    result = pyfiglet.figlet_format(text, font="banner")
    length = 0
    max_length = 0
    width = 0
    for letter in result:
        if letter == "\n":
            # print()
            width += 1
            if length > max_length:
                max_length = length
                length = 0
        else:
            # print(letter, end="")
            length += 1


    photo_name=text_on_img(text=result, size=300, str_lehgth=max_length, str_width=width, id=message.from_user.id)
    photo = open(photo_name, "rb")
    bot.send_photo(message.from_user.id, photo)
    #bot.send_sticker(message.from_user.id, sticker)

def text_on_img(text, size, str_lehgth, str_width, id):
    img = Image.new('RGB', (str_lehgth*2, str_width*15), color='white')
    d = ImageDraw.Draw(img)
    d.text((10, 10), text, fill='black')
    photo_name = str(id) +"/"+ datetime.datetime.now().strftime("%d_%m%_Y_%H_%M") + '.png'
    img.save(photo_name)

bot.infinity_polling()