# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:28:38 2018

@author: anshu
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 03 15:08:26 2018

@author: anshu
"""
import numpy as np
import matplotlib.pyplot as plt
import pygame
import sys

################Reinforcement Learning initiallization############
def Reinf_learn(s_states, a_actions):
    # Change if you get sum of row=1
    P_trans= np.random.rand(a_actions, s_states,s_states)
    alpha=0.9 
    gamma=0.9
    reward=-1
    #vq= np.zeros((s_states,1))
    V_init=np.zeros((s_states,1)) #initial guess for old value function
    V_upd=np.zeros((s_states,1)) #for storing new value function
    action_state=0.0
    delta=[]
    #diff=0.00001 # to get precision in the result
    #delta=-200
    i=0
    while(i<1000):
         #print(V_init.T)
         for s in range(s_states):#loop over states: s=0,1,...,n_states-1
             Q=[]#create an empty list to store Q-function values
             #change=np.zeros((s_states,1)) 
             #x= np.zeros((s_states,1))
             for a in range(a_actions):
                 Q.append(reward+gamma*(np.dot(P_trans[[a],[s]],V_init))) 
                 #Q.append(reward+gamma*(np.dot(P_trans[[a],[s]],V_init))) #loop over actions: a=0,1,...,m_actions-1
             V_upd[s]=max(Q) #optimal value function equals the smallest Q-function value
             V_init[s]=(1-alpha)*Q[s]+alpha*(reward+gamma*V_upd[s])
         i+=1
         #delta.append(abs(V_upd.T-V_init.T))
         for state in range(s_states): 
            delta.append(abs(V_upd[state]-V_init[state]))
            V_init[state]=V_upd[state] #update the value function
         action_state= np.argmax(V_upd)
    return action_state, delta;
########################################################
s_states=4
a_actions=4
action=0
learn=[]
#####################gridworld##########################

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
world = pygame.image.load("gridprob.jpg")
pygame.draw.circle(world, red, [x_agent, y_agent], 10)
pygame.draw.polygon(world, darkBlue, [[775, 455], [755, 475],[755, 495], [795, 495], [795, 475]])
pygame.draw.rect(world, white, [770, 475, 10, 20])

#pygame.draw.lines(screen, black, False, (x, y), (580, x), 1)
#pygame.draw.lines(screen, black, False,(x, y), (x, 380), 1)

## Grid creation for the environment:

count_time=0
clock = pygame.time.Clock()

while (play_continue):
 screen.blit(world,(0,0))
 clock.tick()
 pygame.display.update()

 for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
 if (count_time==2):
     world = pygame.image.load("gridprob.jpg")
     pygame.draw.polygon(world, darkBlue, [[775, 455], [755, 475],[755, 495], [795, 495], [795, 475]])
     pygame.draw.rect(world, white, [770, 475, 10, 20])
     pygame.display.update()
     count_time=0
 if(x_agent==775 and y_agent==475):
     play_continue=False
 else:
    action, learn= Reinf_learn(s_states, a_actions)
 if (x_agent<800 and y_agent<500 and x_agent>0 and y_agent>0) :       
     if action==0:
         x_agent+=50;
     if action==1:    
         x_agent-=50;
     if action==2:
         y_agent -= 50;
     if action==3:
         y_agent += 50;
 if (x_agent>800 and y_agent<500 and y_agent>0):
     x_agent-=50;
 if (x_agent<800 and y_agent>500 and x_agent>0):
     y_agent -= 50;
 if (y_agent>500 and x_agent>800):
     x_agent-=50;
     y_agent -= 50;
 if(x_agent<0 and y_agent<500 and y_agent>0):
     x_agent+=50;
 if(x_agent<800 and y_agent<0 and x_agent>0):
     y_agent += 50;
 if (x_agent<0 and y_agent<0):
     x_agent+=50;
     y_agent += 50;
 count_time +=1
 pygame.draw.circle(world, red, [x_agent, y_agent], 10)
 pygame.display.update()
 clock.tick(2)
 
print(learn)
learn_array=np.asarray(learn)
learn_plot=learn_array[::3,]
plt.plot(learn_array[:150,])
plt.ylabel('Learning_through iteration')
plt.show()
 
 

