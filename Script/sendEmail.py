import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import MAIL_PASSWORD, MAIL


# Configurando
mail_server = 'smtp.gmail.com'
mail_port = 465
sender_address = MAIL
sender_password = MAIL_PASSWORD
receiver_address = 'vitorandre6@gmail.com'


# Enviando email
def send_mail(recipient, message):
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(mail_server, mail_port, context=context) as server:
            server.login(sender_address, sender_password)
            server.sendmail(sender_address, recipient, message)
        print("E-mail enviado com sucesso!")
    except smtplib.SMTPAuthenticationError:
        print("Erro de autenticação: Nome de usuário ou senha inválidos.")
    except smtplib.SMTPException as e:
        print(
        f"Erro ao enviar o e-mail: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


# Anexar arquivos
def add_attachment():
    pass


message = MIMEMultipart("")
message["Subject"] = "Hello from Python!"
message["From"] = sender_address
message["To"] = receiver_address

#
greeting = """\
Hello,
I'm sending you a test email because I'm learning how to send email with Python!"""


# Descrição da mensagem
body = """\
<html>
  <body>
    <p>Hello,<br> I'm sending you a test email because I'm learning how to send email with Python!
    </p>
  </body>
</html>
"""

part1 = MIMEText(greeting, "plain")
part2 = MIMEText(body, "html")

message.attach(part1)
message.attach(part2)



send_mail(receiver_address, message.as_string())
