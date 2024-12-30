from tkinter import *

def shop():
	window = Tk()
	
	window.title("Магазин") #даём ему имя
	window.geometry("300x250") #задём масштаб
	
	bt1 = Button(window, width=10, command=get_bal).pack(anchor=CENTER,expand=True)
	bt2 = Button(window, width=10, command=open_shop).pack(anchor=CENTER,expand=True)

	mainloop()