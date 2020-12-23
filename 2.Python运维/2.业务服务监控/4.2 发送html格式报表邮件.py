import smtplib
from email.mime.text import MIMEText
from email.header import Header

HOST = ("smtp.163.com")
SUBJECT = "Test email from Python-notebook"
TO = ["861022418@qq.com", "2859626066@qq.com"]
FROM = "17610291226@163.com"
text = "哈哈哈哈哈"

message = MIMEText(""" #创建一个MIMEText对象，分别指定HTML内容、类型（文本或html）、字符编码
<table width="800" border="0" cellspacing="0" cellpadding="4">
    <tr>
        <td bgcolor="#CECFAD" height="20">*官网数据<a href="monitor.domain.com">更多>></a></td>
    </tr>

    <tr>
        <td bgcolor="#EFEBDE" height="100">
            1）日访问量:<font color=red>152433</font>访问次数:23651  页面浏览量:45123  点击数:54512  数据流量:504Mb<br/>
    
            2）状态码信息<br/>&nbsp;&nbsp;500:105 404:3264 503:214<br/>
    
            3）访客浏览器信息<br/>&nbsp;&nbsp;IE:50% firefox: 10% chrome: 30% other: 10%<br/>
    
            4）页面信息<br/>
                &nbsp;&nbsp;/index.php 42153<br/>
                &nbsp;&nbsp;/view.php 21451<br/>
                &nbsp;&nbsp;/login.php 5112<br/>
        </td>
    </tr>
</table>""", "html", "utf-8")
# message["From"] = Header(FROM, "utf-8") # 会报错554
message["From"] = "bit" + "<" + FROM + ">"
message["To"] = Header(",".join(TO), "utf-8")
message["Subject"] = Header(SUBJECT, "utf-8")

if __name__ == "__main__":
    server = smtplib.SMTP_SSL(HOST, 465)
    server.login(FROM, "****")

    server.sendmail(FROM, TO, message.as_string())
    server.quit()
