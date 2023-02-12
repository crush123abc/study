import threading
import time


class MyThead(threading.Thread):
    def run3333(self) -> None:
        time.sleep(1)
        print('wowowowowo')
        time.sleep(3)

    def run(self) -> None:
        self.run3333()

# threading.Thread(aaa)

x=MyThead()
# x=MyThead()
# x=MyThead()
# x=MyThead()
# x=MyThead()
x.start()
print("done")

# class MyTherd:
#     def aa(self, mmm):
#         print(mmm)
#
#
# class My(MyTherd):
#     def abc(self):
#         print("调用了")
#
#     # def aa(self, aaa):
#     #     print("儿子调用了", aaa)
#
#
# m = My()
# m.aa("9999")
