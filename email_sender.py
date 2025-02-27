import smtplib
import ssl 
from email.message import EmailMessage
from loader import config

def send_message():
    msg = EmailMessage()

    subject = "Новый функционал!"
    message = '''
    Добавлена функция сохранения некоторых данных, посчитанных за последний день в гугл таблицу.
    В таблцие представлена информация о:
    количестве run-ов за день;
    количестве submit-ов за день;
    количестве успешных submit-ов за день;
    проценте успешных submit-ов;
    уникальных пользователей, проявивших активность за день;
    самую популярную задачу за день;
    количество решений самой популярной задачи.
    С таблицей можно ознакомиться по ссылке 
    https://docs.google.com/spreadsheets/d/1-CYI-SYwxuul-ICKIJuirxyUKOsdCADDcBCeb6MFXUs/edit?usp=sharing
    Таблица обновляется каждый день в полночь.
    '''

    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = config.email.login
    msg['To'] = "nighpavel@yandex.ru"  
    
    smtp_server = 'smtp.mail.ru'
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(config.email.login, config.email.password)
        server.send_message(msg)
