# -*- coding: cp1251 -*-

import json
import telebot
import requests
import re
from collections import OrderedDict
from telebot.types import InputMediaPhoto



# ������� ����� ����������!


bot = telebot.TeleBot('1876464698:AAFTukoK361uiDmYHKFlqBPkKvA5WvrY3aM')

@bot.message_handler(content_types=['text'])
def response_to_the_command_hello_world(message):
    if message.text == '���������':
        bot.send_message(message.from_user.id, '����������:')
        with open('total_result.json', 'r', encoding='utf-8') as file:
            result = json.load(file)

            for i_hotel in result['�����']:
                name_hotel = i_hotel['�������� �����']
                address = i_hotel['�����']
                distance = i_hotel['���������� �� ������']
                price = i_hotel['����']
                photo_list = i_hotel['����']


                # #5 ���� - �������� ���������� ������ ������������
                bot.send_message(message.from_user.id, '�������� �����: {name_hotel}\n'
                                                       '�����: {address}\n'
                                                       '���������� �� ������: {distance}\n'
                                                       '��������� �� �����: {price}\n'.format(
                    name_hotel=name_hotel,
                    address=address,
                    distance=distance,
                    price=price
                ))

                # �������� ����
                bot.send_message(message.from_user.id, '*����������*:', parse_mode='MarkdownV2')
                media = []
                for i_photo in photo_list:
                    media.append(InputMediaPhoto(i_photo))
                bot.send_media_group(message.from_user.id, media)


bot.polling(none_stop=True, interval=0)