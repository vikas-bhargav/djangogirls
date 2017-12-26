# Python code to illustrate Sending mail from
# your Gmail account
import smtplib



EMAIL_HOST_USER = 'vikas.djangotest@gmail.com'
EMAIL_HOST_PASSWORD = 'vikas@djangotest'
EMAIL_HOST_SENDER = 'vikasbhargav0@gmail.com'

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail(EMAIL_HOST_USER, EMAIL_HOST_SENDER, message)

# terminating the session
s.quit()