import pandas as pandas
import requests
import time

url1 = 'https://api.chat-api.com/instance409704/sendMessage?token=krz6j7h0urdw4qj1'

url2 = 'https://api.chat-api.com/instance409704/sendFile?token=krz6j7h0urdw4qj1'

myobj = {
    "phone": "61451961237",
    "body": "Hola Carlos Andres, Soy Jorge Torres, del equipo de Antanas Mockus 🌻💚.  "
            "Llevo más de 20 años trabajando junto *al  profe 👨‍🏫 * por la cultura ciudadana y la protección de la vida en                  Colombia."
            "En algún momento nos diste tu contacto, y es por eso que te escribimos este mensaje.🤓   "
            "Nos gustaría saber cual es tu tema de interés para mejorar en Bogotá. "
            "Responde con la palabra TEMA para continuar nuestra conversación.   "
            "Activa tu poder ciudadano este 13 de marzo  "
            "¡Gracias por creer! #Verde110 🌻🥕  https://www.jorge-torres-comunidad.com/  "
            "Si quieres seguir en contacto, te agradezco me agregues dentro de tus contactos. "
            "Para no seguir recibiendo mensajes envía BAJA"
}

with open('E:\\whatsapp-bot\\data\\foco.txt') as f:
    text = f.readlines()

df = pandas.read_csv("E:\\whatsapp-bot\\data\\contacto_de_prueba.csv")

for index, contact in df.iterrows():
    time.sleep(10)
    print(contact['nombre'])
    print(contact['movil'])

    caption = "Hola " + contact['nombre'] + "."
    phone = contact['movil']

    myobj2 = {
        "phone": phone,
        "body": text[0],
        "filename": "foco.jpeg",
        "caption": caption
    }

    #x1 = requests.post(url1, data = myobj)
    x2 = requests.post(url2, json=myobj2)
    #print(x2.text)

    print(x2.text)
