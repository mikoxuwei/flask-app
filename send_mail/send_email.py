import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
from email.mime.application import MIMEApplication

html = """
<h1> Hello </h1>
<div> 這是 html 的內容</div>
<div style="color: red;"> 這是紅色的字</div>
<img src="https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg" alt="貓咪圖片" style="width: 300px; height: 200px;">
<a href="https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg">點擊這裡查看圖片</a>
<div>這是直接放圖片img src="https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg" alt="貓咪圖片" style="width: 300px; height: 200px;"</div>
"""

msg = MIMEMultipart()
msg.attach(MIMEText(html, "html", "utf-8"))  # 設定編碼為 utf-8
with open("send_mail/cat.jpg", "rb") as file:
    img = file.read()
attach_file = MIMEApplication(img, name = "cat.jpg")  # 設定附件名稱
msg.attach(attach_file)

msg["From"] = "s2525123a@gmail.com"
msg["To"] = "m11382027@gm2.nutn.edu.tw"
msg["Subject"] = "附件是一張貓的圖片"

# Gmail SMTP 設定
smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()  # 啟動 SMTP 服務
smtp.starttls()  # 啟用 TLS
smtp.login("s2525123a@gmail.com", "vvgy txxr bqcc nyox")  # 登入 Gmail
status = smtp.sendmail(msg["From"], msg["To"], msg.as_string())  # 發送郵件
print("郵件發送狀態:", status)  # 印出發送狀態
smtp.quit()  # 關閉 SMTP 連線