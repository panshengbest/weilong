from helium import *
import time

def check_in(username, password):
    # 打开网 页
    start_chrome('https://720ccl88.emy163.cn/user/login.php')

    # 等待页面加载
    #wait_until(Text('立即登陆').exists)
    time.sleep(15)

    # 输入用户名和密码
    write(username, into=TextField('\u7528\u6237\u540d'))
    write(password, into=TextField('密码'))

    # 点击登录按钮
    click(Button('立即登陆'))

    # 等待页面加载
    #wait_until(Text('系统管理中心').exists)
    time.sleep(15)

    # 点击签到按钮
    click(Text('每日签到'))
    #wait_until(Text('总奖励').exists)
    time.sleep(15)
    click(S('#qiandao'))

    # 等待签到成功提示出现
    #wait_until(Text('签到成功').exists)
    time.sleep(15)

    # 关闭浏览器标签页
    kill_browser()

# 读取账号密码文件
with open('accounts.txt', 'r') as f:
    accounts = f.readlines()

# 循环调用签到函数
for account in accounts:
    username, password = account.strip().split(',')
    check_in(username, password)
    time.sleep(5) # 每次签到之间暂停5秒
