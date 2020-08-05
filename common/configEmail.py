# -*-coding:utf-8 -*-

import os
import smtplib
from email.header import Header
from config import readConfig, getpathInfo
from common.Log import logger
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')  # 从配置文件中读取，邮件主题
app = str(read_conf.get_email('app'))  # 从配置文件中读取，邮件类型
addressee = read_conf.get_email('addressee')  # 从配置文件中读取，邮件收件人
cc = read_conf.get_email('cc')  # 从配置文件中读取，邮件发件人
# mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')  # 获取测试报告路径
logger = logger


class Send_Email():

    def new_file(self, test_dir):
        # 列举test_dir目录下的所有文件，结果以列表形式返回。
        lists = os.listdir(test_dir)
        # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
        # 最后对lists元素，按文件修改时间大小从小到大排序。
        lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
        # 获取最新文件的绝对路径
        file_path = os.path.join(test_dir, lists[-1])
        return file_path

    # 定义：发送邮件，发送最新测试报告html
    def send_email(self, newfile):
        # 打开文件
        f = open(newfile, 'rb')
        # 读取文件内容
        mail_body = f.read()
        # 关闭文件
        f.close()

        # 发送邮箱服务器
        smtpserver = 'smtp.163.com'
        # 发送邮箱用户名/密码
        user = '14787184016@163.com'
        password = 'AZAVKTBBMYDGOCGI'
        # 发送邮箱
        sender = cc  # '14787184016@163.com'  # 发件人邮箱(最好写全, 不然会失败)
        # 单个收件人接收邮件，直接是receiver='XXX@163.com'
        # receiver = addressee  # ['xuechao@stary.ltd']
        # 多人接收邮件
        receiver = ['xuechao@stary.ltd','14787184016@163.com','yuyuanhui@stary.ltd','wanglu2@stary.ltd']
        # 发送邮件主题
        subject = 'Dreame_APP_接口自动化测试报告'
        msg = MIMEMultipart('mixed')
        msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(msg_html1)
        msg_html = MIMEText(mail_body, 'html', 'utf-8')
        msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        msg.attach(msg_html)

        # 要加上msg['From']这句话，否则会报554的错误。
        # 要在163设置授权码（即客户端的密码），否则会报535
        msg['From'] = "{}".format(sender)
        #    msg['To'] = 'XXX@doov.com.cn'
        # 多个收件人
        msg['To'] = ",".join(receiver)
        msg['Subject'] = Header(subject, 'utf-8')
        try:
            # 连接发送邮件
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver, 25)
            smtp.login(user, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
            # logger.info('Email has been send successfully , OK !!!!')
            print("Email has been send successfully , OK !!!!")
        except smtplib.SMTPException as e:
            print(e)


if __name__ == "__main__":
    print('===== Test Api Over,Sending Email  ======')
    # 指定测试报告的路径
    test_dir = "D:\\PycharmProjects\\DX_interfaceTest\\result"
    # 2.取最新测试报告
    new_report = Send_Email().new_file(test_dir)
    # 3.发送邮件，发送最新测试报告html
    Send_Email().send_email(new_report)
    print('===== Test Api  Over, Sending Email Success  ======')
