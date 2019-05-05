import tkinter as tk

class GUI:
	def __init__(self):
		self.wpm = 0
		self.sentence = 'this is a TEst!'
		self.root = tk.Tk()
		self.root.title("Typing Game")
		self.root.geometry("1500x1000")

		Label1 = tk.Label(self.root, text='Type this sentence', background='orange', padx=10, pady=10, font=12)
		Label2 = tk.Label(self.root, text=self.sentence, background='green', font=15, padx=20, pady=20)

		test = self.root.register(self.checkEntry)
		self.Entry1 = tk.Entry(self.root, bg='yellow', width=100, bd=3, font=20, validate='key', validatecommand=(test, '%V'))

		Label1.pack()
		Label2.pack()
		self.Entry1.pack()


	def checkEntry(self, char):	
		return True
