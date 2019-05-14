import os
import random
import tkinter as tk
from tkinter import filedialog
import time
from typing import List

class GUI:

	def __init__(self):
		self.wpm = 0
		self.wpmList = []
		self.avgWpm = 0
		self.start = 0.0
		self.end = 0.0
		self.numOfSentances = 0
		self.currentLine = 0
		self.check = True		# Singleton for timer
		self.sentenceList = []
		self.sentenceCheck = None
		self.root = tk.Tk()

		self.sentence = tk.StringVar()
		self.wpmVar = tk.StringVar()
		self.avgwpmVar = tk.StringVar()
		self.wpmVar.set('Finish the sentence to correctly to get your wpm')
		self.avgwpmVar.set('Average WPM for your session')

		self.setUpStage()

	def setUpStage(self):
		"""
		Sets up the GUI elements on the page
		"""
		self.root.title("Typing Game")
		self.root.geometry("1500x1000")
		label1 = tk.Label(self.root, text='Type this sentence', background='orange', padx=10, pady=10, font=12)
		currentSentance = tk.Label(self.root, textvariable=self.sentence, background='green', font=25, padx=20, pady=20, height=3, wraplength=700)
		self.wpmLabel = tk.Label(self.root, textvariable=self.wpmVar, background='red', font=15, padx=20, pady=20)
		checkWord = self.root.register(self.isValidSentance)
		self.inputTextBox = tk.Entry(self.root, bg='yellow', width=100, bd=3, font=20, validate='key', validatecommand=(checkWord, '%i', '%P'))
		importFile = tk.Button(self.root, text='Import txt file', command=self.promptImport)
		wordsPerMinute = tk.Label(self.root, textvariable=self.avgwpmVar, padx=10, pady=10, font=12)
		resetButton = tk.Button(self.root, text='Reset', command=self.resetOrder)
		randomButton = tk.Button(self.root, text='Random Sentance', command=self.resetRandom)


		# Packing widgets
		label1.pack()
		currentSentance.pack()
		self.inputTextBox.pack()
		self.wpmLabel.pack()
		importFile.pack()
		wordsPerMinute.pack()
		resetButton.pack()
		randomButton.pack()

	def isValidSentance(self, index, text):
		"""
		checks the contents of the entry widget to see when the user starts typing
		and when their sentence matches the required sentence.
		:param index:
		:param text:
		:return:
		"""
		print(text)
		print(self.sentenceCheck)
		if self.check:
			self.check = False 
			self.start = time.time()
		if text == self.sentenceCheck:
			self.end = time.time()
			self.getWpm()
		return True

	def getWpm(self):
		"""
		gets the time it took the user to type and uses that to
		get the users words per minute (wpm)
		:return:
		"""
		time_fact = 60/(self.end - self.start)
		self.wpm = time_fact * self.getNumWords()
		self.wpmVar.set('Your wpm is: ' + str(int(self.wpm)))

	def getNumWords(self):
		"""
		gets the number of words in the sentence the user was asked to type
		:return:
		"""
		numWords = 1
		for space in self.sentenceCheck:
			if space == ' ':
				numWords += 1
		return numWords	

	def readFile(self):
		fileName = open(self.root.fileName, 'r')
		self.numOfSentances = 0
		for line in fileName:
			self.sentenceList.append(line.rstrip())
			self.numOfSentances += 1
		fileName.close()

	def promptImport(self):
		self.root.fileName = filedialog.askopenfilename(initialdir=os.getcwd() ,title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
		self.sentenceList = []
		self.readFile()
		self.randomSentance()

	def nextSentance(self):
		self.currentLine += 1
		if self.currentLine > self.numOfSentances - 1:
			self.currentLine = 0
		print("On line: " + str(self.currentLine))
		self.sentence.set(self.sentenceList[self.currentLine])
		self.sentenceCheck = self.sentenceList[self.currentLine]

	def randomSentance(self):	
		oldLine = self.currentLine
		while (oldLine == self.currentLine):
			self.currentLine = random.randint(0, self.numOfSentances - 1)
		print("Old: " + str(oldLine) + " current: " + str(self.currentLine))
		self.sentence.set(self.sentenceList[self.currentLine])
		self.sentenceCheck = self.sentenceList[self.currentLine]
	
	def resetRandom(self):
		self.reset()
		self.randomSentance()

	def resetOrder(self):
		self.reset()
		self.nextSentance()

	def reset(self):
		if self.sentenceList != []:
			if self.wpm != 0:
				self.wpmList.append(self.wpm)
			self.wpm = 0
			self.start = 0.0
			self.end = 0.0
			if self.check == False:
				self.check = True

			self.inputTextBox.delete(0, 'end')
			self.setWpmAvg()	
		

	def setWpmAvg(self):
		x = 0
		for wpm in self.wpmList:
			x += wpm
		if self.avgWpm == 0:
			self.avgWpm = x
		else:
			self.avgWpm = int( x / len(self.wpmList))
		self.avgwpmVar.set("Your average wpm is: " + str(self.avgWpm))
