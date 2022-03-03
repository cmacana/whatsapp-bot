import requests

url1 = 'https://api.chat-api.com/instance409704/sendMessage?token=krz6j7h0urdw4qj1'

url2 = 'https://api.chat-api.com/instance409704/sendFile?token=krz6j7h0urdw4qj1'

with open('E:\\whatsapp-bot\\data\\foco.txt') as f:
    text = f.readlines()

nombre = "Carlos"

message_body = {
    "phone": 61451961237,
    "body": f'Hola {nombre}. Soy Jorge Torres. Con tu ayuda y apoyo quiero llegar al '
            'Congreso de la República para que juntos preservemos el legado de Antanas Mockus. '
            'Si quieres seguir en contacto, te agradezco me agregues dentro de tus contactos. '
            'Para no seguir recibiendo mensajes envía *BAJA*'}

photo_body = {
    "phone": 61451961237,
    "body": text[0],
    "filename": "foco.jpeg",
    "caption": "El *13 de marzo* activa tu poder ciudadano y VOTA. Gracias 💚 #Verde110"
}

x1 = requests.post(url1, json=message_body)
x2 = requests.post(url2, json=photo_body)
print(x1.text)
print(x2.text)
