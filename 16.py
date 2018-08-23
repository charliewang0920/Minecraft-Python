# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:38:52 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
a = x-1,y-1,z
b = x-2,y-1,z
for i in range(50):
    Hi.setBlock(x+i,y-1,z+i,1)
    Hi.setBlock(x+i,y-1,z+i,1)
    Hi.setBlock(x+i,y-1,z+i,1)
    Hi.setBlock(x+i,y-1,z+i,1)
    
    
    
    
    
"""    village
    x 345
    y 72
    z 276
    """