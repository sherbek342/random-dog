import requests
import time
from settings import BASE_URL, TOKEN


def send_photo(chat_id: str, photo: str) -> None:
    '''send photo to tg user'''
    url = f"{BASE_URL}{TOKEN}/sendPhoto"
    payload = {
        "chat_id": chat_id,
        "photo": photo,
        "caption": "*this is a photo*",
        "parse_mode": "MarkdownV2"
    }
    requests.get(url, params=payload)
    

def last_update() -> list[dict]:
    '''get last updates'''
    url = f"{BASE_URL}{TOKEN}/getUpdates"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result'][-1]

    return


def dog_photo() -> str:
    url = 'https://random.dog/woof.json'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['url']

    return
def cat_photo()->str:
    url = 'https://meow.senither.com/v1/random'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']['url']
def sendMessage(chat_id: str, text: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.get(url=url, params=payload)
    return response.status_code


def main():
    last_update_id = last_update()['update_id']

    while True:
        time.sleep(0.5)

        curr_update = last_update()
        messages = curr_update['message']
        if last_update_id == curr_update['update_id']:
            continue

        if messages:
            if messages.get('text'):
                if curr_update['message']['text'] == '/dog':
                    chat_id = curr_update['message']['chat']['id']
                    photo = dog_photo()
                    send_photo(chat_id, photo)

                if curr_update['message']['text'] == '/cat':
                    chat_id = curr_update['message']['chat']['id']
                    photo = cat_photo()
                    send_photo(chat_id, photo)



                    
            if messages.get('sticker') :
                chat_id = curr_update['message']['chat']['id']
                text = 'I can not read your sticker, please send me /dog or /cat!'
                sendMessage(chat_id,text)


                    
            if messages.get('voice') :
                chat_id = curr_update['message']['chat']['id']
                text = 'I can not hear your voice message, please send me /dog or /cat!'
                sendMessage(chat_id,text)


                    
            if messages.get('photo') :
                chat_id = curr_update['message']['chat']['id']
                text = 'I can not watch your photo, please send me /dog or /cat!'
                sendMessage(chat_id,text)


                    
            if messages.get('video') :
                chat_id = curr_update['message']['chat']['id']
                text = 'I can not watch your video, please send me /dog or /cat!'
                sendMessage(chat_id,text)



                    
            if messages.get('document') :
                chat_id = curr_update['message']['chat']['id']
                text = 'I can not read your file, please send me /dog or /cat!'
                sendMessage(chat_id,text)


            last_update_id = curr_update['update_id']

            

        
main()