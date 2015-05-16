#! /usr/bin/env python

from Tkinter import *
import tkMessageBox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.hintLabel = Label(self, text='Please input your name')
		self.hintLabel.pack()
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.helloBtn = Button(self, text='Hello', command=self.hello)
		self.helloBtn.pack()
		self.alertBtn = Button(self, text='Quit', command=self.quit)
		self.alertBtn.pack()

	def hello(self):
		name = self.nameInput.get() or 'World'
		tkMessageBox.showinfo('Message', 'Hello %s !!!' % name)

app = Application()
app.master.title('Hello Test')
app.mainloop()