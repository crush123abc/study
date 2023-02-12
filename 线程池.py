import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

"""
ThreadPoolExecutor:线程池
as_completed：多个子线程任务同时执行时，使用as_completed可以那个子线程先完成先返回
"""


def run():
    time.sleep(1)
    print('你好')
    time.sleep(3)


start_time = time.time()
# 用一个池子接收，设置一个包含N个线程的线程池
pool = ThreadPoolExecutor(max_workers=3)
# 往池子里面丢任务，自动排队执行子线程，并自动返回一个凭证t1
t1 = pool.submit(run)
# 使用t1凭证去找池子要结果，结果未出来自动阻塞，相当于join（）方法
t1.result()
# 多个子线程任务同时执行时，使用as_completed可以那个子线程先完成先返回，使用这个方法必须传入一个可迭代对象（列表）
# as_completed([t1])
print('done')
end_time = time.time()
print(end_time - start_time)
# 线程池给出的结果进行判断方法（），线程池回调
# t1.add_done_callback(线程池给出的结果进行判断)
