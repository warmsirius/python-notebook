from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

"""
1.通过 MIMEText类来实现HTML格式的邮件
2.当包含图片数据的邮件内容时，需要引用MIMEImage类

注意: 若邮件主体由多个MIME对象组成，则同时需引用MIMEMultipart类来进行组装。0
"""

HOST = ("smtp.163.com")
SUBJECT = "Test email from Python-notebook"
TO = ["17610291226@163.com", "861022418@qq.com", "2859626066@qq.com"]
FROM = "17610291226@163.com"


def addimg(src, imgid):
    """添加图片路径"""
    with open(src, "rb") as fp:
        msgImage = MIMEImage(fp.read())
    msgImage.add_header("Content-ID", imgid)
    return msgImage


msg = MIMEMultipart('related')

msgText = MIMEText("""
<table width="600" border="0" cellspacing="0" cellpadding="4">
    <tr bgcolor="#CECFAD" height="20">
        <td colspan=2 height="20">*卡哇伊喵酱:<a href="#">更多>></a></td>
    </tr>

    <tr bgcolor="#EFEBDE" height="100">
        <td>
            <img height="400" width="400" src="cid:cat1" />
        </td>
        
        <td>
            <img height="400" width="400" src="cid:cat2" />
        </td>
    </tr>
    <tr bgcolor="#EFEBDE" height="100">
        <td>
            <img height="400" width="400" src="cid:cat3"/>
        </td>
        <td>
            <img height="400" width="400" src="cid:cat4">
        </td>
    </tr>
</table>""", "html", "utf-8")

msg.attach(msgText)
msg.attach(addimg("../../assets/cat1.jpeg", "cat1"))
msg.attach(addimg("../../assets/cat2.jpeg", "cat2"))
msg.attach(addimg("../../assets/cat3.jpeg", "cat3"))
msg.attach(addimg("../../assets/cat4.jpeg", "cat4"))

msg["From"] = "bit" + "<" + FROM + ">"
msg["To"] = Header(",".join(TO), "utf-8")
msg["Subject"] = Header(SUBJECT, "utf-8")

if __name__ == "__main__":
    server = smtplib.SMTP_SSL(HOST, 465)
    server.login(FROM, "****")

    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
