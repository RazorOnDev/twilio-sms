from twilio.rest import Client



# Autenticación

account_sid = 'PASTE_HERE_YOUR_ACC_SID_FROM_TWILIO'

auth_token = '[AuthToken]'

client = Client(account_sid, auth_token)



# Solicitar entradas del usuario

from_number = input("Introduce el número de teléfono de Twilio (con prefijo): ")

to_number = input("Introduce el número de teléfono destinatario (con prefijo): ")

mensaje = input("Introduce el mensaje: ")



# Crear y enviar el mensaje

message = client.messages.create(

  from_=from_number,

  body=mensaje,

  to=to_number

)



# Imprimir el SID del mensaje

print(f"Mensaje enviado con SID: {message.sid}")

