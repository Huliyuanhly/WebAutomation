from ActualExecise2.TestDatas.Common_datas import home_url

# 正常场景 - 测试数据
success_data = {"username": "18684720553", "passwd": "python", "check_url": home_url}
# 异常场景 - 测试数据 手机号为空/密码为空/手机号格式不正确
wrong_data = [
    {"username": "", "passwd": "python", "check": "请输入手机号"},  # 用户名为空
    {"username": "18684720553", "passwd": "", "check": "请输入密码"},  # 密码为空
    {"username": "186847205", "passwd": "python", "check": "请输入正确的手机号"}  # 用户名格式不正确
]
# 异常场景 - 测试数据 密码不正确
wrong_passwd = {"username": "18684720553", "passwd": "11111111", "check": "帐号或密码错误!"}
