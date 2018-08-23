# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:57:52 2018

@author: NTPU
"""
import random
from time import sleep
from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
r = random.randrange(1,7)
c = random.randrange(1,16)
l = random.randrange(2,16)
for i in range(500):
    if r ==1:
        sleep(0.1)
        Hi.setBlocks(x,y,z,x-l,y,z,35,c)
        x = x+l
    elif r==2:
        sleep(0.1)
        Hi.setBlocks(x,y,z,x-l,y,z,35,c)
        x = x-l
    elif r==3:
        sleep(0.1)
        Hi.setBlocks(x,y,z,x,y,z+l,35,c)
        z =z+l
    elif r==4:
        sleep(0.1)
        Hi.setBlocks(x,y,z,x,y,z-l,35,c)
        z=z-l
    elif r==5:
        sleep(0.1)
        Hi.setBlocks(x,y,z,x,y+l,z,35,c)
        y=y+l
    elif r==6:
        sleep(0.1)
        Hi.setBlocks(x,y,z,x,y-l,z,35,c) 
        y=y-l
    
    




