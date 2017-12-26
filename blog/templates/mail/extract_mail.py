import imaplib
import email
from email.parser import Parser

#
EMAIL_HOST_USER = 'vikas.djangotest@gmail.com'
EMAIL_HOST_PASSWORD = 'vikas@djangotest'
EMAIL_HOST_REVEIVER = 'vikasbhargav0@gmail.com'

# Create Connection
mail = imaplib.IMAP4_SSL('imap.gmail.com')

mail.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

mail.list() # Lists all labels in GMail
mail.select('inbox') # Connected to inbox.

# result, data = mail.uid('search', None, "ALL")
result, data = mail.uid('search', None, '(HEADER Subject "327778")')
# search and return uids instead
i = len(data[0].split()) # data[0] is a space separate string
print("data: ", data)
print("result: ",result)
print("i: ", i)
for x in range(i):
    latest_email_uid = data[0].split()[x] # unique ids wrt label selected
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    # result, email_data = mail.uid('search', None, '(HEADER Subject "My Search Term")')
    # fetch the email body (RFC822) for the given ID
    raw_email = email_data[0][1]
    print("raw_email: ", raw_email)
    raw_email_string = raw_email.decode('utf-8')
    # converts byte literal to string removing b''
    email_message = email.message_from_string(raw_email_string)
    # this will loop through all the available multiparts in mail
    for part in email_message.walk():
        if part.get_content_type() == "text/plain": # ignore attachments/html
            body = part.get_payload(decode=True)
            save_string = "e.eml"# str("D:Dumpgmailemail_" + str(x) + ".eml")
            # location on disk
            myfile = open(save_string, 'a')
            print(body.decode('utf-8') + "\n\n\n")
            myfile.write(body.decode('utf-8'))
            # body is again a byte literal
            myfile.close()
        else:
            continue