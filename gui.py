import os
import random
import time
import tkinter as tk
from tkinter import filedialog
from typing import List

class GUI:

	def __init__(self):
		self.wpm = 0
		self.wpmList = []
		self.avgWpm = 0
		self.start = 0.0
		self.end = 0.0
		self.numOfSentences = 0
		self.currentLine = 0
		self.check = True		# Singleton for timer
		self.sentenceList = []
		self.sentenceCheck = None
		self.root = tk.Tk()
		self.sentence = tk.StringVar()
		self.wpmVar = tk.StringVar()
		self.avgwpmVar = tk.StringVar()
		self.wpmVar.set('Type the sentence to get your words per minute (wpm)')
		self.avgwpmVar.set('Average WPM for your session: ')

		self.setUpStage()

	def setUpStage(self):
		"""
		Sets up the GUI elements on the page
		"""
		self.root.title("Typing Game")
		self.root.geometry("1500x1000")

		title = tk.Label(self.root, text='Welcome to Typing Tutor! Import a text file to begin! :D', background='#3c7ee8', font=('Helvetica', 30), padx=10)

		currentSentence = tk.Label(self.root, textvariable=self.sentence, background='green', font=('Helvetica', 20), padx=100, pady=5, height=5, wraplength=700)

		checkWord = self.root.register(self.isValidSentence)

		self.inputTextBox = tk.Entry(self.root, bg='black', width=100, bd=3, font=('Helvetica', 15), foreground='white', validate='key', validatecommand=(checkWord, '%i', '%P'), insertbackground='white')

		# Framing WPM labels
		wpmFrame = tk.Frame(self.root)
		currentWpmLabel = tk.Label(wpmFrame, textvariable=self.wpmVar, background='red', font=15, padx=20, pady=20)
		avgWpmLabel = tk.Label(wpmFrame, textvariable=self.avgwpmVar, padx=10, pady=10, font=12)

		# Packing widgets
		title.pack(fill=tk.X)
		currentSentence.pack(pady=30)
		self.inputTextBox.pack(pady=20)
		currentWpmLabel.pack()
		avgWpmLabel.pack()
		wpmFrame.pack()

		self.makeButtons()

	def makeButtons(self):
		"""
		Initilizes four buttons for gui.
		"""
		buttonFrame = tk.Frame(self.root)

		importFile = tk.Button(buttonFrame, text='Import txt file', command=self.promptImport, highlightbackground='blue',background='#9544E5', foreground='white')

		randomButton = tk.Button(buttonFrame, text='Random Sentence', command=self.resetRandom, highlightbackground='blue', background='#17B0F2', foreground='white')

		nextSentenceButton = tk.Button(buttonFrame, text='Next Sentence', command=self.resetOrder, highlightbackground='blue', background='#17B0F2', foreground='white')

		resetButton = tk.Button(buttonFrame, text='Reset', command=self.hardReset, highlightbackground='blue', background='#980000', foreground='white')

		importFile.pack(side=tk.LEFT, padx=5)
		nextSentenceButton.pack(side=tk.LEFT, padx=5)
		randomButton.pack(side=tk.LEFT, padx=5)
		resetButton.pack(side=tk.LEFT, padx=5)
		buttonFrame.pack()


	def isValidSentence(self, index, text):
		"""
		checks the contents of the entry widget to see when the user starts typing
		and when their sentence matches the required sentence.
		-add find_wrong_word to check each time a character is typed.
		:param index:
		:param text:
		:return:
		"""
		print(text)
		print(self.sentenceCheck)
		if self.check:
			self.start = time.time()
			self.check = False

		if text == self.sentenceCheck:
			self.end = time.time()
			self.getWpm()

		return True

	def find_wrong_word(self):
		""" creates a list by splitting the current contents of the list,
		then does the below for loop to return the missing words from the self.sentence check,
		effectively shows the user what word they typed wrong.

		Example:
		x = ['word', 'cat', 'dog,']
		y = ['word', 'dog,']
		i = 0
		for item in x:
			x.remove(y[i])
     		i += 1
		"""

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
		self.numOfSentences = 0
		for line in fileName:
			self.sentenceList.append(line.rstrip())
			self.numOfSentences += 1
		fileName.close()

	def promptImport(self):
		self.root.fileName = filedialog.askopenfilename(initialdir=os.getcwd() + '/textFiles',title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
		self.sentenceList = []
		self.readFile()
		self.randomSentence()
		self.inputTextBox.delete(0, 'end')

	def nextSentence(self):
		self.currentLine += 1
		if self.currentLine > self.numOfSentences - 1:
			self.currentLine = 0
		print("On line: " + str(self.currentLine))
		self.sentence.set(self.sentenceList[self.currentLine])
		self.sentenceCheck = self.sentenceList[self.currentLine]
		self.inputTextBox.delete(0, 'end')

	def randomSentence(self):
		oldLine = self.currentLine
		while (oldLine == self.currentLine):
			self.currentLine = random.randint(0, self.numOfSentences - 1)
		print("Old: " + str(oldLine) + " current: " + str(self.currentLine))
		self.sentence.set(self.sentenceList[self.currentLine])
		self.sentenceCheck = self.sentenceList[self.currentLine]

	def resetRandom(self):
		self.reset()
		self.randomSentence()

	def resetOrder(self):
		self.reset()
		self.nextSentence()

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

	def hardReset(self):
		"""
		resets all values to the original values in the init,
		clears everything, resets everything to original state
		similar to reopening the program
		:return:
		"""
		self.wpm = 0
		self.wpmList = []
		self.avgWpm = 0
		self.start = 0.0
		self.end = 0.0
		self.numOfSentences = 0
		self.currentLine = 0
		self.check = True  # Singleton for timer
		self.sentenceList = []
		self.sentenceCheck = None
		self.sentence.set('')
		self.wpmVar.set('Finish the sentence correctly to get your wpm')
		self.avgwpmVar.set('Average WPM for your session')
		self.inputTextBox.delete(0, 'end')

	def setWpmAvg(self):
		x = 0
		for wpm in self.wpmList:
			x += wpm
		if self.avgWpm == 0:
			self.avgWpm = x
		else:
			self.avgWpm = int( x / len(self.wpmList))
		self.avgwpmVar.set("Your average wpm is: " + str(self.avgWpm))
