import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自django练手项目的测试邮件',
        '欢迎访问django项目，我们在测试邮件发送！',
        'xxxx@163.com',
        ['xxxxx@qq.com'],
    )