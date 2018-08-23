# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:06:23 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
Hi.setBlocks(x,y,z,x+40,y+10,z+40,51)
Hi.setBlocks(x+1,y+1,z+1,x+39,y+9,z+39,0)w