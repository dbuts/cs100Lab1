# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:24:00 2017

Main loop for the python project

@author: Franklin Navarro
"""

import gameLogic
import interface
from time import sleep

gb = gameLogic.gameBoard()

def update(x, y, gameBoard, self):
	gameBoard.updateBoard(x, y)
	self.updateState(gb.board)
	win = gb.checkWin(x,y)
	if(win == 1):
		self.win(gb.player)

	elif(win == -1):
		self.draw()


gui = interface.Interface(update, gb)



	