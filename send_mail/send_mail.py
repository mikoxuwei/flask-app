# 寄送 Email 的程式
# 準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]='s2525123a@gmail.com'
msg["To"]='m11382027@gm2.nutn.edu.tw'
msg["Subject"]='你好'
# 寄送純文字內容
msg.add_alternative('<h3>測試看看：1234567890</h3>', subtype='html')

# 發送郵件
import smtplib

# Gmail SMTP 設定
smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = "s2525123a@gmail.com"  # 請改成你自己的 Gmail 帳號
app_password = "vvgy txxr bqcc nyox"# 請改成你自己的應用程式密碼

# 發送郵件
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.login(sender_email, app_password)
server.send_message(msg)
server.quit()

