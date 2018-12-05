#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import tkinter as tk

'''松耦合'''


# 购买弹窗
class MyDialogBuy(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('进货')

        # 弹窗界面
        self.setup_UI()

    def setup_UI(self):
        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='品名', width=8).pack(side=tk.LEFT)
        self.name = tk.StringVar()
        tk.Entry(row1, textvariable=self.name, width=20).pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(fill="x")
        tk.Label(row2, text='单价', width=8).pack(side=tk.LEFT)
        self.price = tk.IntVar()
        tk.Entry(row2, textvariable=self.price, width=20).pack(side=tk.LEFT)

        # 第三行
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Label(row3, text='数量', width=8).pack(side=tk.LEFT)
        self.amount = tk.IntVar()
        tk.Entry(row3, textvariable=self.amount, width=20).pack(side=tk.LEFT)

        # 第四行
        row4 = tk.Frame(self)
        row4.pack(fill="x")
        tk.Button(row4, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row4, text="确定", command=self.ok).pack(side=tk.RIGHT)

    def ok(self):
            self.buyinfo = [self.name.get(), self.price.get(), self.amount.get()]  # 设置数据
            self.destroy()  # 销毁窗口

    def cancel(self):
            self.buyinfo = None  # 空！
            self.destroy()


# 售出弹窗
class MyDialogSell(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('进货')

        # 弹窗界面
        self.setup_UI()

    def setup_UI(self):
        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='品名', width=8).pack(side=tk.LEFT)
        self.name = tk.StringVar()
        tk.Entry(row1, textvariable=self.name, width=20).pack(side=tk.LEFT)

        # 第二行
        row2 = tk.Frame(self)
        row2.pack(fill="x")
        tk.Label(row2, text='单价', width=8).pack(side=tk.LEFT)
        self.price = tk.IntVar()
        tk.Entry(row2, textvariable=self.price, width=20).pack(side=tk.LEFT)

        # 第三行
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Label(row3, text='数量', width=8).pack(side=tk.LEFT)
        self.amount = tk.IntVar()
        tk.Entry(row3, textvariable=self.amount, width=20).pack(side=tk.LEFT)

        # 第四行
        row4 = tk.Frame(self)
        row4.pack(fill="x")
        tk.Button(row4, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row4, text="确定", command=self.ok).pack(side=tk.RIGHT)

    def ok(self):
            self.sellinfo = [self.name.get(), self.price.get(), self.amount.get()]  # 设置数据
            self.destroy()  # 销毁窗口

    def cancel(self):
            self.sellinfo = None  # 空！
            self.destroy()


# 主窗体
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('库存查询')
        self.geometry("280x200")

        # 程序参数/数据
        self.name = '硒鼓'
        self.price = 998
        self.amount = 1
        self.money = self.price * self.amount

        # 程序界面
        self.setupUI()

    def setupUI(self):
        # 第一行
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='商品名称').pack(side=tk.LEFT)
        tk.Label(row1, text='单价').pack(side=tk.LEFT)
        tk.Label(row1, text='数量').pack(side=tk.LEFT)
        tk.Label(row1, text='总价').pack(side=tk.LEFT)

        # 进货/售出/汇总
        tk.Button(row1, text="进货", command=self.buy).pack(side=tk.LEFT)
        tk.Button(row1, text="售出", command=self.sell).pack(side=tk.LEFT)
        tk.Button(row1, text="汇总", command=self.list).pack(side=tk.LEFT)

    def buy(self):
        # 接收弹窗的数据
        res = self.buyinfo()
        if res is None:
            return
        # 更改参数
        self.name, self.price, self.amount = res
        print(res)

    def sell(self):
        # 接收弹窗的数据
        res = self.buyinfo()
        if res is None:
            return
        # 更改参数
        self.name, self.price, self.amount = res
        print(res)

    def list(self):
        row2 = tk.Frame(self)
        row2.pack(fill="x")
        print(self.name)
        tk.Label(row2, text=self.name).pack(side=tk.LEFT)
        tk.Label(row2, text=self.price).pack(side=tk.LEFT)
        tk.Label(row2, text=self.amount).pack(side=tk.LEFT)
        tk.Label(row2, text=self.money).pack(side=tk.LEFT)

    # 购买弹窗
    def buyinfo(self):
        inputdialog = MyDialogBuy()
        self.wait_window(inputdialog)
        return inputdialog.buyinfo

    # 售出弹窗
    def sellinfo(self):
        inputdialog = MyDialogSell()
        self.wait_window(inputdialog)
        return inputdialog.sellinfo


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()