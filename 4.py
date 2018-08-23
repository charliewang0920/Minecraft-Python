# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:34:23 2018

@author: NTPU
"""
import time
from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
while y<201:
    Hi.setBlock(x,y-1,z,20)
    time.sleep(0.5)
    Hi.setBlock(x+1,y-1,z,20)
    time.sleep(0.5)
    Hi.setBlock(x+2,y-1,z,20)
    time.sleep(0.5)
    Hi.setBlock(x+3,y-1,z,20)
    time.sleep(0.5)
    Hi.setBlock(x+3,y-1,z-1,20)
    time.sleep(0.5)
    Hi.setBlock(x+3,y-1,z-1,20)
    time.sleep(0.5)
    Hi.setBlock(x+3,y-1,z-2,20)
    time.sleep(0.5)
    Hi.setBlock(x+3,y-1,z-3,20)
    time.sleep(0.5)
    Hi.setBlock(x+2,y-1,z-3,20)
    time.sleep(0.5)
    Hi.setBlock(x+1,y-1,z-3,20)
    time.sleep(0.5)
    Hi.setBlock(x,y-1,z-3,20)
    time.sleep(0.5)
    Hi.setBlock(x,y-1,z-2,20)
    time.sleep(0.5)
    Hi.setBlock(x,y-1,z-1,20)
    time.sleep(0.5)
    y = y+1