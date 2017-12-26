import email, getpass, imaplib, os

EMAIL_HOST_USER = 'vikas.djangotest@gmail.com'
EMAIL_HOST_PASSWORD = 'vikas@djangotest'


detach_dir = '.' # directory where to save attachments (default: current)
user = EMAIL_HOST_USER # input("Enter your GMail username:")
pwd = EMAIL_HOST_PASSWORD # getpass.getpass("Enter your password: ")

# connecting to the gmail imap server
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("inbox") # here you a can choose a mail box like INBOX instead
# use m.list() to get all the mailboxes

resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
items = items[0].split() # getting the mails id

for emailid in items:
    print("inside for ")
    resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
    # print(resp, data)
    email_body = data[0][1] # getting the mail content
    mail = email.message_from_string(str(email_body)) # parsing the mail content to get a mail object
    print(mail)

    #Check if any attachments at all
    if mail.get_content_maintype() != 'multipart':
        print("multipart: ", mail.walk())

        pass
    # print("mail.walk(): ", mail.walk())
    # print(type(mail["From"]), type(mail["Subject"]))
    #
    # print("["+mail["From"]+"] :" + mail["Subject"])

    # we use walk to create a generator so we can iterate on the parts and forget about the recursive headach
    for part in mail.walk():
        print("part : ", part)
        # multipart are just containers, so we skip them
        if part.get_content_maintype() == 'multipart':
            pass

        # is this part an attachment ?
        if part.get('Content-Disposition') is None:
            pass

        #filename = part.get_filename()

        filename = 'd1.txt'# mail["From"] + "_hw1answer"
        print("file name : ", filename)
        print("part.get_payload(decode=True): ", part.get_content_maintype())

        att_path = os.path.join(detach_dir, filename)
        # finally write the stuff
        fp = open('d.txt', 'wb')
        fp.write(part.get_payload(decode=True))
        fp.close()
        #Check if its already there
        if not os.path.isfile(att_path) :
            print("indside file")
            # finally write the stuff
            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()