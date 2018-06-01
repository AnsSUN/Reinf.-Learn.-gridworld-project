# -*- coding: utf-8 -*-
"""
Created on Thu May 03 15:08:26 2018

@author: anshu
"""
import numpy as np
import pygame
import sys


pygame.init()
width = 800
height = 500
x = 0
y = 0
x_agent=25
y_agent=25
play_continue=True
screen= pygame.display.set_mode((width, height))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
yellow= (255,255,0)

screen.fill(yellow)
# Set title of screen
pygame.display.set_caption("Reinforcement Learning Gridworld Problem")
pygame.draw.line(screen, (0,0,0), (x, y), (800, x), (3))
pygame.draw.line(screen, (0,0,0), (x, y), (x, 500), (3))
#pygame.draw.circle(screen, red, [x_agent, y_agent], 10)
#pygame.draw.polygon(screen, darkBlue, [[775, 455], [755, 475],[755, 495], [795, 495], [795, 475]])
#pygame.draw.rect(screen, white, [770, 475, 10, 20])

#pygame.draw.lines(screen, black, False, (x, y), (580, x), 1)
#pygame.draw.lines(screen, black, False,(x, y), (x, 380), 1)

## Grid creation for the environment:


clock = pygame.time.Clock()
clock1= pygame.time.Clock()
while (play_continue):

 clock.tick()
 pygame.display.update()
 for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
 x+=50
 y+=50
 pygame.draw.line(screen, (0,0,0), (0, y), (800, x), (3))
 pygame.draw.line(screen, (0,0,0), (x, 0), (x, 500), (3))
 pygame.display.update()
 
 clock = pygame.time.Clock()

play_continue=False

play_continue=True
while (play_continue):

 clock.tick()
 pygame.display.update()
 for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit(); 
 x_agent+=50
 y_agent+=50
 pygame.draw.circle(screen, red, [x_agent, y_agent], 10)
 #pygame.draw.line(screen, (0,0,0), (x, 0), (x, 500), (3))
 pygame.display.update()
 clock1.tick(23)
 
 
 ### Iteration for agent to move in grid world #################
 #clock.tick(30)
 #pygame.display.update()
 

 
 
 

