import random
import tkinter as tk
from tkinter import filedialog
import time
from typing import List

class GUI:

	def __init__(self):
		self.wpm = 0
		self.start = 0.0
		self.end = 0.0
		self.time1 = 0.0
		self.check = 0
		self.sentence_list = []
		self.sentence_check = None
		self.root = tk.Tk()
		self.root.title("Typing Game")
		self.root.geometry("1500x1000")
		self.filename = 'test_phrases.txt'
		self.wordsList = []

		self.sentence = tk.StringVar()
		self.wpm_var = tk.StringVar()
		self.wpm_var.set('Finish the sentence to correctly to get your wpm')


		Label1 = tk.Label(self.root, text='Type this sentence', background='orange', padx=10, pady=10, font=12)
		Label2 = tk.Label(self.root, textvariable=self.sentence, background='green', font=25, padx=20, pady=20, height=3, wraplength=700)
		self.wpm_Label = tk.Label(self.root, textvariable=self.wpm_var, background='red', font=15, padx=20, pady=20)
		test = self.root.register(self.checkEntry)
		self.Entry1 = tk.Entry(self.root, bg='yellow', width=100, bd=3, font=20, validate='key', validatecommand=(test, '%i', '%P'))
		Button1 = tk.Button(self.root, text='Import txt file', command=self.prompt_import)

		# Packing widgets
		Label1.pack()
		Label2.pack()
		self.Entry1.pack()
		self.wpm_Label.pack()
		Button1.pack()



	def checkEntry(self, index, text):
		"""
		checks the contents of the entry widget to see when the user starts typing
		and when their sentence matches the required sentence.
		:param index:
		:param text:
		:return:
		"""
		print(text)
		print(self.sentence_check)
		if self.check == 0:
			self.check += 1
			self.start_timer()
		if text == self.sentence_check:
			self.end_timer()
			self.get_wpm()
		return True

	def start_timer(self):
		"""
		starts the timer
		:return:
		"""
		self.start = time.time()


	def end_timer(self):
		"""
		ends the timer
		:return:
		"""
		self.end = time.time()


	def get_wpm(self):
		"""
		gets the time it took the user to type and uses that to
		get the users words per minute (wpm)
		:return:
		"""
		self.time1 = self.end - self.start
		time_fact = 60/self.time1
		self.wpm = time_fact * self.get_num_words()
		self.update_wpm_label()

	def get_num_words(self):
		"""
		gets the number of words in the sentence the user was asked to type
		:return:
		"""
		num_words = 1
		for space in self.sentence_check:
			if space == ' ':
				num_words += 1
		return num_words

	def update_wpm_label(self):
		"""
		update the wpm label to contain the users wpm
		:return:
		"""
		self.wpm_var.set('Your wpm is: ' + str(int(self.wpm)))

	def read_file(self):
		file_name = open(self.root.fileName, 'r')
		for line in file_name:
			self.sentence_list.append(line.rstrip())
		file_name.close()

	def prompt_import(self):
		self.root.fileName = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
		self.read_file()
		self.choose_sentence()

	def choose_sentence(self):
		rand = random.randint(0, len(self.sentence_list)-1)
		self.sentence.set(self.sentence_list[rand])
		self.sentence_check = self.sentence_list[rand]
		self.wordsList = self.sentence_list[rand].split()


