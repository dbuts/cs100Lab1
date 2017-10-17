# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:25:15 2017

Holds the various functions for processsing the game

@author: David Butler
"""
class gameBoard:
	def __init__(self):
		self.board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
		self.turnCount = 0;
		self.player = 'x'

	def updateBoard(self, x, y):
		self.board[x][y] = self.player

	def checkWin(self, x, y):
		self.turnCount+=1
		if(self.checkRow(self.player, x) or self.checkColumn(self.player, y) or self.checkDiagonal(self.player, x, y)):
			return 1
		elif(self.turnCount == 9):
			return -1
		else:
			if(self.player == 'x'):
				self.player = 'o'
			else:
				self.player = 'x'
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

	def checkDiagonal(self, character, x, y):
		if(self.board[1][1] != character):
			return False
		rtn1 = True
		rtn2 = True
		y1 = 0
		y2 = 2
		for x in range(0,3):
			if(self.board[x][y1] != character):
				rtn1 = False
			if(self.board[x][y2] != character):
				rtn2 = False
			y1 += 1
			y2 -= 1
		if(rtn1 or rtn2):
			return True
		else:
			return False