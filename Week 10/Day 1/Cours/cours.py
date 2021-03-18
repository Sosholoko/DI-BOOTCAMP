
import requests
import time

current_id = 0

token = "1653597939:AAGIz2snnqmQg9FE2ZD1alzjvZypR5dIlDo"



#get_me = method_url + "/getMe"

#r = requests.get(get_me)

#print(r.text)

def get_messages(offset):
    get_updates = f"https://api.telegram.org/bot{token}/getUpdates"
    r = requests.get(get_updates, params={"offset": offset+1}) # Making a request

    return r.json() # Converts the response to a dictionary


#message_send = f"https://api.telegram.org/bot{token}/sendMessage"
#Time

while True:
    # Check for new messages
    msgs = get_messages(current_id)

    for update in msgs['result']:
        current_id = update['update_id']

        content = update["message"]["text"]
        user_id = update["message"]["from"]["id"]
        if content == "/WhatsYourName":
            send_message = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.get(send_message, params={"chat_id":user_id, "text":"Sasha !"})
        elif content == "/sasha":
            send_message = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.get(send_message, params={"chat_id":user_id, "text":"21 years old !"})
        else:
            send_message = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.get(send_message, params={"chat_id":user_id, "text":"I don't understand, sorry"})

        print(content)

    # Sleep 2s
    time.sleep(2)

