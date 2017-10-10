# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:25:15 2017

Holds the various functions for processsing the game

@author: David Butler
"""
class gameBoard:
	board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

	def __init__(self):
		self.board = board

	def updateBoard(self, character, x, y):
		self.board[x][y] = character
		checkWin(self, character, x, y)

	#def checkWin(self, charater, x, y):

