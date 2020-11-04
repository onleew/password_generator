from tkinter import *
from tkinter import messagebox as mb
import random
import time
import sys

def window():
	window = Tk()
	window.geometry("300x170")
	window.resizable(width = False, height = False)
	window.title('Password generate')

	global message
	message = StringVar()

	global bt
	global pt
	global ent
	global lb1
	global ex
	bt = Button(text = 'Сгенерировать', font = ("Ubuntu", 15))
	pt = Label(text = 'Password generate', font = ("Ubuntu", 20))
	ent = Entry(font = ("Ubuntu", 15), textvariable = message, justify = 'center')
	lb1 = Label(text = 'Введите количество символов', font = ("Ubuntu", 14))
	ex = Button(text = 'Выйти', font = ("Ubuntu", 14))

	bt.config(command = function.generate)
	ex.config(command = function.exit)

	function.pack()

	window.mainloop()

class function:
	def generate(self):
		chars1 = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

		try:
			lenght = int(message.get())

			pw = ''
			for i in range(lenght):
				pw += random.choice(chars1)

			file = open('password.txt', 'a')
			file.write('\n' + pw)
			file.close()

			mb.showinfo("Внимание", "Файл сохранён в дериктории")
		except:
			mb.showerror("Error", "Введите число!")

	def exit(self):
		sys.exit()

	def pack(self):
		pt.pack()
		lb1.pack()
		ent.pack()
		bt.pack()
		ex.pack()

if __name__ == '__main__':
	window()
