import imaplib
import email
from email.header import decode_header
import requests
import os
def plus_plus(title,msg):
    # TODO
    token=""
    response = requests.get(url=f"http://www.pushplus.plus/send?token={token}&title={title}&content={msg}&template=html")
    if response.status_code == 200:
        print("成功发送(或许)")
        print("消息流水号:",response.json()["data"])
# 邮箱配置
# TODO
# 域名 一般是 mail.xxxx
IMAP_SERVER = ''
IMAP_PORT = 993
# 邮箱名
EMAIL_ACCOUNT = ''
# IMAP授权码 并非登陆密码
PASSWORD = ''

# 连接到IMAP服务器
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(EMAIL_ACCOUNT, PASSWORD)

# 选择收件箱
mail.select('inbox')

# 搜索邮件
status, messages = mail.search(None, 'ALL')
print(f'当前邮件数量:{len(messages[0].split())}')
if os.path.exists('mail.txt'):
    with open('mail.txt', 'r') as f:
        content = int(f.read())
        print(f'上一次邮件数量:{content}')
    if content != len(messages[0].split()):
        new_mails_num = len(messages[0].split()) - content
        if status == 'OK':
            new_mails = ""
            i = 1
            for num in [str(a+content+1).encode('utf-8') for a in range(new_mails_num)]:
                status, data = mail.fetch(num, '(RFC822)')
                if status == 'OK':
                    raw_email = data[0][1]
                    email_message = email.message_from_bytes(raw_email)
                    subject, encoding = decode_header(email_message['Subject'])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else 'utf-8')
                    print(subject)
                    new_mails += str(i) + '、' + subject + '\n'
                    i += 1
            print(f"数量：{new_mails_num} \n内容:\n{new_mails}")
            plus_plus(f"有{new_mails_num}封新邮件",new_mails)
    with open('mail.txt', 'w') as f:
        f.write(str(len(messages[0].split())))
else:
    with open('mail.txt', 'w') as f:
        f.write(str(len(messages[0].split())))
mail.close()
mail.logout()
