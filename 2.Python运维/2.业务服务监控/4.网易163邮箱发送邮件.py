import smtplib
from email.mime.text import MIMEText
from email.header import Header

HOST = ("smtp.163.com")
SUBJECT = "Test email from Python-notebook"
TO = ["861022418@qq.com", "904765116@qq.com"]
FROM = "17610291226@163.com"
text = "哈哈哈哈哈"

message = MIMEText("For Bot: \r\n  Python rules all.", "plain", "utf-8")
# message["From"] = Header(FROM, "utf-8") # 会报错554
message["From"] = "username" + "<" + FROM + ">"
message["To"] = Header(",".join(TO), "utf-8")
message["Subject"] = Header(SUBJECT, "utf-8")

if __name__ == "__main__":
    server = smtplib.SMTP_SSL(HOST, 465)
    server.login(FROM, "LGYUIWHBLRMQCFNN")

    server.sendmail(FROM, TO, message.as_string())
    server.quit()
