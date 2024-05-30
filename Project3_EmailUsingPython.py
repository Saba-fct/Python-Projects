import smtplib
import email.message

HOST = 'smtp-mail.outlook.com'
PORT = 587
password = 'personalpassword' # App generated password b/c 2FA is enabeled (change password)


FROM_EMAIL = 'saba_din@hotmail.co.uk'
TO_EMAIL = 'najafzawar72@gmail.com'
subject = 'Testing mail'
body = 'This message is being sent using python'

# Creating Message
msg = email.message.EmailMessage()
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = subject
msg.set_content(body)

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f'[*]Echoing the Server: {status_code}, {response}')

status_code, response = smtp.starttls()
print(f'[*]Starting TLS Connection: {status_code}, {response}')

status_code, response = smtp.login(FROM_EMAIL, password)
print(f'[*]Logging in: {status_code}, {response}')

smtp.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
smtp.quit()
