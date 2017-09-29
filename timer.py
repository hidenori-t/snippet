# coding: utf-8
# 参考 http://meganezumi.seesaa.net / article / 391262919.html

import tkinter as Tk
import time
import datetime

my_time = (datetime.datetime(2069, 1, 28) -
           datetime.datetime.now()).total_seconds()

WIDTH = 10


class Timer(Tk.Frame):

    def __init__(self, master=None):  # 各ボタンの配置
        Tk.Frame.__init__(self, master)

        self.master.title('I have only 1600000000 seconds till my death')

        b1 = Tk.Button(self, text=u'start', command=self.start,
                       font='Helvetica, 12')
        b2 = Tk.Button(self, text=u'reset', command=self.stop,
                       font='Helvetica, 12')
        self.tokei = Tk.Label(self, text=my_time, font='Helvetica, 25')

        self.s1 = Tk.Spinbox(self, from_=0, to=99, increment=1, width=WIDTH)
        self.s2 = Tk.Spinbox(self, from_=0, to=59, increment=1, width=WIDTH)

        b1.grid(row=1, column=0, columnspan=2,
                padx=5, pady=2, sticky=Tk.W + Tk.E)
        b2.grid(row=1, column=2, columnspan=2,
                padx=5, pady=2, sticky=Tk.W + Tk.E)
        self.tokei.grid(row=2, column=0, columnspan=4,
                        padx=5, pady=2, sticky=Tk.W + Tk.E)

    def start(self):  # Startを押したときの動作
        self.started = True
        self.finish = time.time() + int(my_time)
        self.count()

    def count(self):
        if self.started:
            t = self.finish - time.time()
            self.tokei.config(text="%02d" % t)  # 表示時間を1秒毎に書き換え
            self.after(100, self.count)

    def stop(self):  # 停止処理
        self.started = False
        self.tokei.config(text=my_time)

if __name__ == '__main__':  # スクリプトファイルとして実行されたとき用
    f = Timer()
    f.pack()
    f.mainloop()
