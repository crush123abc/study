import threading
import time

"""
多线程运行，threading,可用来爬数据和消费放大量数据
I/O密集型：程序需要频繁进行输入输出操作，爬虫就是典型的I/O密集型程序
安排子线程任务：threading.Thread(target=run)
子线程开始工作：start()
守护进程：setDaemon(True)，默认为False，主线程死亡子线程随着主线程死亡，需要在start()方法前使用
线程阻塞：join(),等待子线程任务结束,需要在start()方法后使用

"""

x = 0


def run(parm):
    time.sleep(1)
    # 以f开头，包含的{}里面可以使用变量，print(f'你好{x}----')
    print('你好----')
    # time.sleep(3)


# 开始时间
start_time = time.time()
threads = []  # 用来存储子线程
# run()
for i in range(100):
    # 子线程列表添加（多线程方法安排子线程任务）
    threads.append(threading.Thread(target=run, args=(i,)))
for i in threads:
    # i.setDaemon(True)
    # 子线程正式运行
    i.start()
# for i in threads:
#     #等待子线程任务结束
#     i.join()
# t1 = threading.Thread(target=run)#安排子线程任务
# t2 = threading.Thread(target=run)
# t3 = threading.Thread(target=run)
# t1.setDaemon(True)#守护进程，主进程死亡则子进程死亡
# t1.start()#子线程开始执行
# t2.start()
# t3.start()
#
# t1.join()#等待子线程任务结束
# t2.join()
# t3.join()

# run()
# run()
print('done')
end_time = time.time()
print(end_time - start_time)

#
# def do_something(n):
#     if n <= 1:
#         return n
#     else:
#         return do_something(n - 1) + do_something(n - 2)
#
# start_time=time.time()
# for i in range(50):
#     numbers = do_something(i + 1)
#     print(numbers)
# end_time = time.time()
# print(end_time-start_time)
