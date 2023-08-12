#Made by Yogesh
from tkinter import *
import tkinter.font as tkFont
import webbrowser
from PIL import Image, ImageTk

expression = ""

def opengit():
	webbrowser.open('https://github.com/CaptainYogs')

def openins():
	#webbrowser.open('https://youtu.be/dQw4w9WgXcQ')
	webbrowser.open('https://instagram.com/captainyogs?utm_source=qr&igshid=MzNlNGNkZWQ4Mg%3D%3D')

def openlink():
	webbrowser.open('https://www.linkedin.com/in/yogesh120/')

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="light gray")
	gui.title("Simple Calculator by Yogesh")
	gui.geometry("375x600")
	gui.iconbitmap("Images/CalculatorIco.ico")
	photogit = Image.open("Images/github.png")
	photoimagegit = photogit.resize((80, 80))
	my_imggit=ImageTk.PhotoImage(photoimagegit)
	photolink = Image.open("Images/Link.png")
	photoimagelink = photolink.resize((80, 80))
	my_imglink=ImageTk.PhotoImage(photoimagelink)
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation, font=('Arial 25'))
	expression_field.grid(columnspan=10, rowspan=2, sticky="NSEW")
	Grid.rowconfigure(gui,1,weight=1) 
	Grid.rowconfigure(gui,2,weight=1) 
	Grid.rowconfigure(gui,3,weight=1) 
	Grid.rowconfigure(gui,4,weight=1) 
	Grid.rowconfigure(gui,5,weight=1) 
	Grid.columnconfigure(gui,0,weight=1)
	Grid.columnconfigure(gui,1,weight=1)
	Grid.columnconfigure(gui,2,weight=1)
	Grid.columnconfigure(gui,3,weight=1)
	Ari = tkFont.Font(family='Arial', size=25)
	AriM = tkFont.Font(family='Arial', size=15)
	button1 = Button(gui, text=' 1 ', font=Ari, fg='black', bg='light blue', command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0, sticky="NSEW")
	button2 = Button(gui, text=' 2 ', font=Ari, fg='black', bg='light blue', command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1, sticky="NSEW")
	button3 = Button(gui, text=' 3 ', font=Ari, fg='black', bg='light blue', command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2, sticky="NSEW")
	button4 = Button(gui, text=' 4 ', font=Ari, fg='black', bg='light blue', command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0, sticky="NSEW")
	button5 = Button(gui, text=' 5 ', font=Ari, fg='black', bg='light blue', command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1, sticky="NSEW")
	button6 = Button(gui, text=' 6 ', font=Ari, fg='black', bg='light blue', command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2, sticky="NSEW")
	button7 = Button(gui, text=' 7 ', font=Ari, fg='black', bg='light blue', command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0, sticky="NSEW")
	button8 = Button(gui, text=' 8 ', font=Ari, fg='black', bg='light blue', command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1, sticky="NSEW")
	button9 = Button(gui, text=' 9 ', font=Ari, fg='black', bg='light blue', command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2, sticky="NSEW")
	button0 = Button(gui, text=' 0 ', font=Ari, fg='black', bg='light blue', command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=1, sticky="NSEW")
	plus = Button(gui, text=' + ', font=Ari, fg='black', bg='light blue', command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3, sticky="NSEW")
	minus = Button(gui, text=' - ', font=Ari, fg='black', bg='light blue', command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3, sticky="NSEW")
	multiply = Button(gui, text=' * ', font=Ari, fg='black', bg='light blue', command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3, sticky="NSEW")
	divide = Button(gui, text=' / ', font=Ari, fg='black', bg='light blue', command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3, sticky="NSEW")
	equal = Button(gui, text=' = ', font=Ari, fg='black', bg='light blue', command=equalpress, height=1, width=7)
	equal.grid(row=6, column=0, sticky="NSEW")
	clear = Button(gui, text='Clear', font=Ari, fg='black', bg='light blue', command=clear, height=1, width=7)
	clear.grid(row=5, column='2', sticky="NSEW")
	Decimal= Button(gui, text='.', font=Ari, fg='black', bg='light blue', command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=5, column=0, sticky="NSEW")
	gitl = Button(gui, text = 'Click Me !', image = my_imggit, borderwidth = 0, command=opengit)
	gitl.grid(row=7, column=0)
	maby = Button(gui, text= 'Made By Yogesh!', font=AriM, fg='green', command=openins)
	maby.grid(row=7, column=1, columnspan=2)
	linkl = Button(gui, text = 'Click Me !', image = my_imglink, borderwidth = 0, command=openlink)
	linkl.grid(row=7, column=3)
	gui.mainloop()
