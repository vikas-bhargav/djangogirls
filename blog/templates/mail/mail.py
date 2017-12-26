import smtplib
import time
import imaplib
import email

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
EMAIL_HOST_USER = 'vikas.djangotest@gmail.com'
EMAIL_HOST_PASSWORD = 'vikas@djangotest'

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = EMAIL_HOST_USER
FROM_PWD    = EMAIL_HOST_PASSWORD
SMTP_SERVER = "imap.gmail.com"
# SMTP_PORT   = 993

def read_email_from_gmail():
    # try:
    print("try")
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    print("type:", type, "data: ", data)
    mail_ids = data[0]
    print(mail_ids)

    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    print(first_email_id, "::::", latest_email_id)
    print("fffffffff")
    resp, items = mail.search(None, "ALL")
    items = items[0].split() # getting the mails id

    for emailid in items:
        print("inside for ")
        resp, data = mail.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
        # print(resp, data)
        email_body = data[0][1] # getting the mail content
        mail = email.message_from_string(str(email_body)) # parsing the mail content to get a mail object
        print(mail)
        for response_part in data:
            print(response_part)
            if isinstance(response_part, tuple):
                print("response_part[0]:", response_part[0])
                print("response_part[1]:", response_part[1])
                # print("response_part[2]:", response_part[2])
                msg = email.message_from_string(str(response_part[1]))
                print("msg: ", msg)
                email_subject = msg['subject']
                email_from = msg['from']
                print('From : ' + str(email_from) + '\n')
                print('Subject : ' + str(email_subject) + '\n')


    # for i in range(latest_email_id,first_email_id, -1):
    #     print("for: ",bytes(i))
    #     typ, data = mail.fetch(bytes(i), "(RFC822)")
    #     print("inside for:",i)
    #     print("type:", type, "data: ", data)
    #
    #     for response_part in data:
    #         print(response_part)
    #         if isinstance(response_part, tuple):
    #             msg = email.message_from_string(response_part[1])
    #             email_subject = msg['subject']
    #             email_from = msg['from']
    #             print('From : ' + email_from + '\n')
    #             print('Subject : ' + email_subject + '\n')

    # except Exception as e:
    #     print("except")
    #     print(str(e))


read_email_from_gmail()