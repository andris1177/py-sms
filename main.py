import requests

class Send_sms:
    def __init__(self):
        print("You can only send one message daily")
        self.number = input("Phone number: ")
        self.message = input("Message: ")
        self.send()

    def send(self):
        self.response = requests.post("https://textbelt.com/text", 
        {
            'phone': f'{self.number}',
            'message': f'{self.message}',
            'key': 'textbelt',
        })

        print(self.response.json)

send_sms = Send_sms()