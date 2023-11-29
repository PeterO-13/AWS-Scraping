import smtplib

class EmailSender:
    def __init__(self):
        self.email = 'oluwatobip324@gmail.com'
        self.password = 'P_oluwatobip@324'
        self.smtp_addr = 'smtp.gmail.com'

    def send(self, msg, email_addr):
        try:
            with smtplib.SMTP_SSL(self.smtp_addr) as conn:
                conn.login(user=self.email, password=self.password)
                conn.sendmail(from_addr=self.email, to_addrs=email_addr, msg=msg)
                print('Email sent successfully!!!')
        except:
            print('Something went wrong, please try again.')