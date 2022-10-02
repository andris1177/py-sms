import requests

def input_output():
    print("Naponta csak egy üzenetet lehet küldeni!")
    telefonszám = input("Add meg a telefonszámot amire szeretnél üzenetet küldeni:\n->")
    üzenet = input("Add meg az üzenetet amit szeretnél küldeni\n->")
    return telefonszám, üzenet

def send(tszám, üzenet):
    válasz = requests.post('https://textbelt.com/text', {
    'phone': f'{tszám}',
    'message': f'{üzenet}',
    'key': 'textbelt',
    })

    print(válasz.json())

def main():
    tszám, üzenet = input_output()
    send(tszám, üzenet)

main()