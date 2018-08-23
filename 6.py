# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:59:46 2018

@author: NTPU
"""
import random
from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
#Hi.player.setPos(x+0.5,y,z+0.5)
Hi.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,95,color)
color= random.randrange(1,16)