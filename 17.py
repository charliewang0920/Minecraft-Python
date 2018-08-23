# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:39:43 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()

Hi.setBlocks(x+1,y+3,z+1,x-1,y+5,z-1,161)
Hi.setBlocks(x,y,z,x,y+3,z,17)