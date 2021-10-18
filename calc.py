from tkinter import *
from PIL import ImageTk, Image
from math import sin, cos, tan, log , sqrt

root = Tk()
root.title('Custom Calculator')
root.iconbitmap('favicon.ico')
root.resizable(width=False, height=False)



frame = LabelFrame(root)
e = Entry(frame, width=49, borderwidth=5)

def button_click(number):
	num = e.get()
	e.delete(0, END)
	current = str(num)+str(number)
	e.insert(0, current)
	

def clear():
	e.delete(0, END)

def button_cos(number):
	return
	

def button_sin():
	return
	

def button_tan():
	return

def button_log():
	return

def square():
	return




button_0 = Button(frame, text='0', pady=8, padx=67, command=lambda:button_click('0'))
button_1 = Button(frame, text='1', pady=8, padx=30, command=lambda:button_click('1'))
button_2 = Button(frame, text='2', pady=8, padx=30, command=lambda:button_click('2'))
button_3 = Button(frame, text='3', pady=8, padx=30, command=lambda:button_click('3'))
button_4 = Button(frame, text='4', pady=8, padx=30, command=lambda:button_click('4'))
button_5 = Button(frame, text='5', pady=8, padx=30, command=lambda:button_click('5'))
button_6 = Button(frame, text='6', pady=8, padx=30, command=lambda:button_click('6'))
button_7 = Button(frame, text='7', pady=8, padx=30, command=lambda:button_click('7'))
button_8 = Button(frame, text='8', pady=8, padx=30, command=lambda:button_click('8'))
button_9 = Button(frame, text='9', pady=8, padx=30, command=lambda:button_click('9'))

button_dot = Button(frame, text=' .', pady=8, padx=30, command=lambda:button_click('.'))
button_clear = Button(frame, text='C', pady=8, padx=66, command=clear)

button_cos = Button(frame, text='cos', pady=8, padx=24, command=button_cos)
button_sin = Button(frame, text='sin', pady=8, padx=26, command=button_sin)
button_tan = Button(frame, text='tan', pady=8, padx=25, command=button_tan)
button_log = Button(frame, text='log ', pady=8, padx=27, command=button_log)


button_plus = Button(frame, text='+  ', pady=8, padx=30)
button_subtract = Button(frame, text='- ', pady=8, padx=30)
button_multiply = Button(frame, text='X ', pady=8, padx=32)
button_equals = Button(frame, text='=  ', pady=8, padx=68)
button_divide = Button(frame, text='/ ', pady=8, padx=33)
button_square = Button(frame, text=' x² ', pady=8, padx=30)

frame.pack()
e.grid(row='0', column='0', columnspan=4)
button_0.grid(row='5', column='0', columnspan=2)

button_1.grid(row='4', column='0')
button_2.grid(row='4', column='1')
button_3.grid(row='4', column='2')

button_4.grid(row='3', column='0')
button_5.grid(row='3', column='1')
button_6.grid(row='3', column='2')

button_7.grid(row='2', column='0')
button_8.grid(row='2', column='1')
button_9.grid(row='2', column='2')

button_plus.grid(row='4', column='3')
button_subtract.grid(row='5', column='3')
button_multiply.grid(row='3', column='3')
button_equals.grid(row='6', column='2', columnspan=2)
button_divide.grid(row='5', column='3')
button_dot.grid(row='5', column='2')
button_square.grid(row='2', column='3')

button_clear.grid(row='6', column='0', columnspan=2)

button_cos.grid(row='1', column='0')
button_sin.grid(row='1', column='1')
button_tan.grid(row='1', column='2')
button_log.grid(row='1', column='3')



root.mainloop()