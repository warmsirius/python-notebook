import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

"""
本示例通过 MIMEText 与 MIMEImage 类的组合,实现图文邮件格式。

另通过 MIMEText 类再定义 Content-Disposition 属性来实现带附件的邮件。

我们可以利用这些丰富的特性来定制周报邮件,如业务服务质量周报。
"""

HOST = ("smtp.163.com")
SUBJECT = "Test attachment email from Python-notebook"
TO = ["17610291226@163.com", "861022418@qq.com", "2859626066@qq.com"]
FROM = "17610291226@163.com"


def addimg(src, imgid):
    """添加图片路径"""
    with open(src, "rb") as fp:
        msgImage = MIMEImage(fp.read())
    msgImage.add_header("Content-ID", imgid)
    return msgImage


msg = MIMEMultipart('related')

msgtext = MIMEText(
    """<font color=red>
        官网业务周平均延时图表:<br/>
        <img src="cid:cat1" border="1"><br/>
        详细内容见附件。
    </font>""", "html", "utf-8")

msg.attach(msgtext)  # MIMEMultipart对象附加MIMEText的内容
msg.attach(addimg("../../assets/cat3.jpeg", "cat1"))

# 创建一个MIMEText对象,附加week_report.xlsx文档
attach = MIMEText(open("./dir1/a.txt", "rb").read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream"
new_file_name = '=?utf-8?b?' + base64.b64encode("业务服务质量周报".encode()).decode() + '?='
attach["Content-Disposition"] = "attachment; filename={}".format(new_file_name)

msg.attach(attach)  # MIMEMultipart对象附加MIMEText附件内容

msg["From"] = "bit" + "<" + FROM + ">"
msg["To"] = Header(",".join(TO), "utf-8")
msg["Subject"] = Header(SUBJECT, "utf-8")

if __name__ == "__main__":
    server = smtplib.SMTP_SSL(HOST, 465)
    server.login(FROM, "****")

    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
