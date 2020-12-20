def send_email(subject, message, recipient, mail_type="html"):
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(app.config["MAIL_SETTINGS"]["HOST"], app.config["MAIL_SETTINGS"]["PORT"], context=context) as server: 
        server.login(app.config["MAIL_SETTINGS"]["SENDER"], app.config["MAIL_SETTINGS"]['PASSWORD'])
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = app.config['MAIL_SETTINGS']['SENDER']
        msg['To'] = recipient 

        
        if mail_type == 'html':
            msg.attach(MIMEText(message, 'html'))
        else:
            msg.attach(MIMEText(message, 'plain'))

        server.sendmail(app.config['MAIL_SETTINGS']['SENDER'], recipient, msg.as_string())
