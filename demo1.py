from tkinter import *
class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0

    def __getitem__(self, item):
        self.counter += 1
        return super(CounterList, self).__getitem__(item)

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLable = Label(self, text='Hello,world!')
        self.helloLable.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()





if __name__ == '__main__':
    app = Application()
    app.master.title('hello')
    app.mainloop()

