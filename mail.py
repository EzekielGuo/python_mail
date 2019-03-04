import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'xxx@xx.com'  # 发件人邮箱账号
my_pass = 'xxx'  # 发件人邮箱密码
my_user = 'xxx@21vianet.com'  # 收件人邮箱账号，我这边发送给自己

def mail(content_info,titles):
    ret = True
    try:
        # msg = MIMEText(content_info, 'plain', 'utf-8')
        msg = MIMEText(content_info, 'html', 'utf-8')
        msg['From'] = formataddr(["tts告警", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["Joe", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = titles  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP()
        server.connect("mail.21nmc.com", 25)
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret

content = "<p>ttsceshi</p>"

mail(content,"tts告警")
