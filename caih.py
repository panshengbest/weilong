from helium import *
import time

def check_in(username, password):
    # ����ҳ
    start_chrome('https://720ccl88.emy163.cn/user/login.php')

    # �ȴ�ҳ�����
    wait_until(Text('������½').exists)

    # �����û���������
    write(username, into=TextField('�û���'))
    write(password, into=TextField('����'))

    # �����¼��ť
    click(Button('������½'))

    # �ȴ�ҳ�����
    wait_until(Text('ϵͳ��������').exists)

    # ���ǩ����ť
    click(Text('ÿ��ǩ��'))
    wait_until(Text('�ܽ���').exists)
    click(S('#qiandao'))

    # �ȴ�ǩ���ɹ���ʾ����
    wait_until(Text('ǩ���ɹ�').exists)

    # �ر��������ǩҳ
    kill_browser()

# ��ȡ�˺������ļ�
with open('accounts.txt', 'r') as f:
    accounts = f.readlines()

# ѭ������ǩ������
for account in accounts:
    username, password = account.strip().split(',')
    check_in(username, password)
    time.sleep(5) # ÿ��ǩ��֮����ͣ5��