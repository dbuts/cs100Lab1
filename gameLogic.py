# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:25:15 2017

Holds the various functions for processsing the game

@author: David Butler
"""
class gameBoard:
	turnCount = 0;
	board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
	def __init__(self):
		self.board = board

	def updateBoard(self, character, x, y):
		self.board[x][y] = character
		if(checkWin(self, character, x, y) == 1):
			print character + "'s won!"

		elif(checkWin(self, character, x, y) == -1):
			print "Cat's Scratch!"

	def checkWin(self, charater, x, y):
		if(checkRow(self, character, x) or checkColumn(self, character, y) or checkDiagonal(self, character, x, y)):
			return 1
		elif(turnCount == 9):
			return -1
		else:
			return 0

	def checkRow(self, character, x):
		rtn = True
		for i in range(0, 3):
			if(self.board[x][i] != character):
				rtn = False
		return rtn

	def checkColumn(self, character, y):
		rtn = True
		for i in range(0, 3):
			if(self.board[i][y] != character):
				rtn = False
		return rtn

	def checkDiagonal(self, character):
		if(self.board[1][1] != character):
			return False
		rtn1 = True
		rtn2 = True
		y1 = 0
		y2 = 3
		for x in range(0,3):
			if(self.board[x][y1] != character):
				rtn1 = False
			if(self.board[x][y2] != character):
				rtn2 = False
		if(rtn1 or rtn2):
			return True
		else:
			return False