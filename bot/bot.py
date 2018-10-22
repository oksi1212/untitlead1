import requests
import datetime


class Bot:

    def __init__(self, token):
        self.token = token
        self.api_url = "http://api.telegram/org/bot{}".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        respons = requests.get(self.api_url + method, params)
        result_json = respons.json()['result']
        return result_json

    def send_massage(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        respons = requests.post(self.api_url + method, params)
        return respons

    def get_last_update(self):
        get_results = self.get_updates()
        if len(get_results) > 0:
            return get_results[-1]
        else:
            return get_results[len(get_results)]


greet_bot = Bot("689189867:AAF5QtiGYkwgbYB0Ej6LZe40DINmN6xqEig")
greetings = ("Hello!")
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
#        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1

if __name__ == '__main__':
   try:
       main()
   except KeyboardInterrupt: exit()