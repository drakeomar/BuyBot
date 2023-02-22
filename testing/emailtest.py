import imaplib, email
import html2text

user = 'drake@wirecutcompany.com'
password = 'JanuarySTG@041288'
imap_url = 'imap.gmail.com'

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)

    return msgs


connection = imaplib.IMAP4_SSL(imap_url)
connection.login(user, password)
connection.select('Inbox')

result, data = connection.uid('search', None, '(FROM "BestBuyInfo@emailinfo.bestbuy.com")')
print(data[0].split())
if result == 'OK':
    num = data[0].split()[-1]
    result, data = connection.uid('fetch', num, '(RFC822)')
    if result == 'OK':
        email_message = email.message_from_bytes(data[0][1])
        #print('From:' + email_message['From'])
        #print('To:' + email_message['To'])
        #print('Date:' + email_message['Date'])
        #print('Subject:' + str(email_message['Subject']))
            #print('Content:' + str(email_message.get_payload(decode=True)))
        text = f"{email_message.get_payload(decode=True)}"
        html = text.replace("b'", "")
        h = html2text.html2text(html)


        output = h.replace("\\r\\n","")
        output = output.replace("'", "")
        result = output.find("Verification Code:")


        print(output)
        print(result)
        result = result + 20
        end_result = result + 10
        print(output[result:end_result].strip())
connection.close()
connection.logout()
