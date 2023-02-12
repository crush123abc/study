import multiprocessing
import time


def run(parm):
    time.sleep(1)
    # time.sleep(1)
    # 以f开头，包含的{}里面可以使用变量
    print('你好----')
    time.sleep(3)


if __name__ == '__main__':

    start_time = time.time()
    threads = []  # 用来存储子线程
    # run()
    # 不能超过电脑本身cpu数量
    for i in range(12):
        # 子线程列表添加（多线程方法安排子线程任务）
        threads.append(multiprocessing.Process(target=run, args=(i,)))
    for i in threads:
        # i.setDaemon(True) #守护进程
        # 子线程正式运行
        i.start()
    for i in threads:
        # 等待子线程任务结束
        i.join()

    print('done')
    end_time = time.time()
    print(end_time - start_time)
