import apiai
import json

def send_message(message):
    request = apiai.ApiAI('c8c095664331415185fd19c7b43e5d09').text_request()
    request.lang = 'ru'
    request.session_id = 'session_1'
    request.query = message
    response = json.loads(request.getresponse().read().decode('utf-8'))
    print(response['result']['fulfillment']['speech'])
    return response['result']['action']


print('Введите сообщение - или для выхода "Выход"')
message = input()
action = None
while True:
    action = send_message(message)
    if action == 'smalltalk.greetings.bye':
        break
    message = input()
