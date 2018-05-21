import unittest,os
from HTMLReport import HTMLReport
import time

# test_dir = './'  # 表示脚本当前路径
test_dir =os.path.dirname(os.getcwd())+'/TestCase'  # 表示脚本当前路径
discovery = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # 匹配所有的test开头的.py文件

if __name__ == '__main__':
    # 测试用例执行器
    runner = HTMLReport.TestRunner(report_file_name='',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                   output_path='report',  # 保存文件夹名，默认“report”
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='无测试描述',  # 报告描述，默认“测试描述”
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   thread_start_wait=0,  # 各线程启动延迟，默认 0 s
                                   sequential_execution=False,  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   # 如果用例中存在 tearDownClass ，建议设置为True，
                                   # 否则 tearDownClass 将会在所有用例线程执行完后才会执行。
                                   # lang='en'
                                   lang='cn'  # 支持中文与英文，默认中文
                                   )
    # 执行测试用例套件
    runner.run(discovery)

