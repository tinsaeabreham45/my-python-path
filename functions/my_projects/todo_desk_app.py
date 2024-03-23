import imaplib
import email

# IMAP server settings
IMAP_SERVER = 'imap.gmail.com'
USERNAME = 'tinsaeabreham54@gmail.com'
PASSWORD = 'oktdccwjxnmasodk'

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(USERNAME, PASSWORD)

# Select the mailbox (inbox in this case)
mail.select('inbox')

# Search for all emails
result, data = mail.search(None, 'ALL')

if result == 'OK':
    # Iterate through all email ids
    for num in data[0].split():
        # Fetch the email data
        result, data = mail.fetch(num, '(RFC822)')
        if result == 'OK':
            # Parse the email message
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Extract email headers
            print('From:', msg['From'])
            print('To:', msg['To'])
            print('Subject:', msg['Subject'])

            # Extract email body
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == 'text/plain':
                        body = part.get_payload(decode=True).decode('utf-8')
                        print('Body:', body)
            else:
                body = msg.get_payload(decode=True).decode('utf-8')
                print('Body:', body)

            print('-----------------------------------')

# Logout and close the connection
mail.logout()
