import pandas as pandas
import requests

url1 = 'https://api.chat-api.com/instance409704/sendMessage?token=krz6j7h0urdw4qj1'

url2 = 'https://api.chat-api.com/instance409704/sendFile?token=krz6j7h0urdw4qj1'

nombre = "Carlos"
# myobj = {
#     "phone": "61451961237",
#     "body": f'Hola {nombre}. Soy Jorge Torres. Con tu ayuda y apoyo quiero llegar al '
#             "Congreso de la República para que juntos preservemos el legado de Antanas Mockus."
#             'Promoveremos:'
#             '✅ El respeto y cuidado de la vida.'
#             ' ✅ La cultura ciudadana.'
#             ' ✅ La educación de calidad.'
#             ' ✅ La protección ambiental.'
#             'El 13 de marzo activa tu poder ciudadano y VOTA ✏️ marcando Partido Alianza Verde'
#             '🌻 Número 110 de la Cámara de Representantes por Bogotá. 🥕'
#             'Si quieres seguir en contacto, te agradezco me agregues dentro de tus contactos.'
#             'Para no seguir recibiendo mensajes envía BAJA'
# }

with open('E:\\whatsapp-bot\\data\\foco.txt') as f:
    text = f.readlines()

myobj2 = {
    "phone": 61451961237,
    "body": text[0],
    "filename": "foco.jpeg",
    "caption": f'Hola {nombre}.'
}

# "caption": f'Hola {nombre}. Soy Jorge Torres. Con tu ayuda y apoyo quiero llegar al '
# "Congreso de la República para que juntos preservemos el legado de Antanas Mockus."
# 'El 13 de marzo activa tu poder ciudadano y VOTA ✏️ marcando Partido Alianza Verde'
# '🌻 Número 110 de la Cámara de Representantes por Bogotá. 🥕'
# 'Gracias 💚 #Verde110'
# 'Si quieres seguir en contacto, te agradezco me agregues dentro de tus contactos.'
# 'Para no seguir recibiendo mensajes envía BAJA'

x1 = requests.post(url2, data = myobj2)
print(x1.text)

print(x1.text)
