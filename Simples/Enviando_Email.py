import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

msg = MIMEMultipart
message = "Você Recebeu Um Email Enviado Com Python!!!  "

password = "*** Senha Do Email Que Irá Enviar***"
msg['From'] = "*** Email Que Irá Enviar***"
msg['To'] = "*** Email Que Irá Receber***"
msg['Subject'] = "Enviando Gmail Com Python "

msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(msg['From'],password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
