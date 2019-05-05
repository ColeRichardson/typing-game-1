import tkinter as tk
import time

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
		self.Entry1 = tk.Entry(self.root, bg='yellow', width=100, bd=3, font=20, validate='key', validatecommand=(test, '%i'))

		Label1.pack()
		Label2.pack()
		self.Entry1.pack()



	def checkEntry(self, index):
		print(index)
		print(self.Entry1.get())
		if index == 0:
			self.start_timer()
		return True

	def get_wpm(self, time):
		time_min = time/60
		wpm = time_min/len(self.sentence)

	def start_timer(self):
		start = time.time()
		while self.Entry1.get() != self.sentence:
			pass
		end = time.time()
		time1 = start - end
		print(time1)

	


