import smtplib
from email.message import EmailMessage
def send(con,form):
    server =smtplib.SMTP(con['server'],con['port'])
    server.starttls()
    server.login(con['from'],con['pass'])

    msg = EmailMessage()
    msg['From']     = con['from']
    msg['To']       = con['to']
    msg['Subject']  = con['subject']
    body=''
    for key,val in form.items():body+='%s : %s\n'%(key,val)
    msg.set_content(body)
    result=server.send_message(msg)
    server.quit()
    
    if result=={}:return True
    else:return False
