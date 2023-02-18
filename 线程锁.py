# import threading
# import time
#
# x = 0
# # 创建锁，线程锁
# suo = threading.Lock()
#
#
# def run():
#     global x
#     # 锁定
#     suo.acquire()
#     x += 1
#     time.sleep(1)
#     # 释放锁
#     suo.release()
#     # 以f开头，包含的{}里面可以使用变量
#     print(f'你好{x}----')
#
#
# for i in range(10):
#     t = threading.Thread(target=run)
#     t.start()
