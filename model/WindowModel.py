from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import utils.SearchHelper as SH


class SearchingWindowModel():
    def __init__(self):
        self.window = Tk()
        self.window.title = "图像检索"
        self.window.geometry('400x200')

        self.canvas = Canvas(self.window)
        Label(self.window, text='输入图片路径:').pack()
        self.filename = StringVar()
        Entry(self.window, textvariable=self.filename).pack()
        Button(self.window, text='选择图片', command=self.getfilename).pack()

        Label(self.window, text='输入数据集路径').pack()
        self.databasepath = StringVar()
        Entry(self.window, textvariable=self.databasepath).pack()
        Button(self.window,text='选择数据集',command=self.getdatabase).pack()

        Button(self.window, text='搜索', command=self.Search).pack()
        self.window.mainloop()


    def getfilename(self):
        self.filename.set(askopenfilename())

    def getdatabase(self):
        self.databasepath.set(askopenfilename())

    def Search(self):
        getfilename = self.filename.get()
        im = mpimg.imread(getfilename)
        plt.title("query")
        plt.imshow(im)
        plt.show()
        database = self.databasepath.get()
        print(getfilename)
        print(database)
        SH.search(getfilename,database)
