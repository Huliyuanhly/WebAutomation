import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
print(base_dir)
testdatas_dir = os.path.join(base_dir, 'TestDatas')
testcases_dir = os.path.join(base_dir, 'testCases')
htmlreport_dir = os.path.join(base_dir, 'OutPuts/Reports')
logs_dir = os.path.join(base_dir, 'OutPuts/Logs')
pageshots_dir = os.path.join(base_dir, 'OutPuts/PageShots')
