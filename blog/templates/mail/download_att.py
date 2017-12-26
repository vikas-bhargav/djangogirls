# Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail
# Make sure you have IMAP enabled in your gmail settings.
# Right now it won't download same file name twice even if their contents are different.

import email
import getpass, imaplib
import os
import sys

EMAIL_HOST_USER = 'vikas.djangotest@gmail.com'
EMAIL_HOST_PASSWORD = 'vikas@djangotest'
EMAIL_HOST_REVEIVER = 'vikasbhargav0@gmail.com'

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')

userName = EMAIL_HOST_USER # raw_input('Enter your GMail username:')
passwd = EMAIL_HOST_PASSWORD # getpass.getpass('Enter your password: ')

try:
    print("inside try")
    imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
    typ, accountDetails = imapSession.login(userName, passwd)
    print(typ)
    print(accountDetails)
    if typ != 'OK':
        print('Not able to sign in!')


    imapSession.select('inbox')
    typ, data = imapSession.search(None, 'ALL')
    print('------------------------')
    print(typ)
    print(data)
    if typ != 'OK':
        print ('Error searching Inbox.')


    # Iterating over all emails
    for msgId in data[0].split():
        print("inside for--- ")
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
        print(typ)
        print(messageParts)
        if typ != 'OK':
            print('Error fetching mail.')

        emailBody = messageParts[0][1]
        print("emailBody: ", emailBody)
        mail = email.message_from_string((emailBody.decode('utf-8')))
        print("mail : ", mail)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                print(part.as_string())
                continue
            if part.get('Content-Disposition') is None:
                print(part.as_string())
                continue
            fileName = part.get_filename()
            print("file name: ", fileName)

            if bool(fileName):
                print("inside if")
                filePath = os.path.join(detach_dir, 'attachments', fileName)
                if not os.path.isfile(filePath) :
                    print(fileName)
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
    imapSession.close()
    imapSession.logout()
except :
    print('Not able to download all attachments.')